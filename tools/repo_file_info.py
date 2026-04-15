#!/usr/bin/env python3
"""
Repository File Info Generator.

Interactive tool that scans files/archives in a selected folder and generates
size + SHA-256 hash data for repository files.json / mod.json.

Interactive workflow (no arguments):
  1. Select a folder via file explorer dialog (or enter path manually)
  2. Choose scan mode: all files or archives only
  3. Choose recursive scan or not
  4. Choose output format: plain text or JSON (single / multi-file)
  5. Optionally enter a URL prefix for download links
  6. Results are saved to a file next to the scanned folder

CLI mode (with arguments):
    python repo_file_info.py "D:/releases/" --json --archives-only
    python repo_file_info.py "D:/releases/" --recursive --json --multi --save
"""

import argparse
import hashlib
import json
import os
import sys
import tkinter as tk
from datetime import datetime
from pathlib import Path
from tkinter import filedialog
from typing import Dict, List, Optional


# ── Hashing & File Info ─────────────────────────────────────────────────────

def compute_sha256(file_path: Path, chunk_size: int = 65536) -> str:
    """Compute SHA-256 hash of a file.

    Args:
        file_path: Path to the file.
        chunk_size: Read buffer size in bytes.

    Returns:
        SHA-256 hash as hex string with 'sha256:' prefix.
    """
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            sha256.update(chunk)
    return f"sha256:{sha256.hexdigest()}"


def get_file_info(file_path: Path) -> Dict[str, object]:
    """Get size and hash for a single file.

    Args:
        file_path: Path to the file.

    Returns:
        Dict with 'name', 'size', 'hash', and 'size_human' keys.
    """
    size = file_path.stat().st_size
    file_hash = compute_sha256(file_path)
    return {
        "name": file_path.name,
        "size": size,
        "hash": file_hash,
        "size_human": format_size(size),
    }


def format_size(size_bytes: int) -> str:
    """Format byte size to human-readable string.

    Args:
        size_bytes: Size in bytes.

    Returns:
        Human-readable size string (e.g. '5.2 MB').
    """
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.1f} MB"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.2f} GB"


# ── Archive Extensions ──────────────────────────────────────────────────────

ARCHIVE_EXTENSIONS = {
    ".7z", ".zip", ".rar", ".gz", ".bz2", ".tar",
    ".iso", ".cab", ".xz", ".lzma",
}


# ── Scanning ────────────────────────────────────────────────────────────────

def scan_path(
    target_path: Path,
    recursive: bool = False,
    archives_only: bool = False,
) -> List[Dict[str, object]]:
    """Scan a file or directory for file info.

    Args:
        target_path: Path to a file or directory.
        recursive: If True, scan subdirectories recursively.
        archives_only: If True, only include archive files.

    Returns:
        List of file info dicts.
    """
    results: List[Dict[str, object]] = []

    if target_path.is_file():
        if archives_only and target_path.suffix.lower() not in ARCHIVE_EXTENSIONS:
            return results
        print(f"  Hashing: {target_path.name} ...", end=" ", flush=True)
        info = get_file_info(target_path)
        print(f"OK ({info['size_human']})")
        results.append(info)
    elif target_path.is_dir():
        pattern = "**/*" if recursive else "*"
        files = sorted(target_path.glob(pattern))
        for file in files:
            if not file.is_file():
                continue
            if archives_only and file.suffix.lower() not in ARCHIVE_EXTENSIONS:
                continue
            rel_path = file.relative_to(target_path)
            print(f"  Hashing: {rel_path} ...", end=" ", flush=True)
            info = get_file_info(file)
            info["relative_path"] = str(rel_path)
            print(f"OK ({info['size_human']})")
            results.append(info)
    else:
        print(f"Error: path not found: {target_path}", file=sys.stderr)

    return results


# ── Formatters ──────────────────────────────────────────────────────────────

def format_plain(results: List[Dict]) -> str:
    """Format results as a plain text table.

    Args:
        results: List of file info dicts.

    Returns:
        Formatted table string.
    """
    if not results:
        return "No files found."

    lines = []
    lines.append(f"{'File':<50} {'Size (bytes)':>15} {'Size':>10} {'Hash'}")
    lines.append("-" * 130)

    for info in results:
        name = info.get("relative_path", info["name"])
        lines.append(
            f"{name:<50} {info['size']:>15} {info['size_human']:>10} {info['hash']}"
        )

    lines.append("")
    lines.append(f"Total files: {len(results)}")
    total_size = sum(r["size"] for r in results)
    lines.append(f"Total size:  {total_size} bytes ({format_size(total_size)})")
    return "\n".join(lines)


def format_json_single(results: List[Dict], url_prefix: str = "") -> str:
    """Format results as JSON snippets for single-file versions.

    Each file produces a separate file group with one version entry.

    Args:
        results: List of file info dicts.
        url_prefix: URL prefix for download links.

    Returns:
        JSON string ready to paste into files.json.
    """
    file_groups = []
    for info in results:
        version_entry = {
            "version": "VERSION",
            "expected_files": {"1": info["name"]},
            "url": {"1": url_prefix + info["name"] if url_prefix else f"URL/{info['name']}"},
            "size": {"1": info["size"]},
            "hash": {"1": info["hash"]},
        }
        file_group = {
            "display_name": info["name"],
            "category": "MAIN",
            "versions": [version_entry],
        }
        file_groups.append(file_group)

    output = {"files": file_groups}
    return json.dumps(output, indent=2, ensure_ascii=False)


def format_json_multi(results: List[Dict], url_prefix: str = "") -> str:
    """Format results as JSON snippets for multi-file versions (mods).

    All files are grouped under a single file group with one version entry
    containing numbered size/hash/url/expected_files dicts.

    Args:
        results: List of file info dicts.
        url_prefix: URL prefix for download links.

    Returns:
        JSON string ready to paste into files.json.
    """
    urls = {}
    expected_files = {}
    sizes = {}
    hashes = {}

    for idx, info in enumerate(results, start=1):
        key = str(idx)
        urls[key] = url_prefix + info["name"] if url_prefix else f"URL/{info['name']}"
        expected_files[key] = info["name"]
        sizes[key] = info["size"]
        hashes[key] = info["hash"]

    version_entry = {
        "version": "VERSION",
        "description": "",
        "expected_files": expected_files,
        "url": urls,
        "size": sizes,
        "hash": hashes,
    }

    file_group = {
        "display_name": results[0]["name"] if results else "DISPLAY_NAME",
        "category": "MAIN",
        "versions": [version_entry],
    }

    output = {"files": [file_group]}
    return json.dumps(output, indent=2, ensure_ascii=False)


# ── Save Results ────────────────────────────────────────────────────────────

def save_results_to_file(
    target_path: Path,
    content: str,
    archives_only: bool,
    output_format: str,
    save_dir: Optional[Path] = None,
) -> Path:
    """Save results to a file.

    Args:
        target_path: The scanned folder/file path (used for filename generation).
        content: Formatted output string.
        archives_only: Whether archives-only mode was used.
        output_format: 'plain', 'json_single', or 'json_multi'.
        save_dir: Directory to save the file in. If None, saves next to
            the scanned folder.

    Returns:
        Path to the saved file.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    mode_tag = "archives" if archives_only else "all"
    fmt_tag = output_format.replace("_", "-")

    if target_path.is_file():
        default_parent = target_path.parent
        base_name = target_path.stem
    else:
        default_parent = target_path
        base_name = target_path.name

    parent = save_dir if save_dir is not None else default_parent

    ext = ".json" if "json" in output_format else ".txt"
    filename = f"file_info_{base_name}_{mode_tag}_{fmt_tag}_{timestamp}{ext}"
    out_path = parent / filename

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

    return out_path


# ── Interactive Folder Selection ────────────────────────────────────────────

def select_folder_interactive() -> Optional[Path]:
    """Open a folder selection dialog or accept manual path input.

    Returns:
        Selected folder Path, or None if cancelled.
    """
    print("\nSelect folder to scan:")
    print("1. Choose folder via file explorer")
    print("2. Enter path manually")

    choice = input("\nYour choice (1-2): ").strip()

    if choice == "1":
        root = tk.Tk()
        root.withdraw()
        try:
            chosen = filedialog.askdirectory(
                title="Select folder to scan",
            )
        finally:
            root.destroy()

        if not chosen:
            print("Selection cancelled.")
            return None

        target = Path(chosen).resolve()
        print(f"Selected folder: {target}")
        return target

    elif choice == "2":
        raw = input("Enter folder path: ").strip().strip('"').strip("'")
        if not raw:
            print("No path specified.")
            return None

        target = Path(raw).resolve()
        if not target.exists():
            print(f"Error: path does not exist: {target}")
            return None

        print(f"Selected folder: {target}")
        return target

    else:
        print("Invalid choice.")
        return None


def select_scan_mode() -> Optional[bool]:
    """Ask user whether to scan all files or archives only.

    Returns:
        True for archives only, False for all files, None if cancelled.
    """
    print("\nWhat to scan?")
    print("1. All files")
    print("2. Archives only (.7z, .zip, .rar, ...)")

    choice = input("\nYour choice (1-2): ").strip()

    if choice == "1":
        return False
    elif choice == "2":
        return True
    else:
        print("Invalid choice.")
        return None


def select_recursive() -> bool:
    """Ask user whether to scan subdirectories recursively.

    Returns:
        True for recursive scan, False otherwise.
    """
    print("\nScan subdirectories recursively?")
    print("1. No (only files in the selected folder)")
    print("2. Yes (including all subfolders)")

    choice = input("\nYour choice (1-2): ").strip()
    return choice == "2"


def select_output_format() -> Optional[str]:
    """Ask user for output format.

    Returns:
        'plain', 'json_single', or 'json_multi'. None if cancelled.
    """
    print("\nOutput format:")
    print("1. Table (plain text)")
    print("2. JSON (single-file — one entry per file)")
    print("3. JSON (multi-file — all files in one version entry)")

    choice = input("\nYour choice (1-3): ").strip()

    if choice == "1":
        return "plain"
    elif choice == "2":
        return "json_single"
    elif choice == "3":
        return "json_multi"
    else:
        print("Invalid choice.")
        return None


def ask_url_prefix() -> str:
    """Ask user for optional URL prefix.

    Returns:
        URL prefix string (may be empty).
    """
    print("\nURL prefix for download links (leave empty if not needed):")
    print("Example: https://github.com/user/repo/releases/download/v1.0/")
    prefix = input("> ").strip()
    return prefix


def select_save_location(default_dir: Path) -> Optional[Path]:
    """Ask user where to save the output file.

    Args:
        default_dir: Default save directory (the scanned folder).

    Returns:
        Selected directory Path, or None if cancelled.
    """
    print("\nWhere to save the result?")
    print(f"1. Scanned folder ({default_dir})")
    print("2. Choose folder via file explorer")
    print("3. Enter path manually")

    choice = input("\nYour choice (1-3): ").strip()

    if choice == "1":
        return default_dir

    elif choice == "2":
        root = tk.Tk()
        root.withdraw()
        try:
            chosen = filedialog.askdirectory(
                title="Select folder to save results",
                initialdir=str(default_dir),
            )
        finally:
            root.destroy()

        if not chosen:
            print("Selection cancelled, saving to scanned folder.")
            return default_dir

        target = Path(chosen).resolve()
        print(f"Save folder: {target}")
        return target

    elif choice == "3":
        raw = input("Enter folder path: ").strip().strip('"').strip("'")
        if not raw:
            print("No path specified, saving to scanned folder.")
            return default_dir

        target = Path(raw).resolve()
        if not target.is_dir():
            print(f"Folder does not exist: {target}")
            create = input("Create it? (y/n): ").strip().lower()
            if create == "y":
                target.mkdir(parents=True, exist_ok=True)
                print(f"Created: {target}")
            else:
                print("Saving to scanned folder.")
                return default_dir

        print(f"Save folder: {target}")
        return target

    else:
        print("Invalid choice, saving to scanned folder.")
        return default_dir


# ── Interactive Mode ────────────────────────────────────────────────────────

def run_interactive():
    """Run the tool in interactive mode with folder selection dialogs."""

    print("=" * 60)
    print("  Repository File Info Generator")
    print("=" * 60)

    # 1. Select folder
    target = select_folder_interactive()
    if target is None:
        input("\nPress Enter to exit...")
        return

    # 2. Scan mode: all files or archives only
    archives_only = select_scan_mode()
    if archives_only is None:
        input("\nPress Enter to exit...")
        return

    # 3. Recursive scan?
    recursive = select_recursive()

    # 4. Output format
    output_format = select_output_format()
    if output_format is None:
        input("\nPress Enter to exit...")
        return

    # 5. URL prefix (only for JSON)
    url_prefix = ""
    if output_format in ("json_single", "json_multi"):
        url_prefix = ask_url_prefix()

    # ── Scan ────────────────────────────────────────────────────────────
    print(f"\n{'=' * 60}")
    mode_str = "archives only" if archives_only else "all files"
    rec_str = " (recursive)" if recursive else ""
    print(f"Scanning: {target}")
    print(f"Mode: {mode_str}{rec_str}")
    print(f"{'=' * 60}\n")

    results = scan_path(target, recursive=recursive, archives_only=archives_only)

    if not results:
        print("\nNo files found.")
        input("\nPress Enter to exit...")
        return

    # ── Format ──────────────────────────────────────────────────────────
    if output_format == "plain":
        content = format_plain(results)
    elif output_format == "json_single":
        content = format_json_single(results, url_prefix=url_prefix)
    elif output_format == "json_multi":
        content = format_json_multi(results, url_prefix=url_prefix)
    else:
        content = format_plain(results)

    # ── Display ─────────────────────────────────────────────────────────
    print(f"\n{'=' * 60}")
    print("Result:")
    print(f"{'=' * 60}")
    print(content)

    # ── Save location ───────────────────────────────────────────────────
    save_dir = select_save_location(target if target.is_dir() else target.parent)

    # ── Save to file ────────────────────────────────────────────────────
    out_path = save_results_to_file(
        target, content, archives_only, output_format, save_dir=save_dir,
    )
    print(f"\n{'=' * 60}")
    print(f"Result saved to: {out_path}")
    print(f"{'=' * 60}")

    input("\nPress Enter to exit...")


# ── CLI Mode ────────────────────────────────────────────────────────────────

def run_cli():
    """Run the tool in command-line mode with arguments."""
    parser = argparse.ArgumentParser(
        description="Generate file size and SHA-256 hash info for repository files.json.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "D:/releases/MyMod_v2.0.7z"
  %(prog)s "D:/releases/" --json
  %(prog)s "D:/releases/" --recursive --json --url-prefix "https://example.com/files/"
  %(prog)s "D:/releases/" --json --multi
        """,
    )
    parser.add_argument(
        "path",
        type=str,
        help="Path to a file or directory to scan.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output as JSON snippet for files.json.",
    )
    parser.add_argument(
        "--multi",
        action="store_true",
        help="Multi-file mode: group all files into one version entry with numbered keys.",
    )
    parser.add_argument(
        "--recursive", "-r",
        action="store_true",
        help="Recursively scan subdirectories.",
    )
    parser.add_argument(
        "--archives-only", "-a",
        action="store_true",
        help="Only include archive files (7z, zip, rar, etc.).",
    )
    parser.add_argument(
        "--url-prefix",
        type=str,
        default="",
        help="URL prefix for download links in JSON output.",
    )
    parser.add_argument(
        "--save", "-s",
        action="store_true",
        help="Save results to a file next to the scanned folder.",
    )

    args = parser.parse_args()
    target = Path(args.path).resolve()

    if not target.exists():
        print(f"Error: path does not exist: {target}", file=sys.stderr)
        sys.exit(1)

    print(f"Scanning: {target}")
    print()

    results = scan_path(target, recursive=args.recursive, archives_only=args.archives_only)

    if not results:
        print("No files found.")
        sys.exit(0)

    print()

    if args.json:
        if args.multi:
            output = format_json_multi(results, url_prefix=args.url_prefix)
            fmt = "json_multi"
        else:
            output = format_json_single(results, url_prefix=args.url_prefix)
            fmt = "json_single"
        print("=" * 60)
        print("JSON output (paste into files.json):")
        print("=" * 60)
        print(output)
    else:
        output = format_plain(results)
        fmt = "plain"
        print(output)

    if args.save:
        out_path = save_results_to_file(target, output, args.archives_only, fmt)
        print(f"\nSaved to: {out_path}")


# ── Entry Point ─────────────────────────────────────────────────────────────

def main():
    """Entry point: interactive mode if no arguments, CLI mode otherwise."""
    if len(sys.argv) > 1:
        run_cli()
    else:
        run_interactive()


if __name__ == "__main__":
    main()
