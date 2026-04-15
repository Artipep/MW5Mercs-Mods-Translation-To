# MW5:Mercs Mod Manager — Documentation / Документация / Документація

<p align="center">
  <img src="logo/logo.png" alt="MW5:Mercs Mod Manager" width="100%"/>
</p>

> **[English](#english)** | **[Русский](#русский)** | **[Українська](#українська)**

---

# English

## Table of Contents

- [For Users](#for-users)
  - [Installation](#installation)
  - [First Run](#first-run)
  - [Interface](#interface)
  - [Managing Mods](#managing-mods)
  - [Load Order](#load-order)
  - [Load Order Rules](#load-order-rules)
  - [Presets](#presets)
  - [Modpacks](#modpacks)
  - [Catalog — Nexusmods](#catalog--nexusmods)
  - [Third-Party Repositories](#third-party-repositories)
  - [Installing a Mod from Archive](#installing-a-mod-from-archive)
  - [Multi-Folder Archives](#multi-folder-archives)
  - [Settings](#settings)
- [For Mod Makers and Repository Owners](#for-mod-makers-and-repository-owners)
  - [Repository System Overview](#repository-system-overview)
  - [Repository Structure](#repository-structure)
  - [repository.json](#repositoryjson)
  - [Repository Categories](#repository-categories)
  - [Type repository — Mod Structure](#type-repository--mod-structure)
  - [Type nexus_api — Mod Structure](#type-nexus_api--mod-structure)
  - [Mod Metadata Files](#mod-metadata-files)
  - [Translation Compatibility (for_mod_name)](#translation-compatibility-for_mod_name)
  - [featured.json — Featured Mods](#featuredjson--featured-mods)
  - [mod_manager_properties.json](#mod_manager_propertiesjson)
  - [mod_manager_install_rules.json](#mod_manager_install_rulesjson)
  - [Full Repository Example](#full-repository-example)
  - [Publishing a Repository](#publishing-a-repository)
  - [Notes for Repository Developers](#notes-for-repository-developers)
- [Tools](#tools)
  - [repo_file_info.py — File Size & Hash Generator](#repo_file_infopy--file-size--hash-generator)

---

## For Users

### Installation

#### Windows

1. Download the archive `MW5Mercs_Mod_Manager_vX.X.X_windows_x64.zip` from the Releases page
2. Extract to any folder (e.g. `C:\Tools\MW5ModManager`)
3. Run `MW5Mercs Mod Manager.exe`

#### Linux

1. Download the archive `MW5Mercs_Mod_Manager_vX.X.X_linux_x64.zip`
2. Extract: `unzip MW5Mercs_Mod_Manager_*.zip`
3. Grant execute permission: `chmod +x "MW5Mercs Mod Manager"`
4. Run: `./"MW5Mercs Mod Manager"`

#### System Requirements

| | Windows | Linux |
|---|---|---|
| OS | Windows 10/11 x64 | Ubuntu 20.04+, Fedora 36+, Arch and others |
| Game | MechWarrior 5: Mercenaries (Steam, Epic, GOG) | same |
| .NET / Runtime | not required | not required |

---

### First Run

On first launch, a setup wizard opens. You need to specify:

**Game folder** — the root folder of MechWarrior 5, for example:
```
D:\Games\Steam\steamapps\common\MechWarrior 5 Mercenaries
```

**Steam Workshop folder** (optional) — the folder with Steam Workshop mods:
```
D:\Games\Steam\steamapps\workshop\content\784080
```

**Interface language** — English, Русский, Українська.

After that, the program will automatically find the mods folder `MW5Mercs/Mods` inside the game folder.

---

### Interface

The program consists of several pages accessible via the side menu:

| Page | EN Label | Description |
|---|---|---|
| **Home** | Home | Installed mods list with quick management, updates overview, game launch |
| **Mods** | Mods | Detailed list of all installed mods with tabs: OVERVIEW, CONFLICTS, RULES, PRESETS |
| **Files** | Files | File system browser for the mods folder |
| **Catalog** | Catalog | Search and install mods from Nexusmods and repositories |
| **Settings** | Settings | Program configuration |

On the **Catalog** page, there are additional tabs:

| Tab | EN Label | Description |
|---|---|---|
| **Install** | INSTALL | Install mods from archive or folder |
| **Mods** | MODS | Browse and install mods from Nexusmods and repository catalogs |
| **Translations** | TRANSLATIONS | Browse and install translation mods |
| **Update** | UPDATE | Check and install updates for linked mods |
| **Links** | LINKS | Manage links between installed mods and Nexusmods / repository sources |
| **Modpacks** | MODPACKS | Create, manage, and apply mod collections with presets |

---

### Managing Mods

On the **Mods** page (tab OVERVIEW), all found mods are listed from:
- the `MW5Mercs/Mods` folder inside the game
- the Steam Workshop folder (if configured)

Available actions for each mod:
- **Enable / Disable** — changes the `defaultEnabled` field in the mod's `mod.json`
- **Change load order** — by dragging or entering a number
- **Open mod folder** — in Explorer / file manager
- **Delete** — removes the mod folder from disk

> **Note:** load order is defined by the `defaultLoadOrder` field in each mod's `mod.json`. Higher numbers load later. In case of conflict, the mod with the higher value wins.

#### Conflicts

The program automatically detects conflicts — when two or more mods modify the same game files. Conflicts are displayed on the CONFLICTS tab on the **Mods** page.

---

### Load Order

MW5 loads mods in the order defined by the `defaultLoadOrder` field in `mod.json`. A mod with a higher number overrides mods with lower numbers when files conflict.

In the program, order can be changed by:
- **Dragging** a mod card
- **Entering a number** directly
- **Arrow buttons** — move up/down

After changing the order, the program physically updates `mod.json` files — changes take effect on the next game launch.

---

### Load Order Rules

Rules are constraints the program applies automatically during sorting.

#### Rule Types

| Type | Description |
|---|---|
| **After mod** (`after`) | This mod must load after the specified mod |
| **Before mod** (`before`) | This mod must load before the specified mod |
| **First group** (`first`) | This mod must always be in the first group (low numbers) |
| **Last group** (`last`) | This mod must always be in the last group (high numbers) |

#### Creating a Rule

1. Go to the **Mods** page → RULES tab
2. Click **Add rule**
3. Select the mod and rule type
4. For `after`/`before` rules — select the target mod
5. Click **Save**

Rules are stored in the file `mod_manager_rules.json` in the mods folder. Clicking **Apply** re-sorts mods according to all active rules.

---

### Presets

A preset is a saved configuration: which mods are enabled and their load order.

#### Saving a Preset

1. Go to the **Mods** page → PRESETS tab
2. Click **Mods Preset** → **Create**
3. Enter a name for the preset

#### Applying a Preset

1. Select a preset from the list
2. Click **Apply**

Presets are stored in `config/presets/mods/` as JSON files. Each file represents one preset:

```json
{
  "1": {
    "mods": {
      "ModFolderName": {
        "bEnabled": true,
        "defaultLoadOrder": 1
      },
      "AnotherMod": {
        "bEnabled": false,
        "defaultLoadOrder": 2
      }
    }
  }
}
```

---

### Modpacks

A modpack is a collection of mod references, presets, and repository links bundled together. Unlike presets (which only store mod enabled/disabled states and load order), modpacks store full mod metadata including sources (Nexusmods, repositories).

Modpacks do **not** contain actual mod files — only references to them (folder names, Nexusmods IDs, repository URLs). When applying a modpack, the program adds uninstalled mods to the install queue and restores included presets.

#### Creating a Modpack

1. Go to **Catalog** → **MODPACKS** tab (right panel)
2. Click **Create**
3. The catalog switches to show installed linked mods
4. Check the mods you want to include (you can also browse Nexusmods or repositories as source)
5. Optionally select **Mods Preset** and/or **Rules Preset** from existing presets
6. Linked repositories are added automatically from the selected mods
7. Enter a modpack name
8. Click **Create Modpack**

#### Applying a Modpack

1. Select a modpack from the list
2. Click **Apply** (✓)
3. The program:
   - Checks which mods are already installed
   - Adds uninstalled mods to the install queue
   - Restores and applies included presets (mods and rules)
   - Shows a summary message

#### Previewing a Modpack

Click on a modpack name (without pressing Apply) to preview its contents:
- **Mods** — list of included mods with installation status
- **Rules Presets** — included rules presets
- **Mods Presets** — included mods presets
- **Repositories** — linked repositories

#### Import / Export

- **Import**: Click **Import** → select a `.json` modpack file
- **Export**: Select a modpack → click **Export** → choose save location

Modpacks are stored in `config/modpacks/` as JSON files. Each file contains the modpack name, list of mods with metadata, preset data, and repository URLs.

---

### Catalog — Nexusmods

On the **Catalog** page (tabs MODS and TRANSLATIONS), mods from Nexusmods are displayed via the GraphQL v2 API.

**No authorization required.** The program accesses the Nexusmods catalog, retrieves mod information, and generates download links without requiring a Nexusmods account or API key.

**Features:**
- Search mods by name
- View description, screenshots, and mod files
- Download and install mods directly from the program
- Check for updates for linked mods

---

### Third-Party Repositories

Repositories are separate mod catalogs hosted on any HTTP/HTTPS server or locally. This is the primary system for distributing mods not hosted on Nexusmods (e.g. early access, translations).

#### Adding a Repository

1. Go to **Settings** → GENERAL tab
2. Click **Add** in the Repositories section
3. Enter the repository URL or path to a local folder:
   - HTTP/HTTPS: `https://example.com/my-mw5-repo`
   - Local: `D:\MyRepository` or `/home/user/mw5-repo`
4. Enter a display name
5. Click **Save**

After adding, the program will download `repository.json` and show available categories in the catalog.

---

### Installing a Mod from Archive

A mod can also be installed from a ready-made archive (`.7z`, `.zip`, `.rar`) or from a folder.

1. Go to **Catalog** → INSTALL tab
2. Select an archive or folder with the mod
3. The program will extract the archive to the game's mods folder

Supported formats: `.7z`, `.zip`, `.rar`, `.tar`, `.gz`.
Built-in 7-Zip is used for extraction (bundled with the program).

---

### Multi-Folder Archives

If an archive contains multiple mod folders (each with its own `mod.json`), the program will install all of them. Each folder is installed separately into the mods directory.

When creating a link to a Nexusmods or repository source for such a mod, the link is automatically applied to all sibling folders from the same archive.

---

### Settings

| Parameter | Description |
|---|---|
| **Game folder** | Path to MW5 (required) |
| **Steam Workshop folder** | Path to Steam Workshop folder (optional) |
| **Game version** | Text field for specifying the version (informational) |
| **Language** | Interface language: English, Русский, Українська |
| **Check Nexusmods updates** | Check for updates on startup |
| **Check repository updates** | Check for repository updates on startup |
| **Close on game launch** | Automatically close the manager when MW5 launches |
| **Downloads folder** | Where downloaded archives are saved |
| **Repositories** | List of connected repositories |

---

---

## For Mod Makers and Repository Owners

### Repository System Overview

A repository is a folder (local or on an HTTP/HTTPS server) containing:
- `repository.json` — repository description and its categories
- Category folders with subfolders for each mod

The program reads the repository on startup and shows mods in the catalog. When the user clicks "Install", it downloads the archive from the metadata URL and installs the mod.

**Supported hosting methods:**
- Any HTTP/HTTPS server with direct file access (GitHub Pages, Nginx, Apache, CDN)
- GitHub / GitLab / Codeberg / Bitbucket / Gitea / Forgejo repository (auto-normalizes web URLs to raw)
- Local folder on disk (for testing)

---

### Repository Structure

```
my-repository/
├── repository.json               # Required — repository description
│
├── early_access_mods/            # Category folder (path defined in repository.json)
│   ├── featured.json             # Optional — list of featured mods
│   ├── MyMod/                    # Mod folder (folder name = identifier)
│   │   ├── mod.json              # Required — mod metadata
│   │   ├── description.md        # Optional — description (Markdown)
│   │   ├── files.json             # Required — file list with versions and download links
│   │   ├── requirements.json     # Optional — dependencies
│   │   ├── changelog.json        # Optional — change history
│   │   └── preview.png           # Optional — preview image
│   └── AnotherMod/
│       ├── mod.json
│       └── files.json
│
├── early_access_translations/    # Translations folder
│   ├── featured.json
│   └── MyTranslation/
│       ├── mod.json
│       └── files.json
│
├── nexusmods_mods/               # nexus_api category (links to Nexusmods)
│   ├── featured.json
│   └── 12345/                    # Folder name = nexusmods mod ID
│       └── nexusmods_id.json
│
└── nexusmods_translations/       # Nexusmods translations
    ├── featured.json
    └── 67890/
        └── nexusmods_id.json
```

---

### repository.json

Root repository description file. **Required.**

```json
{
  "name": "My MW5 Repository",
  "categories": {
    "1": {
      "name": "early_access_mods",
      "type": "repository",
      "is_translation": false,
      "path": "early_access_mods",
      "display_name": "Early Access Mods",
      "mods": ["WeaponPack", "BalanceMod"]
    },
    "2": {
      "name": "early_access_translations",
      "type": "repository",
      "is_translation": true,
      "path": "early_access_translations",
      "display_name": "Translations",
      "mods": ["RussianTranslation"]
    },
    "3": {
      "name": "nexusmods_mods",
      "type": "nexus_api",
      "is_translation": false,
      "path": "nexusmods_mods",
      "display_name": "Popular Nexusmods Mods",
      "mods": ["12345"]
    },
    "4": {
      "name": "nexusmods_translations",
      "type": "nexus_api",
      "is_translation": true,
      "path": "nexusmods_translations",
      "display_name": "Nexusmods Translations",
      "mods": ["67890"]
    }
  }
}
```

#### repository.json Fields

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | yes | Display name of the repository |
| `categories` | object | yes | Categories object (key — arbitrary identifier) |

#### Category Fields

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | yes | Category name — any string. Used as the internal identifier for the category. Also serves as the folder path if `path` is not specified |
| `type` | string | yes | `repository` — full metadata in folder, `nexus_api` — only ID for Nexusmods API query |
| `is_translation` | bool | yes | `true` if the category contains translations |
| `path` | string | yes | Relative path to category folder from repository root |
| `display_name` | string | optional | Custom display name for the interface |
| `mods` | array of strings | required for remote | List of mod folder names. **Required** for remote (HTTP) repositories — without it the program cannot discover mods. For local repositories this is optional (the program reads the filesystem). |

> **Important:** category keys (`"1"`, `"2"`, ...) are arbitrary strings. The program uses the `name` field inside the object as the canonical identifier.

---

### Repository Categories

#### Type `repository`

The program downloads mod metadata from folders with `mod.json`. All descriptions, versions, dependencies are in the repository itself. Suitable for mods distributed outside Nexusmods.

#### Type `nexus_api`

The program uses `nexusmods_id.json` from the folder to get the mod ID, then loads full data via the Nexusmods GraphQL API. Used for displaying Nexusmods mods in the repository catalog.

---

### Type `repository` — Mod Structure

Each mod is a folder inside a category folder.

```
CategoryFolder/
└── MyModFolderName/     ← folder name = mod identifier in the program
    ├── mod.json          ← required
    ├── files.json        ← required
    ├── description.md    ← optional
    ├── requirements.json ← optional
    ├── changelog.json    ← optional
    └── preview.png       ← optional
```

> The mod folder name is used as a unique identifier — it must remain constant. Renaming the folder will break the link with the installed mod for users.

---

### Type `nexus_api` — Mod Structure

```
nexusmods_mods/
└── 12345/                      ← folder name = nexusmods ID (recommended)
    └── nexusmods_id.json        ← required
```

**nexusmods_id.json:**

```json
{
  "nexusmods_id": 12345
}
```

The program uses this number to query the Nexusmods API and retrieve the mod's name, description, images, and file links.

---

### Mod Metadata Files

#### mod.json — required

Main mod metadata in the repository. This is **not** the game's `mod.json` — it's a separate format.
Versions are stored separately in `files.json`.

**Mod example:**
```json
{
  "name": "My Awesome Mod",
  "author": "AuthorName",
  "mod_page": "https://github.com/author/my-awesome-mod",
  "images": {
    "preview": "preview.png"
  }
}
```

**Translation example:**
```json
{
  "for_mod_name": "Target Mod Name",
  "name": "Target Mod Name / Translation RUS",
  "author": "AuthorName",
  "images": {
    "preview": "preview.png"
  }
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | yes | Display name of the mod |
| `author` | string | recommended | Mod author |
| `for_mod_name` | string | translations only | Target mod name for translations. Set to `"Original_game"` to check compatibility against the game version from settings |
| `mod_page` | string | optional | Mod page URL (GitHub, forum, etc.) |
| `images.preview` | string | optional | Preview image filename or URL |

---

#### description.md — optional

Mod description in Markdown or plain text. If the file exists, the program uses it instead of the `description` field from `mod.json`.

---

#### files.json — required

Contains the list of mod files grouped by category, each with its own versions, download links, file sizes, and hashes.

**Mod files example:**
```json
{
  "files": [
    {
      "display_name": "Main Files",
      "category": "MAIN",
      "versions": [
        {
          "version": "2.1.0",
          "description": "Main mod files",
          "expected_files": { "1": "MyMod_v2.1.0.7z" },
          "url": { "1": "https://example.com/releases/v2.1.0/MyMod_v2.1.0.7z" },
          "size": { "1": 5242880 },
          "hash": { "1": "sha256:abcdef1234567890..." }
        },
        {
          "version": "2.0.0",
          "description": "Previous stable version",
          "expected_files": { "1": "MyMod_v2.0.0.7z" },
          "url": { "1": "https://example.com/releases/v2.0.0/MyMod_v2.0.0.7z" },
          "size": { "1": 4800000 },
          "hash": { "1": "sha256:fedcba0987654321..." }
        }
      ]
    }
  ]
}
```

> Each file group has a `display_name` and `category` at the group level. The `versions` array inside each group contains version-specific data. This creates a file card with a version dropdown for each group.

**Translation files example:**
```json
{
  "files": [
    {
      "display_name": "Translation",
      "versions": [
        {
          "version": "1.0.0",
          "compatibility": [
            { "version": "2.0.0", "build": "2000" }
          ],
          "expected_files": { "1": "MyTranslation_v1.0.0.7z" },
          "url": { "1": "https://example.com/releases/v1.0.0/MyTranslation_v1.0.0.7z" },
          "size": { "1": 1048576 },
          "hash": { "1": "sha256:abc123..." }
        }
      ]
    }
  ]
}
```

#### File Group Fields

| Field | Type | Description |
|---|---|---|
| `display_name` | string | Display name for the file card. When omitted, the archive filename from the first version's `expected_files` is used |
| `category` | string | File category: `"MAIN"` (default) or `"OPTIONAL"`. Mods only |

#### Version Fields

| Field | Type | Description |
|---|---|---|
| `version` | string | Version number (e.g. `"2.1.0"`) |
| `compatibility` | array | List of compatible versions of the target mod (or game versions if `for_mod_name` is `"Original_game"`). Translations only |
| `description` | string | Version/file description (optional) |
| `expected_files` | object | Expected filenames, dict format: `{"1": "file.7z", "2": "part2.7z"}` |
| `url` | object | Download URLs, dict format: `{"1": "https://..."}`. Keys match `expected_files` |
| `size` | object | File sizes in **bytes**, dict format: `{"1": 5242880}`. Example: `5242880` = 5 MB |
| `hash` | object | File hashes, dict format: `{"1": "sha256:..."}` (optional, for verification) |

> All file-related fields (`expected_files`, `url`, `size`, `hash`) use a numbered dictionary format where keys (`"1"`, `"2"`, ...) correspond to file parts. For single-file downloads, use key `"1"`.

---

#### requirements.json — optional

Mod dependencies on other mods.

```json
{
  "requirements": [
    {
      "name": "YetAnotherWeaponCompleteEdition",
      "folder": "YetAnotherWeaponCompleteEdition",
      "required": true,
      "description": "Mandatory dependency"
    },
    {
      "name": "MW5 Compatibility Framework",
      "folder": "MW5Compatibility",
      "required": false,
      "description": "Recommended for full compatibility"
    }
  ]
}
```

| Field | Type | Description |
|---|---|---|
| `name` | string | Display name of the dependency |
| `folder` | string | Folder name of the dependency mod (for searching installed mods) |
| `required` | bool | `true` — mandatory, `false` — recommended |
| `description` | string | Description of the dependency |

---

#### changelog.json — optional

Mod change history.

```json
{
  "changelog": [
    {
      "version": "2.1.0",
      "changes": [
        "Added HAG 20",
        "Fixed Gauss Rifle balance",
        "Compatibility with patch 1.1.380"
      ]
    }
  ]
}
```

---

### Translation Compatibility (for_mod_name)

Translations can specify which mod (or the game itself) they are made for, and which versions they are compatible with.

In `mod.json` of a translation, use the `for_mod_name` field:
- Set it to the **folder name** of the target mod — compatibility will be checked against the installed mod version.
- Set it to `"Original_game"` — compatibility will be checked against the **game version** from the program settings.

The `compatibility` array in each version entry lists version/build pairs the translation supports.

#### Example: Translation for the base game

**mod.json:**
```json
{
  "for_mod_name": "Original_game",
  "name": "Game Translation RUS",
  "author": "Translator"
}
```

**files.json:**
```json
{
  "files": [
    {
      "display_name": "Game Translation RUS",
      "versions": [
        {
          "version": "1.1.383",
          "compatibility": [
            { "version": "1.1.383", "build": "" },
            { "version": "1.1.380", "build": "" }
          ],
          "expected_files": { "1": "translation_v1.1.383.7z" },
          "url": { "1": "https://example.com/releases/translation_v1.1.383.7z" },
          "size": { "1": 102400 },
          "hash": { "1": "sha256:abc123..." }
        }
      ]
    }
  ]
}
```

When `for_mod_name` is `"Original_game"`:
- The `build` field inside `compatibility` entries can be left **empty** (`""`) since the game version in settings usually does not include a build number.
- The program maps `"Original_game"` → `"Game"` internally and uses the existing game version check (`is_game_version_requirement()`).
- The game version is taken from **Settings → Game version** (user-configured).

#### Example: Translation for a specific mod

**mod.json:**
```json
{
  "for_mod_name": "YetAnotherWeaponCompleteEdition",
  "name": "YAWCE / Translation RUS",
  "author": "Translator"
}
```

**files.json:**
```json
{
  "files": [
    {
      "display_name": "YAWCE / Translation RUS",
      "versions": [
        {
          "version": "3.0.0",
          "compatibility": [
            { "version": "3.0.0", "build": "300" },
            { "version": "2.9.0", "build": "290" }
          ],
          "expected_files": { "1": "YAWCE_RUS_v3.0.0.7z" },
          "url": { "1": "https://example.com/releases/YAWCE_RUS_v3.0.0.7z" },
          "size": { "1": 204800 },
          "hash": { "1": "sha256:def456..." }
        }
      ]
    }
  ]
}
```

In this case, the program checks against the installed mod's version and build number from `compatibility` entries.

#### How it works internally

When a translation is installed from the catalog:
1. `for_mod_name` is read from the repository `mod.json`.
2. `"Original_game"` is converted to `"Game"` and stored in `translation_requirements_mod_name` in `mod_manager_properties.json`.
3. The `compatibility` array is converted to a semicolon-separated string `"version|build;version|build"` and stored in `translation_requirements_mod_version_build`.
4. On the Installed/Files pages, the program checks compatibility — for `"Game"`, it compares against `config.game_version`; for regular mods, it searches installed mods by `file_name`.

> If `mod_manager_properties.json` inside the archive already contains `translation_requirements_*` fields, the archive values take priority and are not overwritten by repository data.

---

### featured.json — Featured Mods

The `featured.json` file in a category folder defines the list of featured mods. They are displayed first in the catalog and specially marked.

```json
["MyBestMod", "AnotherGreatMod", "EssentialTool"]
```

Values in the array are **folder names** of mods (for `repository`) or **folder names** (not IDs) for `nexus_api`.

> The order in `featured.json` defines the display order in the catalog. Other mods appear after featured ones in arbitrary order.

---

### mod_manager_properties.json

This file is created by the program in each installed mod's folder. It stores metadata linking the mod to its source (Nexusmods, repository, or manual install).

**This file is managed automatically** — it is created and updated when installing mods from the catalog, creating links, or updating mods. Mod authors can also include it in their archives to pre-configure links.

> **Note for users:** If a mod author includes `mod_manager_properties.json` in the archive, you need to enable the **"Copy mod_manager_properties.json"** checkbox on the download archives step during installation. Alternatively, you can enable this checkbox by default in **Settings** so it is always pre-checked.

#### Example

```json
{
  "file_name": "My Awesome Mod",
  "installed_version": "2.1.0",
  "is_files_mod": false,
  "files_mod_move_to": "",
  "files_mod_backup_on_replace": true,
  "files_mod_files_moved": false,
  "files_mod_files_list": [],
  "is_nexusmods": true,
  "nexusmods_mod_id": 12345,
  "nexusmods_mod_name": "My Awesome Mod",
  "nexusmods_mod_url": "https://www.nexusmods.com/mechwarrior5mercenaries/mods/12345",
  "is_repo": false,
  "repo_url": "",
  "repo_mod_category": "",
  "repo_mod_name": "",
  "repo_file_display_name": "",
  "is_translation": false,
  "translation_requirements_mod_name": "",
  "translation_requirements_mod_version_build": ""
}
```

#### Fields

| Field | Type | Description |
|---|---|---|
| `file_name` | string | Mod file display name in the manager |
| `installed_version` | string | Currently installed version |
| `is_files_mod` | bool | `true` if this is a files mod (no `mod.json`, files placed directly) |
| `is_nexusmods` | bool | `true` if linked to a Nexusmods mod |
| `nexusmods_mod_id` | int | Nexusmods mod ID |
| `nexusmods_mod_name` | string | Mod name on Nexusmods |
| `nexusmods_mod_url` | string | Full URL to the mod page on Nexusmods |
| `is_repo` | bool | `true` if installed from a repository |
| `repo_url` | string | Repository URL |
| `repo_mod_category` | string | Repository category ID (e.g. `"1"`, `"2"`) |
| `repo_mod_name` | string | Mod folder name in the repository |
| `repo_file_display_name` | string | File group `display_name` from `files.json` (used for update matching) |
| `is_translation` | bool | `true` if this mod is a translation |
| `translation_requirements_mod_name` | string | Required mod name (`"Game"` = requires a specific game version) |
| `translation_requirements_mod_version_build` | string | Required version\|build pairs, semicolon-separated (e.g. `"1.2.0\|123;1.3.0\|456"`) |
| `files_mod_move_to` | string | Target path for files mod file placement |
| `files_mod_backup_on_replace` | bool | Whether to backup replaced files |
| `files_mod_files_moved` | bool | `true` if files have been moved from files mod folder |
| `files_mod_files_list` | array | List of files managed by this files mod |

---

### mod_manager_install_rules.json

This file can be **included by mod authors** inside their mod archive. When the user installs the mod, the program automatically imports the rules into the load order system and then **deletes this file** from the installed mod folder.

This allows mod authors to ship recommended load order rules with their mods.

#### Format

```json
{
  "rules": [
    {
      "mod_name": "My Translation Mod",
      "mod_folder": "MyTranslationMod",
      "rule_type": "after",
      "target_name": "Original Mod",
      "target_folder": "OriginalMod"
    },
    {
      "mod_name": "My Translation Mod",
      "mod_folder": "MyTranslationMod",
      "rule_type": "last"
    }
  ]
}
```

#### Rule Fields

| Field | Type | Required | Description |
|---|---|---|---|
| `mod_folder` | string | yes | The mod folder this rule applies to |
| `rule_type` | string | yes | Rule type: `after`, `before`, `first`, `last` |
| `target_folder` | string | for `after`/`before` | Target mod folder (not needed for `first`/`last`) |
| `mod_name` | string | no | Display name of the mod (informational, not used by program) |
| `target_name` | string | no | Display name of the target mod (informational, not used by program) |
| `enabled` | bool | no | Ignored on import — all rules are always imported as **disabled** |

#### Rule Types

| Type | Description |
|---|---|
| `after` | The mod loads **after** the target mod (higher load order number) |
| `before` | The mod loads **before** the target mod (lower load order number) |
| `first` | The mod is placed in the **first** load group (lowest priority) |
| `last` | The mod is placed in the **last** load group (highest priority) |

#### How It Works

1. Mod author places `mod_manager_install_rules.json` in the mod archive root (next to `mod.json`)
2. User installs the mod through the program
3. The program reads the rules file and merges rules into the global `mod_manager_rules.json`
4. All imported rules are added as **disabled** (the user must enable them manually)
5. Duplicate rules (matching `mod_folder` + `rule_type` + `target_folder`) are skipped
6. The `mod_manager_install_rules.json` file is **deleted** from the installed folder after processing

> **Note for users:** If a mod author includes `mod_manager_install_rules.json` in the archive, you need to enable the **"Copy mod_manager_install_rules.json"** checkbox on the download archives step during installation. Alternatively, you can enable this checkbox by default in **Settings** so it is always pre-checked.

---

### Game mod.json (MW5 Format)

This file is the standard MechWarrior 5 mod descriptor. It is **created by the mod author** and included in the mod archive. The program reads it to get the mod's display name, version, and load order. When the user changes load order through the program, the `defaultLoadOrder` field is updated.

**Location:** `<mods_folder>/<ModName>/mod.json`

> **Important:** Do not confuse with the repository `mod.json` (described above). The game `mod.json` has a completely different format with `displayName`, `buildNumber`, etc.

#### Example

```json
{
  "displayName": "My Awesome Mod",
  "version": "2.1.0",
  "buildNumber": 210,
  "description": "A great mod for MW5",
  "author": "ModAuthor",
  "authorURL": "https://github.com/modauthor",
  "defaultLoadOrder": 5,
  "gameVersion": "1.1.383",
  "manifest": [],
  "steamPublishedFileId": 0,
  "steamLastSubmittedBuildNumber": 0,
  "steamModVisibility": "Public"
}
```

#### Fields

| Field | Type | Default | Description |
|---|---|---|---|
| `displayName` | string | `"Unknown Mod"` | Display name of the mod (shown in game and manager) |
| `version` | string | `"1.0.0"` | Mod version |
| `buildNumber` | int | `0` | Build number |
| `description` | string | `""` | Mod description |
| `author` | string | `""` | Author name |
| `authorURL` | string | `""` | Author's URL |
| `defaultLoadOrder` | int | `0` | Load order priority — managed by the program when user rearranges mods |
| `gameVersion` | string | `""` | Target game version |
| `manifest` | array | `[]` | List of mod file paths |
| `steamPublishedFileId` | int | `0` | Steam Workshop file ID |
| `steamLastSubmittedBuildNumber` | int | `0` | Last submitted build number to Steam |
| `steamModVisibility` | string | `"Public"` | Steam Workshop visibility |

> **Note:** The `defaultLoadOrder` field is the primary mechanism the game uses for mod load order. The program modifies this field when the user rearranges mods on the Mods page.

---

### backup.json

An automatic **copy of the original game `mod.json`**, created the first time the program modifies the mod's load order. This preserves the original `defaultLoadOrder` value so it can be restored later.

**Location:** `<mods_folder>/<ModName>/backup.json`

The format is identical to the game `mod.json` described above. The file is created once and never updated afterwards.

---

### modlist.json

Stores the enabled/disabled state of all mods. This is the file the game reads to determine which mods are active.

**Location:** `<mods_folder>/modlist.json`

#### Example

```json
{
  "gameVersion": "1.1.383",
  "modStatus": {
    "MyMod": {
      "bEnabled": true
    },
    "AnotherMod": {
      "bEnabled": false
    },
    "DisabledMod": {
      "bEnabled": false
    }
  }
}
```

#### Fields

| Field | Type | Description |
|---|---|---|
| `gameVersion` | string | Game version string |
| `modStatus` | object | Map of mod folder names to their status |
| `modStatus.<folder>.bEnabled` | bool | `true` — mod is enabled, `false` — disabled |

> **Note:** If a mod folder is not listed in `modStatus`, the mod is considered **enabled** by default.

---

### mod_manager_rules.json

Stores load order rules configured by the user through the program's Rules page. This file is placed in the mods folder.

**Location:** `<mods_folder>/mod_manager_rules.json`

#### Example

```json
{
  "rules_enabled": true,
  "rules": [
    {
      "mod_folder": "TranslationMod",
      "rule_type": "after",
      "target_folder": "OriginalMod",
      "enabled": true
    },
    {
      "mod_folder": "CoreFramework",
      "rule_type": "first",
      "target_folder": "",
      "enabled": true
    },
    {
      "mod_folder": "VisualOverhaul",
      "rule_type": "last",
      "target_folder": "",
      "enabled": false
    },
    {
      "mod_folder": "WeaponMod",
      "rule_type": "before",
      "target_folder": "BalanceMod",
      "enabled": true
    }
  ]
}
```

#### Top-Level Fields

| Field | Type | Default | Description |
|---|---|---|---|
| `rules_enabled` | bool | `true` | Global toggle for the rules system. When `false`, all rules are ignored |
| `rules` | array | `[]` | Array of load order rules |

#### Rule Fields

| Field | Type | Description |
|---|---|---|
| `mod_folder` | string | Folder name of the mod this rule applies to |
| `rule_type` | string | Rule type: `after`, `before`, `first`, `last` |
| `target_folder` | string | Target mod folder (for `after`/`before`; empty for `first`/`last`) |
| `enabled` | bool | Whether this individual rule is active |

#### Rule Types

| Type | Description |
|---|---|
| `after` | The mod loads **after** the target mod (higher load order number) |
| `before` | The mod loads **before** the target mod (lower load order number) |
| `first` | The mod is placed in the **first** load group (lowest priority) |
| `last` | The mod is placed in the **last** load group (highest priority) |

---

### Download State Files

Temporary files that track download progress for resumable downloads. Created when downloading mod archives and deleted after successful completion.

**Location:** `<archives_folder>/<filename>.download_state.json`

#### Example

```json
{
  "url": "https://example.com/releases/MyMod_v2.0.7z",
  "filename": "MyMod_v2.0.7z",
  "total_bytes": 5242880,
  "downloaded_bytes": 2621440,
  "expected_md5": "d41d8cd98f00b204e9800998ecf8427e"
}
```

#### Fields

| Field | Type | Description |
|---|---|---|
| `url` | string | Download URL |
| `filename` | string | Target filename |
| `total_bytes` | int | Total file size in bytes |
| `downloaded_bytes` | int | Bytes downloaded so far |
| `expected_md5` | string/null | Expected MD5 hash for verification (may be `null`) |

> These files are automatically deleted after a successful download. If a download is interrupted, the state file allows the program to resume from where it left off.

---

### config.json

Main application configuration file. Stores all user settings, window state, and repository list.

**Location:** `config/config.json`

#### Example

```json
{
  "game_folder": "D:/Games/Steam/steamapps/common/MechWarrior 5 Mercenaries",
  "mods_folder": "D:/Games/Steam/steamapps/common/MechWarrior 5 Mercenaries/MW5Mercs/Mods",
  "steam_mods_folder": "D:/Games/Steam/steamapps/workshop/content/784080",
  "game_version": "1.1.383",
  "language": "en",
  "check_nexusmods_updates": true,
  "check_repo_updates": true,
  "close_on_launch": false,
  "copy_mod_rules": false,
  "copy_mod_properties": false,
  "archives_folder": "data/downloads",
  "card_styles": {},
  "panel_position_mods": "right",
  "panel_position_catalog": "right",
  "conflict_display": "conflicts_tab",
  "repositories": [
    {
      "name": "Community Repository",
      "url": "https://raw.githubusercontent.com/user/mw5-repo/main",
      "enabled": true
    }
  ],
  "window_width": 1280,
  "window_height": 720,
  "window_x": 100,
  "window_y": 100,
  "window_maximized": false,
  "first_run": false
}
```

#### Fields

| Field | Type | Default | Description |
|---|---|---|---|
| `game_folder` | string | `""` | Path to the game installation folder |
| `mods_folder` | string | `""` | Path to the mods folder (usually `<game_folder>/MW5Mercs/Mods`) |
| `steam_mods_folder` | string | `""` | Path to Steam Workshop mods folder (optional) |
| `game_version` | string | `""` | Game version (entered manually by the user) |
| `language` | string | `"en"` | Interface language code (`"en"`, `"ru"`, `"uk"`) |
| `check_nexusmods_updates` | bool | `true` | Check for Nexusmods updates on startup |
| `check_repo_updates` | bool | `true` | Check for repository updates on startup |
| `close_on_launch` | bool | `false` | Close the application when launching the game |
| `copy_mod_rules` | bool | `false` | Default state of "Copy mod rules" checkbox on download page |
| `copy_mod_properties` | bool | `false` | Default state of "Copy mod properties" checkbox on download page |
| `archives_folder` | string | `"data/downloads"` | Folder for downloaded archives |
| `card_styles` | object | `{}` | Custom card color overrides |
| `panel_position_mods` | string | `"right"` | Info panel position on the Mods page (`"left"` or `"right"`) |
| `panel_position_catalog` | string | `"right"` | Info panel position on the Catalog page (`"left"` or `"right"`) |
| `conflict_display` | string | `"conflicts_tab"` | Conflict display mode: `"always"` or `"conflicts_tab"` |
| `repositories` | array | `[]` | List of configured repositories (see below) |
| `window_width` | int | `1280` | Window width in pixels |
| `window_height` | int | `720` | Window height in pixels |
| `window_x` | int | `100` | Window X position |
| `window_y` | int | `100` | Window Y position |
| `window_maximized` | bool | `false` | Whether the window is maximized |
| `first_run` | bool | `true` | First run flag (triggers the setup wizard) |

#### Repository Entry Fields

| Field | Type | Default | Description |
|---|---|---|---|
| `name` | string | `""` | Display name of the repository |
| `url` | string | `""` | URL or local path to the repository root |
| `enabled` | bool | `true` | Whether the repository is active |

---

### Modpacks

Modpacks save a snapshot of the user's mod configuration for sharing or restoring.

**Location:** `config/modpacks/<name>.json`

#### Example

```json
{
  "name": "My Battle Setup",
  "mods": [
    {
      "folder_name": "WeaponPack",
      "display_name": "Yet Another Weapon",
      "version": "26.0",
      "author": "Author",
      "is_installed": true,
      "is_translation": false,
      "source_type": "nexusmods",
      "nexusmods_mod_id": 1080,
      "nexusmods_mod_name": "Yet Another Weapon",
      "installed_version": "26.0",
      "is_nexusmods_linked": true,
      "is_repo_linked": false
    }
  ],
  "mods_preset": ["1"],
  "rules_preset": ["2"],
  "repositories": ["https://raw.githubusercontent.com/user/mw5-repo/main"],
  "mods_preset_data": {},
  "rules_preset_data": {}
}
```

#### Fields

| Field | Type | Description |
|---|---|---|
| `name` | string | Modpack display name |
| `mods` | array | List of mod entries with metadata |
| `mods_preset` | array | Names of linked mods presets |
| `rules_preset` | array | Names of linked rules presets |
| `repositories` | array | URLs of repositories used by this modpack |
| `mods_preset_data` | object | Embedded mods preset data (for sharing) |
| `rules_preset_data` | object | Embedded rules preset data (for sharing) |

#### Mod Entry Fields

| Field | Type | Description |
|---|---|---|
| `folder_name` | string | Mod folder name |
| `display_name` | string | Mod display name |
| `version` | string | Mod version |
| `author` | string | Mod author |
| `is_installed` | bool | Whether the mod was installed at the time of modpack creation |
| `is_translation` | bool | Whether the mod is a translation |
| `source_type` | string | Source type (e.g. `"nexusmods"`, `"repository"`) |
| `nexusmods_mod_id` | int | Nexusmods mod ID (if linked) |
| `nexusmods_mod_name` | string | Mod name on Nexusmods (if linked) |
| `installed_version` | string | Installed version at the time of creation |
| `is_nexusmods_linked` | bool | Whether the mod is linked to Nexusmods |
| `is_repo_linked` | bool | Whether the mod is linked to a repository |

---

### Presets

Presets save and restore mod order and rules configurations independently.

#### Mods Presets

**Location:** `config/presets/mods/<name>.json`

Saves the enabled state and load order of all mods.

```json
{
  "MyPreset": {
    "mods": {
      "CoreFramework": {
        "bEnabled": true,
        "defaultLoadOrder": 1
      },
      "WeaponPack": {
        "bEnabled": true,
        "defaultLoadOrder": 2
      },
      "VisualMod": {
        "bEnabled": false,
        "defaultLoadOrder": 3
      }
    }
  }
}
```

| Field | Type | Description |
|---|---|---|
| `<preset_name>.mods` | object | Map of mod folder names to their state |
| `<preset_name>.mods.<folder>.bEnabled` | bool | Whether the mod is enabled |
| `<preset_name>.mods.<folder>.defaultLoadOrder` | int | Load order position |

#### Rules Presets

**Location:** `config/presets/rules/<name>.json`

Saves the complete rules configuration.

```json
{
  "MyRulesPreset": {
    "rules_enabled": true,
    "rules": [
      {
        "mod_folder": "TranslationMod",
        "rule_type": "after",
        "target_folder": "OriginalMod",
        "enabled": true
      },
      {
        "mod_folder": "CoreFramework",
        "rule_type": "first",
        "enabled": true
      }
    ]
  }
}
```

| Field | Type | Description |
|---|---|---|
| `<preset_name>.rules_enabled` | bool | Global rules system toggle |
| `<preset_name>.rules` | array | Array of rules (same format as `mod_manager_rules.json`) |

> **Note:** The `target_folder` field is only included for `after`/`before` rules.

---

### mod_manager_backup.json

Full application backup file for export/import of all settings, presets, and rules.

**Location:** User-selected path (default filename: `mod_manager_backup.json`)

#### Example

```json
{
  "config": {
    "game_folder": "D:/Games/...",
    "language": "en",
    "repositories": [
      { "name": "My Repo", "url": "https://...", "enabled": true }
    ]
  },
  "presets_mods": {
    "1.json": { "1": { "mods": { "ModA": { "bEnabled": true, "defaultLoadOrder": 1 } } } }
  },
  "presets_rules": {
    "1.json": { "1": { "rules_enabled": true, "rules": [] } }
  }
}
```

#### Fields

| Field | Type | Description |
|---|---|---|
| `config` | object | Complete contents of `config.json` |
| `presets_mods` | object | All mods presets (key = filename including `.json`) |
| `presets_rules` | object | All rules presets (key = filename including `.json`) |

> This file is created via **Settings → Export Backup** and restored via **Settings → Import Backup**. Importing overwrites the current configuration and all presets.

---

### Multi-File Download Example

When a mod archive is split into multiple files (e.g. due to size limits), use numbered keys in `expected_files`, `url`, `size`, and `hash`:

```json
{
  "files": [
    {
      "display_name": "Full Mod (Multi-Part)",
      "category": "MAIN",
      "versions": [
        {
          "version": "2.2",
          "description": "Full mod (3 parts)",
          "expected_files": {
            "1": "MyMod_Part1.7z",
            "2": "MyMod_Part2.7z",
            "3": "MyMod_Part3.7z"
          },
          "url": {
            "1": "https://example.com/releases/MyMod_Part1.7z",
            "2": "https://example.com/releases/MyMod_Part2.7z",
            "3": "https://example.com/releases/MyMod_Part3.7z"
          },
          "size": {
            "1": 1048576000,
            "2": 729978606,
            "3": 524288000
          },
          "hash": {
            "1": "sha256:aaa111...",
            "2": "sha256:bbb222...",
            "3": "sha256:ccc333..."
          }
        }
      ]
    }
  ]
}
```

The program downloads all parts in sequence, verifying each file hash if provided. All parts are then extracted to the mod folder.

---

### Full Repository Example

```
my-mw5-repo/
├── repository.json
├── early_access_mods/
│   ├── featured.json
│   ├── WeaponPack/
│   │   ├── mod.json
│   │   ├── description.md
│   │   ├── files.json
│   │   ├── requirements.json
│   │   ├── changelog.json
│   │   └── preview.png
│   └── BalanceMod/
│       ├── mod.json
│       └── files.json
├── early_access_translations/
│   ├── featured.json
│   └── RussianTranslation/
│       ├── mod.json
│       └── description.md
├── nexusmods_mods/
│   ├── featured.json
│   └── 12345/
│       └── nexusmods_id.json
└── nexusmods_translations/
    ├── featured.json
    └── 67890/
        └── nexusmods_id.json
```

---

### Publishing a Repository

#### GitHub / GitLab / Codeberg / Bitbucket / Gitea / Forgejo

Place the repository folder in a public git repository. The program accesses raw files directly.

The program **automatically converts** web URLs to raw file URLs for the following platforms:

| Platform | User enters | Program converts to |
|---|---|---|
| GitHub | `https://github.com/user/repo` | `https://raw.githubusercontent.com/user/repo/main` |
| GitLab | `https://gitlab.com/user/repo` | `https://gitlab.com/user/repo/-/raw/main` |
| Codeberg | `https://codeberg.org/user/repo` | `https://codeberg.org/user/repo/raw/branch/main` |
| Bitbucket | `https://bitbucket.org/user/repo` | `https://bitbucket.org/user/repo/raw/main` |
| Gitea (self-hosted) | `https://gitea.example.com/user/repo/src/branch/main` | `https://gitea.example.com/user/repo/raw/branch/main` |

> **Note:** If the `main` branch is not found, the program will also try `master`. You can also specify a branch explicitly, e.g. `https://github.com/user/repo/tree/dev`.

> **Self-hosted Gitea/Forgejo:** The program cannot auto-detect custom domains. Use URLs containing `/src/branch/...` for auto-conversion, or provide the raw URL directly: `https://gitea.example.com/user/repo/raw/branch/main`.

**Example URL for Forgejo:**
```
http://192.168.3.10:7205/username/mw5-repo/raw/branch/main
```

#### Static HTTP Server

Any server that serves files via direct URLs. Nginx, Apache, Caddy, GitHub Pages, etc.

#### Local Path (for testing)

```
D:\MyMods\TestRepository
```
or
```
/home/user/mw5-repo
```

---

### Notes for Repository Developers

1. **Mod folder names** must not change after publication — users will lose the link with installed mods.
2. **File links** in `url` must be direct (no redirects or authorization). GitHub Releases provides direct raw links.
3. **Encoding** of all JSON and Markdown files — UTF-8.
4. **`is_translation`** is important: translations are displayed separately from main mods in the interface.
5. The `name` field of a category can be any string — the program uses it as an internal identifier and follows the path specified in `path` (or falls back to `name` as the path).
6. Versions in each file group's `versions` array can be listed in **any order** — the program automatically determines the latest version by comparing version strings using semantic versioning.

---

## Tools

### repo_file_info.py — File Size & Hash Generator

A helper script located in the `tools/` folder that generates file sizes and SHA-256 hashes for repository archives. The output can be used to fill in `size` and `hash` fields in `files.json` / `mod.json`.

The tool has two modes:
- **Interactive** — run without arguments (or via `repo_file_info.bat`). The script guides you through folder selection, scan mode, and output format step by step, then saves the result to a file.
- **CLI** — pass a path and flags as command-line arguments.

#### Quick Start (Windows)

Double-click `tools/repo_file_info.bat` — the interactive wizard will start.

#### Interactive Mode Steps

1. **Select folder** — via file explorer dialog or manual path input
2. **Scan mode** — all files or archives only (`.7z`, `.zip`, `.rar`, ...)
3. **Recursive** — scan subdirectories or not
4. **Output format** — plain text table, JSON single-file, or JSON multi-file
5. **URL prefix** — optional prefix for download links (JSON only)
6. **Result** — displayed in the console and saved to a file next to the scanned folder

#### CLI Usage

```bash
python tools/repo_file_info.py <path> [options]
```

#### CLI Options

| Flag | Description |
|---|---|
| `--json` | Output as JSON snippet ready for `files.json` |
| `--multi` | Multi-file mode: group all files into one version entry with numbered keys (`url_2`, `size_2`, etc.) |
| `--recursive`, `-r` | Recursively scan subdirectories |
| `--archives-only`, `-a` | Only include archive files (`.7z`, `.zip`, `.rar`, etc.) |
| `--url-prefix <url>` | URL prefix for download links in JSON output |
| `--save`, `-s` | Save results to a file next to the scanned folder |

#### CLI Examples

```bash
# Scan a single archive
python tools/repo_file_info.py "D:/releases/MyMod_v2.0.7z"

# Scan a folder and output JSON
python tools/repo_file_info.py "D:/releases/" --json

# Scan all subfolders recursively, archives only, with URL prefix, save to file
python tools/repo_file_info.py "D:/releases/" --recursive --archives-only --json \
  --url-prefix "https://github.com/user/repo/releases/download/v1.0/" --save

# Multi-file mode (multiple archives per version entry)
python tools/repo_file_info.py "D:/releases/" --json --multi
```

---

---

# Русский

## Содержание

- [Для пользователей](#для-пользователей)
  - [Установка](#установка)
  - [Первый запуск](#первый-запуск)
  - [Интерфейс](#интерфейс)
  - [Управление модами](#управление-модами)
  - [Порядок загрузки](#порядок-загрузки)
  - [Правила порядка загрузки](#правила-порядка-загрузки)
  - [Пресеты](#пресеты)
  - [Модпаки](#модпаки)
  - [Каталог — Nexusmods](#каталог--nexusmods)
  - [Сторонние репозитории](#сторонние-репозитории)
  - [Установка мода из архива](#установка-мода-из-архива)
  - [Многопапочные архивы](#многопапочные-архивы)
  - [Настройки](#настройки-1)
- [Для мододелов и владельцев репозиториев](#для-мододелов-и-владельцев-репозиториев)
  - [Обзор системы репозиториев](#обзор-системы-репозиториев)
  - [Структура репозитория](#структура-репозитория)
  - [repository.json](#repositoryjson-1)
  - [Категории репозитория](#категории-репозитория)
  - [Тип repository — структура мода](#тип-repository--структура-мода)
  - [Тип nexus_api — структура мода](#тип-nexus_api--структура-мода)
  - [Файлы метаданных мода](#файлы-метаданных-мода)
  - [Совместимость переводов (for_mod_name)](#совместимость-переводов-for_mod_name)
  - [featured.json — рекомендуемые моды](#featuredjson--рекомендуемые-моды)
  - [mod_manager_properties.json](#mod_manager_propertiesjson-1)
  - [mod_manager_install_rules.json](#mod_manager_install_rulesjson-1)
  - [Полный пример репозитория](#полный-пример-репозитория)
  - [Публикация репозитория](#публикация-репозитория)
  - [Замечания для разработчиков репозитория](#замечания-для-разработчиков-репозитория)
- [Инструменты](#инструменты)
  - [repo_file_info.py — генератор размеров и хешей файлов](#repo_file_infopy--генератор-размеров-и-хешей-файлов)

---

## Для пользователей

### Установка

#### Windows

1. Скачайте архив `MW5Mercs_Mod_Manager_vX.X.X_windows_x64.zip` со страницы релизов
2. Распакуйте в любую папку (например, `C:\Tools\MW5ModManager`)
3. Запустите `MW5Mercs Mod Manager.exe`

#### Linux

1. Скачайте архив `MW5Mercs_Mod_Manager_vX.X.X_linux_x64.zip`
2. Распакуйте: `unzip MW5Mercs_Mod_Manager_*.zip`
3. Дайте права на выполнение: `chmod +x "MW5Mercs Mod Manager"`
4. Запустите: `./"MW5Mercs Mod Manager"`

#### Системные требования

| | Windows | Linux |
|---|---|---|
| ОС | Windows 10/11 x64 | Ubuntu 20.04+, Fedora 36+, Arch и другие |
| Игра | MechWarrior 5: Mercenaries (Steam, Epic, GOG) | то же |
| .NET / Runtime | не требуется | не требуется |

---

### Первый запуск

При первом запуске откроется мастер настройки. Нужно указать:

**Папка игры** — корневая папка MechWarrior 5, например:
```
D:\Games\Steam\steamapps\common\MechWarrior 5 Mercenaries
```

**Папка Steam Workshop** (опционально) — папка с модами из Steam Workshop:
```
D:\Games\Steam\steamapps\workshop\content\784080
```

**Язык интерфейса** — English, Русский, Українська.

После этого программа автоматически найдёт папку модов `MW5Mercs/Mods` внутри папки игры.

---

### Интерфейс

Программа состоит из нескольких страниц, переключаемых через боковое меню:

| Страница | Метка | Описание |
|---|---|---|
| **Главная** | Главная | Список установленных модов, обзор обновлений, запуск игры |
| **Моды** | Моды | Детальный список всех модов с вкладками: ОБЗОР, КОНФЛИКТЫ, ПРАВИЛА, ПРЕСЕТЫ |
| **Файлы** | Файлы | Просмотр файловой системы папки модов |
| **Каталог** | Каталог | Поиск и установка модов из Nexusmods и репозиториев |
| **Параметры** | Параметры | Конфигурация программы |

На странице **Каталог** есть дополнительные вкладки:

| Вкладка | Метка | Описание |
|---|---|---|
| **Установка** | УСТАНОВКА | Установка мода из архива или папки |
| **Моды** | МОДЫ | Просмотр и установка модов из каталогов Nexusmods и репозиториев |
| **Переводы** | ПЕРЕВОДЫ | Просмотр и установка переводов |
| **Обновление** | ОБНОВЛЕНИЕ | Проверка и установка обновлений для связанных модов |
| **Связи** | СВЯЗИ | Управление связями между установленными модами и источниками (Nexusmods / репозиторий) |
| **Модпаки** | МОДПАКИ | Создание, управление и применение коллекций модов с пресетами |

---

### Управление модами

На странице **Моды** (вкладка ОБЗОР) отображается список всех найденных модов из:
- папки `MW5Mercs/Mods` внутри игры
- папки Steam Workshop (если задана)

Для каждого мода доступны действия:
- **Включить / выключить** — изменяет поле `defaultEnabled` в `mod.json` мода
- **Изменить порядок загрузки** — перетаскиванием или вводом числа
- **Открыть папку мода** — в Explorer / файловом менеджере
- **Удалить** — удаляет папку мода с диска

> **Внимание:** порядок загрузки задаётся полем `defaultLoadOrder` в `mod.json` каждого мода. Чем больше число — тем позже загружается мод. При конфликте побеждает мод с бо́льшим значением.

#### Конфликты

Программа автоматически обнаруживает конфликты — когда два или более модов изменяют одни и те же игровые файлы. Конфликты отображаются на вкладке КОНФЛИКТЫ на странице **Моды**.

---

### Порядок загрузки

MW5 загружает моды в порядке, определённом полем `defaultLoadOrder` в `mod.json`. Мод с бо́льшим числом перекрывает моды с меньшим числом при конфликте файлов.

В программе порядок изменяется:
- **Перетаскиванием** карточки мода
- **Вводом числа** напрямую в поле
- **Кнопками стрелок** — сдвинуть вверх/вниз

После изменения порядка программа обновляет файлы `mod.json` физически — изменения вступают в силу сразу при следующем запуске игры.

---

### Правила порядка загрузки

Правила — это ограничения, которые программа применяет автоматически при сортировке.

#### Типы правил

| Тип | Описание |
|---|---|
| **После мода** (`after`) | Данный мод должен загружаться после указанного мода |
| **Перед модом** (`before`) | Данный мод должен загружаться перед указанным модом |
| **В начало** (`first`) | Данный мод всегда должен быть в первой группе (низкие номера) |
| **В конец** (`last`) | Данный мод всегда должен быть в последней группе (высокие номера) |

#### Создание правила

1. Перейдите на страницу **Моды** → вкладка ПРАВИЛА
2. Нажмите **Добавить правило**
3. Выберите мод и тип правила
4. Для правил `after`/`before` — выберите второй мод
5. Нажмите **Сохранить**

Правила хранятся в файле `mod_manager_rules.json` в папке модов. При нажатии **Применить** программа пересортирует моды в соответствии со всеми активными правилами.

---

### Пресеты

Пресет — это сохранённая конфигурация: какие моды включены и в каком порядке загружаются.

#### Сохранение пресета

1. Перейдите на страницу **Моды** → вкладка ПРЕСЕТЫ
2. Нажмите **Пресет модов** → **Создать**
3. Введите имя пресета

#### Применение пресета

1. Выберите пресет из списка
2. Нажмите **Применить**

Пресеты хранятся в папке `config/presets/mods/` в формате JSON. Каждый файл — это один пресет:

```json
{
  "1": {
    "mods": {
      "ModFolderName": {
        "bEnabled": true,
        "defaultLoadOrder": 1
      },
      "AnotherMod": {
        "bEnabled": false,
        "defaultLoadOrder": 2
      }
    }
  }
}
```

---

### Модпаки

Модпак — это коллекция ссылок на моды, пресетов и URL-ов репозиториев, объединённых вместе. В отличие от пресетов (которые хранят только состояния включения/выключения модов и порядок загрузки), модпаки хранят полные метаданные модов, включая источники (Nexusmods, репозитории).

Модпаки **не содержат** файлов модов — только ссылки на них (имена папок, ID Nexusmods, URL репозиториев). При применении модпака программа добавляет неустановленные моды в очередь установки и восстанавливает включённые пресеты.

#### Создание модпака

1. Перейдите в **Каталог** → вкладка **МОДПАКИ** (правая панель)
2. Нажмите **Создить**
3. Каталог переключится на показ установленных связанных модов
4. Отметьте моды, которые хотите включить (можно также переключиться на Nexusmods или репозитории как источник)
5. Опционально выберите **Пресет модов** и/или **Пресет правил** из существующих
6. Привязанные репозитории добавляются автоматически из выбранных модов
7. Введите имя модпака
8. Нажмите **Создать модпак**

#### Применение модпака

1. Выберите модпак из списка
2. Нажмите **Применить** (✓)
3. Программа:
   - Проверяет, какие моды уже установлены
   - Добавляет неустановленные моды в очередь установки
   - Восстанавливает и применяет включённые пресеты (модов и правил)
   - Показывает итоговое сообщение

#### Предпросмотр модпака

Кликните на имя модпака (без нажатия «Применить») для предварительного просмотра содержимого:
- **Моды** — список включённых модов со статусом установки
- **Пресеты правил** — включённые пресеты правил
- **Пресеты модов** — включённые пресеты модов
- **Репозитории** — привязанные репозитории

#### Импорт / Экспорт

- **Импорт**: Нажмите **Импорт** → выберите `.json` файл модпака
- **Экспорт**: Выберите модпак → нажмите **Экспорт** → укажите место сохранения

Модпаки хранятся в `config/modpacks/` в формате JSON. Каждый файл содержит имя модпака, список модов с метаданными, данные пресетов и URL-ы репозиториев.

---

### Каталог — Nexusmods

На странице **Каталог** (вкладки МОДЫ и ПЕРЕВОДЫ) отображаются моды с сайта Nexusmods через GraphQL v2 API.

**Авторизация не требуется.** Программа обращается к каталогу Nexusmods, получает информацию о модах и генерирует ссылки на скачивание без необходимости аккаунта Nexusmods или API-ключа.

**Возможности:**
- Поиск модов по названию
- Просмотр описания, скриншотов, файлов мода
- Загрузка и установка мода напрямую из программы
- Проверка обновлений для связанных модов

---

### Сторонние репозитории

Репозитории — это отдельные каталоги модов, размещённые на любом HTTP/HTTPS сервере или локально. Это основная система для распространения модов, не размещённых на Nexusmods (например, ранний доступ, переводы).

#### Добавление репозитория

1. Перейдите в **Параметры** → вкладка ОБЩИЕ
2. Нажмите **Добавить** в разделе Репозитории
3. Введите URL репозитория или путь к локальной папке:
   - HTTP/HTTPS: `https://example.com/my-mw5-repo`
   - Локально: `D:\MyRepository` или `/home/user/mw5-repo`
4. Введите отображаемое имя
5. Нажмите **Сохранить**

После добавления программа загрузит `repository.json` и покажет доступные категории в каталоге.

---

### Установка мода из архива

Мод также можно установить из готового архива (`.7z`, `.zip`, `.rar`) или из папки.

1. Перейдите в **Каталог** → вкладка УСТАНОВКА
2. Выберите архив или папку с модом
3. Программа распакует архив в папку модов игры

Поддерживаемые форматы: `.7z`, `.zip`, `.rar`, `.tar`, `.gz`.
Для распаковки используется встроенный 7-Zip (поставляется вместе с программой).

---

### Многопапочные архивы

Если архив содержит несколько папок модов (каждая со своим `mod.json`), программа установит их все. Каждая папка устанавливается отдельно в директорию модов.

При создании связи с Nexusmods или репозиторием для такого мода, связь автоматически применяется ко всем родственным папкам из одного архива.

---

### Настройки

| Параметр | Описание |
|---|---|
| **Папка игры** | Путь к MW5 (обязательно) |
| **Папка Steam Workshop** | Путь к папке Workshop Steam (опционально) |
| **Версия игры** | Текстовое поле для указания версии (справочно) |
| **Язык** | Язык интерфейса: English, Русский, Українська |
| **Проверять обновления Nexusmods** | Проверять обновления при старте |
| **Проверять обновления репозиториев** | Проверять обновления репозиториев при старте |
| **Закрывать при запуске игры** | Автоматически закрыть менеджер при запуске MW5 |
| **Папка загрузок** | Куда сохраняются скачанные архивы |
| **Репозитории** | Список подключённых репозиториев |

---

---

## Для мододелов и владельцев репозиториев

### Обзор системы репозиториев

Репозиторий — это папка (локальная или на HTTP/HTTPS сервере), содержащая:
- `repository.json` — описание репозитория и его категорий
- Папки категорий с подпапками для каждого мода

Программа читает репозиторий при запуске и отображает моды в каталоге. При нажатии «Установить» — скачивает архив по ссылке из метаданных и устанавливает мод.

**Поддерживаемые способы хостинга:**
- Любой HTTP/HTTPS сервер с прямым доступом к файлам (GitHub Pages, Nginx, Apache, CDN)
- GitHub / GitLab / Codeberg / Bitbucket / Gitea / Forgejo репозиторий (автонормализация web-URL в raw)
- Локальная папка на диске (для тестирования)

---

### Структура репозитория

```
my-repository/
├── repository.json               # Обязательный — описание репозитория
│
├── early_access_mods/            # Папка категории (путь задаётся в repository.json)
│   ├── featured.json             # Опционально — список рекомендуемых модов
│   ├── MyMod/                    # Папка мода (имя папки = идентификатор)
│   │   ├── mod.json              # Обязательный — метаданные мода
│   │   ├── description.md        # Опционально — описание (Markdown)
│   │   ├── files.json            # Обязательный — список файлов с версиями и ссылками
│   │   ├── requirements.json     # Опционально — зависимости
│   │   ├── changelog.json        # Опционально — история изменений
│   │   └── preview.png           # Опционально — изображение превью
│   └── AnotherMod/
│       ├── mod.json
│       └── files.json
│
├── early_access_translations/    # Папка переводов
│   ├── featured.json
│   └── MyTranslation/
│       ├── mod.json
│       └── files.json
│
├── nexusmods_mods/               # Категория nexus_api (ссылки на Nexusmods)
│   ├── featured.json
│   └── 12345/                    # Имя папки = nexusmods ID мода
│       └── nexusmods_id.json
│
└── nexusmods_translations/       # Переводы из Nexusmods
    ├── featured.json
    └── 67890/
        └── nexusmods_id.json
```

---

### repository.json

Корневой файл описания репозитория. **Обязателен.**

```json
{
  "name": "My MW5 Repository",
  "categories": {
    "1": {
      "name": "early_access_mods",
      "type": "repository",
      "is_translation": false,
      "path": "early_access_mods",
      "display_name": "Моды раннего доступа",
      "mods": ["WeaponPack", "BalanceMod"]
    },
    "2": {
      "name": "early_access_translations",
      "type": "repository",
      "is_translation": true,
      "path": "early_access_translations",
      "display_name": "Переводы",
      "mods": ["RussianTranslation"]
    },
    "3": {
      "name": "nexusmods_mods",
      "type": "nexus_api",
      "is_translation": false,
      "path": "nexusmods_mods",
      "display_name": "Популярные моды с Nexusmods",
      "mods": ["12345"]
    },
    "4": {
      "name": "nexusmods_translations",
      "type": "nexus_api",
      "is_translation": true,
      "path": "nexusmods_translations",
      "display_name": "Переводы с Nexusmods",
      "mods": ["67890"]
    }
  }
}
```

#### Поля repository.json

| Поле | Тип | Обязательность | Описание |
|---|---|---|---|
| `name` | string | обязательно | Отображаемое имя репозитория |
| `categories` | object | обязательно | Объект категорий (ключ — произвольный идентификатор) |

#### Поля категории

| Поле | Тип | Обязательность | Описание |
|---|---|---|---|
| `name` | string | обязательно | Имя категории — любая строка. Используется как внутренний идентификатор. Также используется как путь к папке, если `path` не указан |
| `type` | string | обязательно | `repository` — полные метаданные в папке, `nexus_api` — только ID для запроса к Nexusmods API |
| `is_translation` | bool | обязательно | `true` если категория содержит переводы |
| `path` | string | обязательно | Относительный путь к папке категории от корня репозитория |
| `display_name` | string | опционально | Пользовательское имя для отображения в интерфейсе |
| `mods` | массив строк | обязательно для удалённых | Список имён папок модов. **Обязателен** для удалённых (HTTP) репозиториев — без него программа не сможет обнаружить моды. Для локальных репозиториев опционален (программа читает файловую систему). |

> **Важно:** ключи категорий (`"1"`, `"2"`, ...) — произвольные строки. Программа использует поле `name` внутри объекта как канонический идентификатор.

---

### Категории репозитория

#### Тип `repository`

Программа скачивает метаданные мода из папок с `mod.json`. Всё описание, версии, зависимости — в самом репозитории. Подходит для модов, распространяемых вне Nexusmods.

#### Тип `nexus_api`

Программа использует `nexusmods_id.json` из папки для получения ID мода, затем загружает полные данные через Nexusmods GraphQL API. Используется для отображения модов с Nexusmods в каталоге репозитория.

---

### Тип `repository` — структура мода

Каждый мод — это папка внутри папки категории.

```
CategoryFolder/
└── MyModFolderName/     ← имя папки = идентификатор мода в программе
    ├── mod.json          ← обязательно
    ├── files.json        ← обязательно
    ├── description.md    ← опционально
    ├── requirements.json ← опционально
    ├── changelog.json    ← опционально
    └── preview.png       ← опционально
```

> Имя папки мода используется как уникальный идентификатор — оно должно быть постоянным. Переименование папки потеряет связь с установленным модом для пользователей.

---

### Тип `nexus_api` — структура мода

```
nexusmods_mods/
└── 12345/                      ← имя папки = nexusmods ID (рекомендуется)
    └── nexusmods_id.json        ← обязательно
```

**nexusmods_id.json:**

```json
{
  "nexusmods_id": 12345
}
```

Программа использует это число для запроса к Nexusmods API и получения названия, описания, изображений и ссылок на файлы мода.

---

### Файлы метаданных мода

#### mod.json — обязательный

Основные метаданные мода в репозитории. **Не является** `mod.json` игры — это отдельный формат.
Версии хранятся отдельно в `files.json`.

**Пример для мода:**
```json
{
  "name": "My Awesome Mod",
  "author": "AuthorName",
  "mod_page": "https://github.com/author/my-awesome-mod",
  "images": {
    "preview": "preview.png"
  }
}
```

**Пример для перевода:**
```json
{
  "for_mod_name": "Target Mod Name",
  "name": "Target Mod Name / Translation RUS",
  "author": "AuthorName",
  "images": {
    "preview": "preview.png"
  }
}
```

| Поле | Тип | Обязательность | Описание |
|---|---|---|---|
| `name` | string | обязательно | Отображаемое имя мода |
| `author` | string | рекомендуется | Автор мода |
| `for_mod_name` | string | только для переводов | Имя целевого мода для переводов. Установите `"Original_game"` для проверки совместимости с версией игры из настроек |
| `mod_page` | string | опционально | URL страницы мода (GitHub, форум, etc.) |
| `images.preview` | string | опционально | Имя файла или URL изображения превью |

---

#### description.md — опциональный

Описание мода в формате Markdown или обычного текста. Если файл существует — программа использует его вместо поля `description` из `mod.json`.

---

#### files.json — обязательный

Содержит список файлов мода, сгруппированных по категориям, каждый со своими версиями, ссылками на скачивание, размерами и хешами.

**Пример для мода:**
```json
{
  "files": [
    {
      "display_name": "Main Files",
      "category": "MAIN",
      "versions": [
        {
          "version": "2.1.0",
          "description": "Основные файлы мода",
          "expected_files": { "1": "MyMod_v2.1.0.7z" },
          "url": { "1": "https://example.com/releases/v2.1.0/MyMod_v2.1.0.7z" },
          "size": { "1": 5242880 },
          "hash": { "1": "sha256:abcdef1234567890..." }
        },
        {
          "version": "2.0.0",
          "description": "Предыдущая стабильная версия",
          "expected_files": { "1": "MyMod_v2.0.0.7z" },
          "url": { "1": "https://example.com/releases/v2.0.0/MyMod_v2.0.0.7z" },
          "size": { "1": 4800000 },
          "hash": { "1": "sha256:fedcba0987654321..." }
        }
      ]
    }
  ]
}
```

> Каждая файловая группа имеет `display_name` и `category` на уровне группы. Массив `versions` внутри группы содержит данные, специфичные для каждой версии. Это создаёт карточку файла с выпадающим списком версий для каждой группы.

**Пример для перевода:**
```json
{
  "files": [
    {
      "display_name": "Translation",
      "versions": [
        {
          "version": "1.0.0",
          "compatibility": [
            { "version": "2.0.0", "build": "2000" }
          ],
          "expected_files": { "1": "MyTranslation_v1.0.0.7z" },
          "url": { "1": "https://example.com/releases/v1.0.0/MyTranslation_v1.0.0.7z" },
          "size": { "1": 1048576 },
          "hash": { "1": "sha256:abc123..." }
        }
      ]
    }
  ]
}
```

#### Поля файловой группы

| Поле | Тип | Описание |
|---|---|---|
| `display_name` | string | Отображаемое имя карточки файла. Если не указано, используется имя архива из `expected_files` первой версии |
| `category` | string | Категория файла: `"MAIN"` (по умолчанию) или `"OPTIONAL"`. Только для модов |

#### Поля версии

| Поле | Тип | Описание |
|---|---|---|
| `version` | string | Номер версии (например, `"2.1.0"`) |
| `compatibility` | array | Список совместимых версий целевого мода (или версий игры, если `for_mod_name` = `"Original_game"`). Только для переводов |
| `description` | string | Описание версии/файла (опционально) |
| `expected_files` | object | Ожидаемые имена файлов, формат словаря: `{"1": "file.7z", "2": "part2.7z"}` |
| `url` | object | Ссылки на скачивание, формат словаря: `{"1": "https://..."}`. Ключи соответствуют `expected_files` |
| `size` | object | Размеры файлов в **байтах**, формат словаря: `{"1": 5242880}`. Пример: `5242880` = 5 МБ |
| `hash` | object | Хеши файлов, формат словаря: `{"1": "sha256:..."}` (опционально, для проверки) |

> Все поля, связанные с файлами (`expected_files`, `url`, `size`, `hash`), используют нумерованный формат словаря, где ключи (`"1"`, `"2"`, ...) соответствуют частям файлов. Для загрузки одного файла используйте ключ `"1"`.

---

#### requirements.json — опциональный

Зависимости мода от других модов.

```json
{
  "requirements": [
    {
      "name": "YetAnotherWeaponCompleteEdition",
      "folder": "YetAnotherWeaponCompleteEdition",
      "required": true,
      "description": "Обязательная зависимость"
    },
    {
      "name": "MW5 Compatibility Framework",
      "folder": "MW5Compatibility",
      "required": false,
      "description": "Рекомендуется для полной совместимости"
    }
  ]
}
```

| Поле | Тип | Описание |
|---|---|---|
| `name` | string | Отображаемое имя зависимости |
| `folder` | string | Имя папки мода-зависимости (для поиска в установленных) |
| `required` | bool | `true` — обязательная, `false` — рекомендуется |
| `description` | string | Пояснение к зависимости |

---

#### changelog.json — опциональный

История изменений мода.

```json
{
  "changelog": [
    {
      "version": "2.1.0",
      "changes": [
        "Добавлен HAG 20",
        "Исправлен баланс Gauss Rifle",
        "Совместимость с патчем 1.1.380"
      ]
    }
  ]
}
```

---

### Совместимость переводов (for_mod_name)

Переводы могут указывать, для какого мода (или самой игры) они предназначены и с какими версиями совместимы.

В `mod.json` перевода используйте поле `for_mod_name`:
- Укажите **имя папки** целевого мода — совместимость будет проверяться по версии установленного мода.
- Укажите `"Original_game"` — совместимость будет проверяться по **версии игры** из настроек программы.

Массив `compatibility` в каждой записи версии содержит пары версия/сборка, с которыми перевод совместим.

#### Пример: перевод для базовой игры

**mod.json:**
```json
{
  "for_mod_name": "Original_game",
  "name": "Game Translation RUS",
  "author": "Translator"
}
```

**files.json:**
```json
{
  "files": [
    {
      "display_name": "Game Translation RUS",
      "versions": [
        {
          "version": "1.1.383",
          "compatibility": [
            { "version": "1.1.383", "build": "" },
            { "version": "1.1.380", "build": "" }
          ],
          "expected_files": { "1": "translation_v1.1.383.7z" },
          "url": { "1": "https://example.com/releases/translation_v1.1.383.7z" },
          "size": { "1": 102400 },
          "hash": { "1": "sha256:abc123..." }
        }
      ]
    }
  ]
}
```

Когда `for_mod_name` = `"Original_game"`:
- Поле `build` внутри записей `compatibility` можно оставить **пустым** (`""`), так как версия игры в настройках обычно не содержит номер сборки.
- Программа преобразует `"Original_game"` → `"Game"` и использует существующий механизм проверки версии игры (`is_game_version_requirement()`).
- Версия игры берётся из **Настройки → Версия игры** (настраивается пользователем).

#### Пример: перевод для конкретного мода

**mod.json:**
```json
{
  "for_mod_name": "YetAnotherWeaponCompleteEdition",
  "name": "YAWCE / Translation RUS",
  "author": "Translator"
}
```

**files.json:**
```json
{
  "files": [
    {
      "display_name": "YAWCE / Translation RUS",
      "versions": [
        {
          "version": "3.0.0",
          "compatibility": [
            { "version": "3.0.0", "build": "300" },
            { "version": "2.9.0", "build": "290" }
          ],
          "expected_files": { "1": "YAWCE_RUS_v3.0.0.7z" },
          "url": { "1": "https://example.com/releases/YAWCE_RUS_v3.0.0.7z" },
          "size": { "1": 204800 },
          "hash": { "1": "sha256:def456..." }
        }
      ]
    }
  ]
}
```

В этом случае программа проверяет совместимость по версии и номеру сборки установленного мода из записей `compatibility`.

#### Как это работает внутри

При установке перевода из каталога:
1. `for_mod_name` считывается из `mod.json` репозитория.
2. `"Original_game"` преобразуется в `"Game"` и записывается в `translation_requirements_mod_name` в `mod_manager_properties.json`.
3. Массив `compatibility` преобразуется в строку `"version|build;version|build"` с разделением точкой с запятой и записывается в `translation_requirements_mod_version_build`.
4. На страницах «Установленные»/«Файлы» программа проверяет совместимость — для `"Game"` сравнивает с `config.game_version`; для обычных модов ищет установленные моды по `file_name`.

> Если `mod_manager_properties.json` внутри архива уже содержит поля `translation_requirements_*`, значения из архива имеют приоритет и не перезаписываются данными из репозитория.

---

### featured.json — рекомендуемые моды

Файл `featured.json` в папке категории задаёт список рекомендуемых модов. Они отображаются первыми в каталоге и помечаются особым образом.

```json
["MyBestMod", "AnotherGreatMod", "EssentialTool"]
```

Значения в массиве — **имена папок** модов (для `repository`) или **имена папок** (не ID) для `nexus_api`.

> Порядок в `featured.json` — это порядок отображения в каталоге. Остальные моды идут после рекомендуемых в произвольном порядке.

---

### mod_manager_properties.json

Этот файл создаётся программой в папке каждого установленного мода. Он хранит метаданные, связывающие мод с его источником (Nexusmods, репозиторий или ручная установка).

**Файл управляется автоматически** — он создаётся и обновляется при установке модов из каталога, создании связей или обновлении модов. Авторы модов также могут включить его в свой архив для предварительной настройки связей.

> **Примечание для пользователей:** Если автор мода включает `mod_manager_properties.json` в архив, вам необходимо включить галочку **«Копировать mod_manager_properties.json»** на этапе скачивания архивов при установке. Либо можно включить эту галочку по умолчанию в **Настройках**, чтобы она всегда была активна.

#### Пример

```json
{
  "file_name": "My Awesome Mod",
  "installed_version": "2.1.0",
  "is_files_mod": false,
  "files_mod_move_to": "",
  "files_mod_backup_on_replace": true,
  "files_mod_files_moved": false,
  "files_mod_files_list": [],
  "is_nexusmods": true,
  "nexusmods_mod_id": 12345,
  "nexusmods_mod_name": "My Awesome Mod",
  "nexusmods_mod_url": "https://www.nexusmods.com/mechwarrior5mercenaries/mods/12345",
  "is_repo": false,
  "repo_url": "",
  "repo_mod_category": "",
  "repo_mod_name": "",
  "repo_file_display_name": "",
  "is_translation": false,
  "translation_requirements_mod_name": "",
  "translation_requirements_mod_version_build": ""
}
```

#### Поля

| Поле | Тип | Описание |
|---|---|---|
| `file_name` | string | Отображаемое имя мода в менеджере |
| `installed_version` | string | Текущая установленная версия |
| `is_files_mod` | bool | `true` если это файловый мод (без `mod.json`, файлы размещаются напрямую) |
| `is_nexusmods` | bool | `true` если связан с модом на Nexusmods |
| `nexusmods_mod_id` | int | ID мода на Nexusmods |
| `nexusmods_mod_name` | string | Имя мода на Nexusmods |
| `nexusmods_mod_url` | string | Полный URL страницы мода на Nexusmods |
| `is_repo` | bool | `true` если установлен из репозитория |
| `repo_url` | string | URL репозитория |
| `repo_mod_category` | string | ID категории в репозитории (например, `"1"`, `"2"`) |
| `repo_mod_name` | string | Имя папки мода в репозитории |
| `repo_file_display_name` | string | `display_name` файловой группы из `files.json` (используется для сопоставления при обновлении) |
| `is_translation` | bool | `true` если мод является переводом |
| `translation_requirements_mod_name` | string | Имя требуемого мода (`"Game"` = требуется определённая версия игры) |
| `translation_requirements_mod_version_build` | string | Пары версия\|билд через точку с запятой (например, `"1.2.0\|123;1.3.0\|456"`) |
| `files_mod_move_to` | string | Целевой путь для размещения файлов файлового мода |
| `files_mod_backup_on_replace` | bool | Создавать ли резервную копию заменяемых файлов |
| `files_mod_files_moved` | bool | `true` если файлы уже перемещены из папки файлового мода |
| `files_mod_files_list` | array | Список файлов, управляемых этим файловым модом |

---

### mod_manager_install_rules.json

Этот файл может быть **включён автором мода** в архив мода. При установке мода программа автоматически импортирует правила в систему порядка загрузки, а затем **удаляет этот файл** из папки установленного мода.

Это позволяет авторам модов поставлять рекомендуемые правила порядка загрузки вместе со своими модами.

#### Формат

```json
{
  "rules": [
    {
      "mod_name": "My Translation Mod",
      "mod_folder": "MyTranslationMod",
      "rule_type": "after",
      "target_name": "Original Mod",
      "target_folder": "OriginalMod"
    },
    {
      "mod_name": "My Translation Mod",
      "mod_folder": "MyTranslationMod",
      "rule_type": "last"
    }
  ]
}
```

#### Поля правила

| Поле | Тип | Обязательность | Описание |
|---|---|---|---|
| `mod_folder` | string | обязательно | Папка мода, к которому применяется правило |
| `rule_type` | string | обязательно | Тип правила: `after`, `before`, `first`, `last` |
| `target_folder` | string | для `after`/`before` | Целевая папка мода (не нужно для `first`/`last`) |
| `mod_name` | string | нет | Отображаемое имя мода (информационное, не используется программой) |
| `target_name` | string | нет | Отображаемое имя целевого мода (информационное, не используется программой) |
| `enabled` | bool | нет | Игнорируется при импорте — все правила всегда импортируются как **выключенные** |

#### Типы правил

| Тип | Описание |
|---|---|
| `after` | Мод загружается **после** целевого мода (больший номер порядка загрузки) |
| `before` | Мод загружается **перед** целевым модом (меньший номер порядка загрузки) |
| `first` | Мод помещается в **первую** группу загрузки (наименьший приоритет) |
| `last` | Мод помещается в **последнюю** группу загрузки (наивысший приоритет) |

#### Как это работает

1. Автор мода помещает `mod_manager_install_rules.json` в корень архива мода (рядом с `mod.json`)
2. Пользователь устанавливает мод через программу
3. Программа читает файл правил и добавляет правила в глобальный `mod_manager_rules.json`
4. Все импортированные правила добавляются как **выключенные** (пользователь должен включить их вручную)
5. Дубликаты правил (совпадение по `mod_folder` + `rule_type` + `target_folder`) пропускаются
6. Файл `mod_manager_install_rules.json` **удаляется** из папки установленного мода после обработки

> **Примечание для пользователей:** Если автор мода включает `mod_manager_install_rules.json` в архив, вам необходимо включить галочку **«Копировать mod_manager_install_rules.json»** на этапе скачивания архивов при установке. Либо можно включить эту галочку по умолчанию в **Настройках**, чтобы она всегда была активна.

---

### Игровой mod.json (формат MW5)

Этот файл — стандартный дескриптор мода MechWarrior 5. Он **создаётся автором мода** и включается в архив мода. Программа читает его для получения имени мода, версии и порядка загрузки. При изменении порядка загрузки через программу обновляется поле `defaultLoadOrder`.

**Расположение:** `<папка_модов>/<ИмяМода>/mod.json`

> **Важно:** Не путайте с `mod.json` репозитория (описан выше). Игровой `mod.json` имеет совершенно другой формат с полями `displayName`, `buildNumber` и т.д.

#### Пример

```json
{
  "displayName": "My Awesome Mod",
  "version": "2.1.0",
  "buildNumber": 210,
  "description": "A great mod for MW5",
  "author": "ModAuthor",
  "authorURL": "https://github.com/modauthor",
  "defaultLoadOrder": 5,
  "gameVersion": "1.1.383",
  "manifest": [],
  "steamPublishedFileId": 0,
  "steamLastSubmittedBuildNumber": 0,
  "steamModVisibility": "Public"
}
```

#### Поля

| Поле | Тип | По умолчанию | Описание |
|---|---|---|---|
| `displayName` | string | `"Unknown Mod"` | Отображаемое имя мода (в игре и менеджере) |
| `version` | string | `"1.0.0"` | Версия мода |
| `buildNumber` | int | `0` | Номер сборки |
| `description` | string | `""` | Описание мода |
| `author` | string | `""` | Имя автора |
| `authorURL` | string | `""` | URL автора |
| `defaultLoadOrder` | int | `0` | Приоритет порядка загрузки — управляется программой при перестановке модов |
| `gameVersion` | string | `""` | Целевая версия игры |
| `manifest` | array | `[]` | Список путей файлов мода |
| `steamPublishedFileId` | int | `0` | ID файла в Steam Workshop |
| `steamLastSubmittedBuildNumber` | int | `0` | Последний отправленный в Steam номер сборки |
| `steamModVisibility` | string | `"Public"` | Видимость в Steam Workshop |

> **Примечание:** Поле `defaultLoadOrder` — основной механизм, по которому игра определяет порядок загрузки модов. Программа изменяет это поле при перестановке модов на странице «Моды».

---

### backup.json

Автоматическая **копия оригинального игрового `mod.json`**, создаваемая при первом изменении порядка загрузки мода. Сохраняет исходное значение `defaultLoadOrder` для возможности восстановления.

**Расположение:** `<папка_модов>/<ИмяМода>/backup.json`

Формат идентичен игровому `mod.json`, описанному выше. Файл создаётся однократно и больше не обновляется.

---

### modlist.json

Хранит состояние включения/выключения всех модов. Этот файл читается игрой для определения активных модов.

**Расположение:** `<папка_модов>/modlist.json`

#### Пример

```json
{
  "gameVersion": "1.1.383",
  "modStatus": {
    "MyMod": {
      "bEnabled": true
    },
    "AnotherMod": {
      "bEnabled": false
    },
    "DisabledMod": {
      "bEnabled": false
    }
  }
}
```

#### Поля

| Поле | Тип | Описание |
|---|---|---|
| `gameVersion` | string | Строка версии игры |
| `modStatus` | object | Словарь имён папок модов и их статусов |
| `modStatus.<папка>.bEnabled` | bool | `true` — мод включён, `false` — выключен |

> **Примечание:** Если папка мода отсутствует в `modStatus`, мод считается **включённым** по умолчанию.

---

### mod_manager_rules.json

Хранит правила порядка загрузки, настроенные пользователем через страницу «Правила» в программе. Этот файл размещается в папке модов.

**Расположение:** `<папка_модов>/mod_manager_rules.json`

#### Пример

```json
{
  "rules_enabled": true,
  "rules": [
    {
      "mod_folder": "TranslationMod",
      "rule_type": "after",
      "target_folder": "OriginalMod",
      "enabled": true
    },
    {
      "mod_folder": "CoreFramework",
      "rule_type": "first",
      "target_folder": "",
      "enabled": true
    },
    {
      "mod_folder": "VisualOverhaul",
      "rule_type": "last",
      "target_folder": "",
      "enabled": false
    },
    {
      "mod_folder": "WeaponMod",
      "rule_type": "before",
      "target_folder": "BalanceMod",
      "enabled": true
    }
  ]
}
```

#### Поля верхнего уровня

| Поле | Тип | По умолчанию | Описание |
|---|---|---|---|
| `rules_enabled` | bool | `true` | Глобальный переключатель системы правил. Когда `false`, все правила игнорируются |
| `rules` | array | `[]` | Массив правил порядка загрузки |

#### Поля правила

| Поле | Тип | Описание |
|---|---|---|
| `mod_folder` | string | Имя папки мода, к которому применяется правило |
| `rule_type` | string | Тип правила (см. таблицу ниже) |
| `target_folder` | string | Целевая папка мода (для `after`/`before`; пусто для `first`/`last`) |
| `enabled` | bool | Активно ли данное правило |

#### Типы правил

| Тип | Описание |
|---|---|
| `after` | Мод загружается **после** целевого мода (больший номер порядка загрузки) |
| `before` | Мод загружается **перед** целевым модом (меньший номер порядка загрузки) |
| `first` | Мод помещается в **первую** группу загрузки (наименьший приоритет) |
| `last` | Мод помещается в **последнюю** группу загрузки (наивысший приоритет) |

---

### Файлы состояния загрузки

Временные файлы, отслеживающие прогресс загрузки для возобновляемых скачиваний. Создаются при загрузке архивов модов и удаляются после успешного завершения.

**Расположение:** `<папка_архивов>/<имя_файла>.download_state.json`

#### Пример

```json
{
  "url": "https://example.com/releases/MyMod_v2.0.7z",
  "filename": "MyMod_v2.0.7z",
  "total_bytes": 5242880,
  "downloaded_bytes": 2621440,
  "expected_md5": "d41d8cd98f00b204e9800998ecf8427e"
}
```

#### Поля

| Поле | Тип | Описание |
|---|---|---|
| `url` | string | URL загрузки |
| `filename` | string | Имя целевого файла |
| `total_bytes` | int | Общий размер файла в байтах |
| `downloaded_bytes` | int | Загружено байт на данный момент |
| `expected_md5` | string/null | Ожидаемый MD5-хеш для проверки (может быть `null`) |

> Эти файлы автоматически удаляются после успешной загрузки. При прерывании загрузки файл состояния позволяет программе возобновить скачивание с того места, где оно было прервано.

---

### config.json

Основной файл конфигурации приложения. Хранит все настройки пользователя, состояние окна и список репозиториев.

**Расположение:** `config/config.json`

#### Пример

```json
{
  "game_folder": "D:/Games/Steam/steamapps/common/MechWarrior 5 Mercenaries",
  "mods_folder": "D:/Games/Steam/steamapps/common/MechWarrior 5 Mercenaries/MW5Mercs/Mods",
  "steam_mods_folder": "D:/Games/Steam/steamapps/workshop/content/784080",
  "game_version": "1.1.383",
  "language": "ru",
  "check_nexusmods_updates": true,
  "check_repo_updates": true,
  "close_on_launch": false,
  "copy_mod_rules": false,
  "copy_mod_properties": false,
  "archives_folder": "data/downloads",
  "card_styles": {},
  "panel_position_mods": "right",
  "panel_position_catalog": "right",
  "conflict_display": "conflicts_tab",
  "repositories": [
    {
      "name": "Community Repository",
      "url": "https://raw.githubusercontent.com/user/mw5-repo/main",
      "enabled": true
    }
  ],
  "window_width": 1280,
  "window_height": 720,
  "window_x": 100,
  "window_y": 100,
  "window_maximized": false,
  "first_run": false
}
```

#### Поля

| Поле | Тип | По умолчанию | Описание |
|---|---|---|---|
| `game_folder` | string | `""` | Путь к папке установки игры |
| `mods_folder` | string | `""` | Путь к папке модов (обычно `<game_folder>/MW5Mercs/Mods`) |
| `steam_mods_folder` | string | `""` | Путь к папке модов Steam Workshop (опционально) |
| `game_version` | string | `""` | Версия игры (вводится пользователем вручную) |
| `language` | string | `"en"` | Код языка интерфейса (`"en"`, `"ru"`, `"uk"`) |
| `check_nexusmods_updates` | bool | `true` | Проверять обновления Nexusmods при запуске |
| `check_repo_updates` | bool | `true` | Проверять обновления репозиториев при запуске |
| `close_on_launch` | bool | `false` | Закрывать приложение при запуске игры |
| `copy_mod_rules` | bool | `false` | Состояние по умолчанию чекбокса «Копировать правила мода» на странице загрузки |
| `copy_mod_properties` | bool | `false` | Состояние по умолчанию чекбокса «Копировать свойства мода» на странице загрузки |
| `archives_folder` | string | `"data/downloads"` | Папка для скачанных архивов |
| `card_styles` | object | `{}` | Пользовательские переопределения цветов карточек |
| `panel_position_mods` | string | `"right"` | Позиция панели информации на странице модов (`"left"` или `"right"`) |
| `panel_position_catalog` | string | `"right"` | Позиция панели информации на странице каталога (`"left"` или `"right"`) |
| `conflict_display` | string | `"conflicts_tab"` | Режим отображения конфликтов: `"always"` или `"conflicts_tab"` |
| `repositories` | array | `[]` | Список настроенных репозиториев (см. ниже) |
| `window_width` | int | `1280` | Ширина окна в пикселях |
| `window_height` | int | `720` | Высота окна в пикселях |
| `window_x` | int | `100` | Позиция окна X |
| `window_y` | int | `100` | Позиция окна Y |
| `window_maximized` | bool | `false` | Развёрнуто ли окно на весь экран |
| `first_run` | bool | `true` | Флаг первого запуска (запускает мастер настройки) |

#### Поля записи репозитория

| Поле | Тип | По умолчанию | Описание |
|---|---|---|---|
| `name` | string | `""` | Отображаемое имя репозитория |
| `url` | string | `""` | URL или локальный путь к корню репозитория |
| `enabled` | bool | `true` | Активен ли репозиторий |

---

### Модпаки

Модпаки сохраняют снимок конфигурации модов пользователя для обмена или восстановления.

**Расположение:** `config/modpacks/<имя>.json`

#### Пример

```json
{
  "name": "My Battle Setup",
  "mods": [
    {
      "folder_name": "WeaponPack",
      "display_name": "Yet Another Weapon",
      "version": "26.0",
      "author": "Author",
      "is_installed": true,
      "is_translation": false,
      "source_type": "nexusmods",
      "nexusmods_mod_id": 1080,
      "nexusmods_mod_name": "Yet Another Weapon",
      "installed_version": "26.0",
      "is_nexusmods_linked": true,
      "is_repo_linked": false
    }
  ],
  "mods_preset": ["1"],
  "rules_preset": ["2"],
  "repositories": ["https://raw.githubusercontent.com/user/mw5-repo/main"],
  "mods_preset_data": {},
  "rules_preset_data": {}
}
```

#### Поля

| Поле | Тип | Описание |
|---|---|---|
| `name` | string | Отображаемое имя модпака |
| `mods` | array | Список записей модов с метаданными |
| `mods_preset` | array | Имена связанных пресетов модов |
| `rules_preset` | array | Имена связанных пресетов правил |
| `repositories` | array | URL-адреса репозиториев, используемых этим модпаком |
| `mods_preset_data` | object | Встроенные данные пресетов модов (для обмена) |
| `rules_preset_data` | object | Встроенные данные пресетов правил (для обмена) |

#### Поля записи мода

| Поле | Тип | Описание |
|---|---|---|
| `folder_name` | string | Имя папки мода |
| `display_name` | string | Отображаемое имя мода |
| `version` | string | Версия мода |
| `author` | string | Автор мода |
| `is_installed` | bool | Был ли мод установлен на момент создания модпака |
| `is_translation` | bool | Является ли мод переводом |
| `source_type` | string | Тип источника (например, `"nexusmods"`, `"repository"`) |
| `nexusmods_mod_id` | int | ID мода на Nexusmods (если привязан) |
| `nexusmods_mod_name` | string | Имя мода на Nexusmods (если привязан) |
| `installed_version` | string | Установленная версия на момент создания |
| `is_nexusmods_linked` | bool | Привязан ли мод к Nexusmods |
| `is_repo_linked` | bool | Привязан ли мод к репозиторию |

---

### Пресеты

Пресеты сохраняют и восстанавливают конфигурации порядка модов и правил независимо друг от друга.

#### Пресеты модов

**Расположение:** `config/presets/mods/<имя>.json`

Сохраняет состояние включения и порядок загрузки всех модов.

```json
{
  "MyPreset": {
    "mods": {
      "CoreFramework": {
        "bEnabled": true,
        "defaultLoadOrder": 1
      },
      "WeaponPack": {
        "bEnabled": true,
        "defaultLoadOrder": 2
      },
      "VisualMod": {
        "bEnabled": false,
        "defaultLoadOrder": 3
      }
    }
  }
}
```

| Поле | Тип | Описание |
|---|---|---|
| `<имя_пресета>.mods` | object | Словарь имён папок модов и их состояний |
| `<имя_пресета>.mods.<папка>.bEnabled` | bool | Включён ли мод |
| `<имя_пресета>.mods.<папка>.defaultLoadOrder` | int | Позиция в порядке загрузки |

#### Пресеты правил

**Расположение:** `config/presets/rules/<имя>.json`

Сохраняет полную конфигурацию правил.

```json
{
  "MyRulesPreset": {
    "rules_enabled": true,
    "rules": [
      {
        "mod_folder": "TranslationMod",
        "rule_type": "after",
        "target_folder": "OriginalMod",
        "enabled": true
      },
      {
        "mod_folder": "CoreFramework",
        "rule_type": "first",
        "enabled": true
      }
    ]
  }
}
```

| Поле | Тип | Описание |
|---|---|---|
| `<имя_пресета>.rules_enabled` | bool | Глобальный переключатель системы правил |
| `<имя_пресета>.rules` | array | Массив правил (формат идентичен `mod_manager_rules.json`) |

> **Примечание:** Поле `target_folder` добавляется только для правил типа `after`/`before`.

---

### mod_manager_backup.json

Полный файл резервной копии приложения для экспорта/импорта всех настроек, пресетов и правил.

**Расположение:** Путь выбирается пользователем (имя по умолчанию: `mod_manager_backup.json`)

#### Пример

```json
{
  "config": {
    "game_folder": "D:/Games/...",
    "language": "ru",
    "repositories": [
      { "name": "My Repo", "url": "https://...", "enabled": true }
    ]
  },
  "presets_mods": {
    "1.json": { "1": { "mods": { "ModA": { "bEnabled": true, "defaultLoadOrder": 1 } } } }
  },
  "presets_rules": {
    "1.json": { "1": { "rules_enabled": true, "rules": [] } }
  }
}
```

#### Поля

| Поле | Тип | Описание |
|---|---|---|
| `config` | object | Полное содержимое `config.json` |
| `presets_mods` | object | Все пресеты модов (ключ = имя файла включая `.json`) |
| `presets_rules` | object | Все пресеты правил (ключ = имя файла включая `.json`) |

> Этот файл создаётся через **Настройки → Экспорт резервной копии** и восстанавливается через **Настройки → Импорт резервной копии**. Импорт перезаписывает текущую конфигурацию и все пресеты.

---

### Пример многофайловой загрузки

Когда архив мода разделён на несколько файлов (например, из-за ограничений размера), используйте нумерованные ключи в `expected_files`, `url`, `size` и `hash`:

```json
{
  "versions": [
    {
      "version": "2.2",
      "category": "MAIN",
      "description": "Полный мод (3 части)",
      "expected_files": {
        "1": "MyMod_Part1.7z",
        "2": "MyMod_Part2.7z",
        "3": "MyMod_Part3.7z"
      },
      "url": {
        "1": "https://example.com/releases/MyMod_Part1.7z",
        "2": "https://example.com/releases/MyMod_Part2.7z",
        "3": "https://example.com/releases/MyMod_Part3.7z"
      },
      "size": {
        "1": 1048576000,
        "2": 729978606,
        "3": 524288000
      },
      "hash": {
        "1": "sha256:aaa111...",
        "2": "sha256:bbb222...",
        "3": "sha256:ccc333..."
      }
    }
  ]
}
```

Программа загружает все части последовательно, проверяя хеш каждого файла при его наличии. Затем все части извлекаются в папку мода.

---

### Полный пример репозитория

```
my-mw5-repo/
├── repository.json
├── early_access_mods/
│   ├── featured.json
│   ├── WeaponPack/
│   │   ├── mod.json
│   │   ├── description.md
│   │   ├── files.json
│   │   ├── requirements.json
│   │   ├── changelog.json
│   │   └── preview.png
│   └── BalanceMod/
│       ├── mod.json
│       └── files.json
├── early_access_translations/
│   ├── featured.json
│   └── RussianTranslation/
│       ├── mod.json
│       └── description.md
├── nexusmods_mods/
│   ├── featured.json
│   └── 12345/
│       └── nexusmods_id.json
└── nexusmods_translations/
    ├── featured.json
    └── 67890/
        └── nexusmods_id.json
```

---

### Публикация репозитория

#### GitHub / GitLab / Codeberg / Bitbucket / Gitea / Forgejo

Разместите папку репозитория в публичном git-репозитории. Программа обращается к raw-файлам напрямую.

Программа **автоматически конвертирует** web-URL в raw URL для следующих платформ:

| Платформа | Пользователь вводит | Программа конвертирует в |
|---|---|---|
| GitHub | `https://github.com/user/repo` | `https://raw.githubusercontent.com/user/repo/main` |
| GitLab | `https://gitlab.com/user/repo` | `https://gitlab.com/user/repo/-/raw/main` |
| Codeberg | `https://codeberg.org/user/repo` | `https://codeberg.org/user/repo/raw/branch/main` |
| Bitbucket | `https://bitbucket.org/user/repo` | `https://bitbucket.org/user/repo/raw/main` |
| Gitea (свой сервер) | `https://gitea.example.com/user/repo/src/branch/main` | `https://gitea.example.com/user/repo/raw/branch/main` |

> **Примечание:** Если ветка `main` не найдена, программа также попробует `master`. Можно указать ветку явно, напр.: `https://github.com/user/repo/tree/dev`.

> **Самостоятельный Gitea/Forgejo:** Программа не может автоопределить пользовательские домены. Используйте URL с `/src/branch/...` для автоконвертации или укажите raw URL напрямую: `https://gitea.example.com/user/repo/raw/branch/main`.

**Пример URL для Forgejo:**
```
http://192.168.3.10:7205/username/mw5-repo/raw/branch/main
```

#### Статический HTTP-сервер

Любой сервер, отдающий файлы по прямым URL. Nginx, Apache, Caddy, GitHub Pages, etc.

#### Локальный путь (для тестирования)

```
D:\MyMods\TestRepository
```
или
```
/home/user/mw5-repo
```

---

### Замечания для разработчиков репозитория

1. **Имена папок** модов не должны меняться после публикации — пользователи потеряют связь с установленными модами.
2. **Ссылки на файлы** в `url` должны быть прямыми (без редиректов и авторизации). GitHub Releases даёт прямые raw-ссылки.
3. **Кодировка** всех JSON и Markdown файлов — UTF-8.
4. **`is_translation`** важен: переводы отображаются отдельно от основных модов в интерфейсе.
5. Поле `name` у категории может быть любой строкой — программа использует его как внутренний идентификатор и следует по пути, указанному в `path` (или по `name`, если `path` не задан).
6. Версии в массиве `versions` каждой файловой группы могут располагаться в **любом порядке** — программа автоматически определяет актуальную версию, сравнивая строки версий по семантическому версионированию.

---

## Инструменты

### repo_file_info.py — генератор размеров и хешей файлов

Вспомогательный скрипт в папке `tools/`, который генерирует размеры файлов и SHA-256 хеши для архивов репозитория. Результат можно использовать для заполнения полей `size` и `hash` в `files.json` / `mod.json`.

Инструмент имеет два режима:
- **Интерактивный** — запуск без аргументов (или через `repo_file_info.bat`). Скрипт пошагово проведёт через выбор папки, режима сканирования и формата вывода, а затем сохранит результат в файл.
- **CLI** — передача пути и флагов как аргументов командной строки.

#### Быстрый старт (Windows)

Дважды кликните `tools/repo_file_info.bat` — запустится интерактивный мастер.

#### Шаги интерактивного режима

1. **Выбор папки** — через диалог проводника или ввод пути вручную
2. **Режим сканирования** — все файлы или только архивы (`.7z`, `.zip`, `.rar`, ...)
3. **Рекурсия** — сканировать подпапки или нет
4. **Формат вывода** — текстовая таблица, JSON одиночный или JSON мульти-файл
5. **URL-префикс** — опциональный префикс для ссылок загрузки (только JSON)
6. **Результат** — выводится в консоль и сохраняется в файл рядом со сканируемой папкой

#### Использование CLI

```bash
python tools/repo_file_info.py <путь> [опции]
```

#### Опции CLI

| Флаг | Описание |
|---|---|
| `--json` | Вывод в формате JSON-сниппета для `files.json` |
| `--multi` | Многофайловый режим: группировка всех файлов в одну запись версии с нумерованными ключами (`url_2`, `size_2` и т.д.) |
| `--recursive`, `-r` | Рекурсивное сканирование подкаталогов |
| `--archives-only`, `-a` | Только архивные файлы (`.7z`, `.zip`, `.rar` и т.д.) |
| `--url-prefix <url>` | Префикс URL для ссылок загрузки в JSON-выводе |
| `--save`, `-s` | Сохранить результат в файл рядом со сканируемой папкой |

#### Примеры CLI

```bash
# Сканирование одного архива
python tools/repo_file_info.py "D:/releases/MyMod_v2.0.7z"

# Сканирование папки с JSON-выводом
python tools/repo_file_info.py "D:/releases/" --json

# Рекурсивное сканирование, только архивы, с URL-префиксом, сохранение в файл
python tools/repo_file_info.py "D:/releases/" --recursive --archives-only --json \
  --url-prefix "https://github.com/user/repo/releases/download/v1.0/" --save

# Многофайловый режим (несколько архивов в одной записи версии)
python tools/repo_file_info.py "D:/releases/" --json --multi
```

---

---

# Українська

## Зміст

- [Для користувачів](#для-користувачів)
  - [Встановлення](#встановлення)
  - [Перший запуск](#перший-запуск)
  - [Інтерфейс](#інтерфейс)
  - [Керування модами](#керування-модами)
  - [Порядок завантаження](#порядок-завантаження)
  - [Правила порядку завантаження](#правила-порядку-завантаження)
  - [Пресети](#пресети-1)
  - [Модпаки](#модпаки-1)
  - [Каталог — Nexusmods](#каталог--nexusmods-1)
  - [Сторонні репозиторії](#сторонні-репозиторії)
  - [Встановлення мода з архіву](#встановлення-мода-з-архіву)
  - [Багатопапкові архіви](#багатопапкові-архіви)
  - [Налаштування](#налаштування)
- [Для моддерів та власників репозиторіїв](#для-моддерів-та-власників-репозиторіїв)
  - [Огляд системи репозиторіїв](#огляд-системи-репозиторіїв)
  - [Структура репозиторію](#структура-репозиторію)
  - [repository.json](#repositoryjson-2)
  - [Категорії репозиторію](#категорії-репозиторію)
  - [Тип repository — структура мода](#тип-repository--структура-мода-1)
  - [Тип nexus_api — структура мода](#тип-nexus_api--структура-мода-1)
  - [Файли метаданих мода](#файли-метаданих-мода)
  - [Сумісність перекладів (for_mod_name)](#сумісність-перекладів-for_mod_name)
  - [featured.json — рекомендовані моди](#featuredjson--рекомендовані-моди)
  - [mod_manager_properties.json](#mod_manager_propertiesjson-2)
  - [mod_manager_install_rules.json](#mod_manager_install_rulesjson-2)
  - [Повний приклад репозиторію](#повний-приклад-репозиторію)
  - [Публікація репозиторію](#публікація-репозиторію)
  - [Зауваження для розробників репозиторію](#зауваження-для-розробників-репозиторію)
- [Інструменти](#інструменти)
  - [repo_file_info.py — генератор розмірів та хешів файлів](#repo_file_infopy--генератор-розмірів-та-хешів-файлів)

---

## Для користувачів

### Встановлення

#### Windows

1. Завантажте архів `MW5Mercs_Mod_Manager_vX.X.X_windows_x64.zip` зі сторінки релізів
2. Розпакуйте в будь-яку папку (наприклад, `C:\Tools\MW5ModManager`)
3. Запустіть `MW5Mercs Mod Manager.exe`

#### Linux

1. Завантажте архів `MW5Mercs_Mod_Manager_vX.X.X_linux_x64.zip`
2. Розпакуйте: `unzip MW5Mercs_Mod_Manager_*.zip`
3. Надайте права на виконання: `chmod +x "MW5Mercs Mod Manager"`
4. Запустіть: `./"MW5Mercs Mod Manager"`

#### Системні вимоги

| | Windows | Linux |
|---|---|---|
| ОС | Windows 10/11 x64 | Ubuntu 20.04+, Fedora 36+, Arch та інші |
| Гра | MechWarrior 5: Mercenaries (Steam, Epic, GOG) | те саме |
| .NET / Runtime | не потрібно | не потрібно |

---

### Перший запуск

При першому запуску відкриється майстер налаштування. Потрібно вказати:

**Папка гри** — коренева папка MechWarrior 5, наприклад:
```
D:\Games\Steam\steamapps\common\MechWarrior 5 Mercenaries
```

**Папка Steam Workshop** (опціонально) — папка з модами Steam Workshop:
```
D:\Games\Steam\steamapps\workshop\content\784080
```

**Мова інтерфейсу** — English, Русский, Українська.

Після цього програма автоматично знайде папку модів `MW5Mercs/Mods` всередині папки гри.

---

### Інтерфейс

Програма складається з кількох сторінок, які перемикаються через бокове меню:

| Сторінка | Мітка | Опис |
|---|---|---|
| **Головна** | Головна | Список встановлених модів, огляд оновлень, запуск гри |
| **Моди** | Моди | Детальний список усіх модів з вкладками: ОГЛЯД, КОНФЛІКТИ, ПРАВИЛА, ПРЕСЕТИ |
| **Файли** | Файли | Перегляд файлової системи папки модів |
| **Каталог** | Каталог | Пошук та встановлення модів з Nexusmods і репозиторіїв |
| **Параметри** | Параметри | Конфігурація програми |

На сторінці **Каталог** є додаткові вкладки:

| Вкладка | Мітка | Опис |
|---|---|---|
| **Встановлення** | ВСТАНОВЛЕННЯ | Встановлення мода з архіву або папки |
| **Моди** | МОДИ | Перегляд та встановлення модів з каталогів Nexusmods і репозиторіїв |
| **Переклади** | ПЕРЕКЛАДИ | Перегляд та встановлення перекладів |
| **Оновлення** | ОНОВЛЕННЯ | Перевірка та встановлення оновлень для зв'язаних модів |
| **Зв'язки** | ЗВ'ЯЗКИ | Керування зв'язками між встановленими модами та джерелами (Nexusmods / репозиторій) |
| **Модпаки** | МОДПАКИ | Створення, керування та застосування колекцій модів з пресетами |

---

### Керування модами

На сторінці **Моди** (вкладка ОГЛЯД) відображається список усіх знайдених модів з:
- папки `MW5Mercs/Mods` всередині гри
- папки Steam Workshop (якщо налаштовано)

Доступні дії для кожного мода:
- **Увімкнути / вимкнути** — змінює поле `defaultEnabled` у `mod.json` мода
- **Змінити порядок завантаження** — перетягуванням або введенням числа
- **Відкрити папку мода** — у Explorer / файловому менеджері
- **Видалити** — видаляє папку мода з диска

> **Увага:** порядок завантаження задається полем `defaultLoadOrder` у `mod.json` кожного мода. Чим більше число — тим пізніше завантажується мод. При конфлікті перемагає мод з більшим значенням.

#### Конфлікти

Програма автоматично виявляє конфлікти — коли два або більше модів змінюють одні й ті самі ігрові файли. Конфлікти відображаються на вкладці КОНФЛІКТИ на сторінці **Моди**.

---

### Порядок завантаження

MW5 завантажує моди в порядку, визначеному полем `defaultLoadOrder` у `mod.json`. Мод з більшим числом перекриває моди з меншим числом при конфлікті файлів.

У програмі порядок змінюється:
- **Перетягуванням** картки мода
- **Введенням числа** напряму в поле
- **Кнопками стрілок** — зсунути вгору/вниз

Після зміни порядку програма фізично оновлює файли `mod.json` — зміни набувають чинності при наступному запуску гри.

---

### Правила порядку завантаження

Правила — це обмеження, які програма застосовує автоматично при сортуванні.

#### Типи правил

| Тип | Опис |
|---|---|
| **Після мода** (`after`) | Цей мод повинен завантажуватися після вказаного мода |
| **Перед модом** (`before`) | Цей мод повинен завантажуватися перед вказаним модом |
| **На початок** (`first`) | Цей мод завжди повинен бути в першій групі (малі номери) |
| **В кінець** (`last`) | Цей мод завжди повинен бути в останній групі (великі номери) |

#### Створення правила

1. Перейдіть на сторінку **Моди** → вкладка ПРАВИЛА
2. Натисніть **Додати правило**
3. Оберіть мод і тип правила
4. Для правил `after`/`before` — оберіть другий мод
5. Натисніть **Зберегти**

Правила зберігаються у файлі `mod_manager_rules.json` у папці модів. При натисканні **Застосувати** програма пересортовує моди відповідно до всіх активних правил.

---

### Пресети

Пресет — це збережена конфігурація: які моди увімкнені та в якому порядку завантажуються.

#### Збереження пресету

1. Перейдіть на сторінку **Моди** → вкладка ПРЕСЕТИ
2. Натисніть **Пресет модів** → **Створити**
3. Введіть назву пресету

#### Застосування пресету

1. Оберіть пресет зі списку
2. Натисніть **Застосувати**

Пресети зберігаються у папці `config/presets/mods/` у форматі JSON. Кожен файл — це один пресет:

```json
{
  "1": {
    "mods": {
      "ModFolderName": {
        "bEnabled": true,
        "defaultLoadOrder": 1
      },
      "AnotherMod": {
        "bEnabled": false,
        "defaultLoadOrder": 2
      }
    }
  }
}
```

---

### Модпаки

Модпак — це колекція посилань на моди, пресетів та URL-ів репозиторіїв, об'єднаних разом. На відміну від пресетів (які зберігають лише стани увімкнення/вимкнення модів та порядок завантаження), модпаки зберігають повні метадані модів, включаючи джерела (Nexusmods, репозиторії).

Модпаки **не містять** файлів модів — лише посилання на них (імена папок, ID Nexusmods, URL репозиторіїв). При застосуванні модпака програма додає невстановлені моди до черги встановлення та відновлює включені пресети.

#### Створення модпака

1. Перейдіть у **Каталог** → вкладка **МОДПАКИ** (права панель)
2. Натисніть **Створити**
3. Каталог переключиться на показ встановлених зв'язаних модів
4. Позначте моди, які хочете включити (можна також переключитися на Nexusmods або репозиторії як джерело)
5. Опціонально оберіть **Пресет модів** та/або **Пресет правил** з існуючих
6. Пов'язані репозиторії додаються автоматично з обраних модів
7. Введіть назву модпака
8. Натисніть **Створити модпак**

#### Застосування модпака

1. Оберіть модпак зі списку
2. Натисніть **Застосувати** (✓)
3. Програма:
   - Перевіряє, які моди вже встановлені
   - Додає невстановлені моди до черги встановлення
   - Відновлює та застосовує включені пресети (модів та правил)
   - Показує підсумкове повідомлення

#### Попередній перегляд модпака

Клікніть на назву модпака (без натискання «Застосувати») для попереднього перегляду вмісту:
- **Моди** — список включених модів зі статусом встановлення
- **Пресети правил** — включені пресети правил
- **Пресети модів** — включені пресети модів
- **Репозиторії** — пов'язані репозиторії

#### Імпорт / Експорт

- **Імпорт**: Натисніть **Імпорт** → оберіть `.json` файл модпака
- **Експорт**: Оберіть модпак → натисніть **Експорт** → вкажіть місце збереження

Модпаки зберігаються у `config/modpacks/` у форматі JSON. Кожен файл містить назву модпака, список модів з метаданими, дані пресетів та URL-и репозиторіїв.

---

### Каталог — Nexusmods

На сторінці **Каталог** (вкладки МОДИ та ПЕРЕКЛАДИ) відображаються моди з сайту Nexusmods через GraphQL v2 API.

**Авторизація не потрібна.** Програма звертається до каталогу Nexusmods, отримує інформацію про моди та генерує посилання на завантаження без необхідності акаунту Nexusmods або API-ключа.

**Можливості:**
- Пошук модів за назвою
- Перегляд опису, скріншотів, файлів мода
- Завантаження та встановлення мода напряму з програми
- Перевірка оновлень для зв'язаних модів

---

### Сторонні репозиторії

Репозиторії — це окремі каталоги модів, розміщені на будь-якому HTTP/HTTPS сервері або локально. Це основна система для розповсюдження модів, не розміщених на Nexusmods (наприклад, ранній доступ, переклади).

#### Додавання репозиторію

1. Перейдіть у **Параметри** → вкладка ЗАГАЛЬНІ
2. Натисніть **Додати** у розділі Репозиторії
3. Введіть URL репозиторію або шлях до локальної папки:
   - HTTP/HTTPS: `https://example.com/my-mw5-repo`
   - Локально: `D:\MyRepository` або `/home/user/mw5-repo`
4. Введіть назву для відображення
5. Натисніть **Зберегти**

Після додавання програма завантажить `repository.json` і покаже доступні категорії в каталозі.

---

### Встановлення мода з архіву

Мод також можна встановити з готового архіву (`.7z`, `.zip`, `.rar`) або з папки.

1. Перейдіть у **Каталог** → вкладка ВСТАНОВЛЕННЯ
2. Оберіть архів або папку з модом
3. Програма розпакує архів у папку модів гри

Підтримувані формати: `.7z`, `.zip`, `.rar`, `.tar`, `.gz`.
Для розпакування використовується вбудований 7-Zip (постачається разом з програмою).

---

### Багатопапкові архіви

Якщо архів містить кілька папок модів (кожна зі своїм `mod.json`), програма встановить їх усі. Кожна папка встановлюється окремо до директорії модів.

При створенні зв'язку з Nexusmods або репозиторієм для такого мода, зв'язок автоматично застосовується до всіх споріднених папок з одного архіву.

---

### Налаштування

| Параметр | Опис |
|---|---|
| **Папка гри** | Шлях до MW5 (обов'язково) |
| **Папка Steam Workshop** | Шлях до папки Workshop Steam (опціонально) |
| **Версія гри** | Текстове поле для вказівки версії (інформаційно) |
| **Мова** | Мова інтерфейсу: English, Русский, Українська |
| **Перевіряти оновлення Nexusmods** | Перевіряти оновлення при старті |
| **Перевіряти оновлення репозиторіїв** | Перевіряти оновлення репозиторіїв при старті |
| **Закривати при запуску гри** | Автоматично закрити менеджер при запуску MW5 |
| **Папка завантажень** | Куди зберігаються завантажені архіви |
| **Репозиторії** | Список підключених репозиторіїв |

---

---

## Для моддерів та власників репозиторіїв

### Огляд системи репозиторіїв

Репозиторій — це папка (локальна або на HTTP/HTTPS сервері), що містить:
- `repository.json` — опис репозиторію та його категорій
- Папки категорій з підпапками для кожного мода

Програма читає репозиторій при запуску та відображає моди в каталозі. При натисканні «Встановити» — завантажує архів за посиланням з метаданих та встановлює мод.

**Підтримувані способи хостингу:**
- Будь-який HTTP/HTTPS сервер з прямим доступом до файлів (GitHub Pages, Nginx, Apache, CDN)
- GitHub / GitLab / Codeberg / Bitbucket / Gitea / Forgejo репозиторій (автонормалізація web-URL в raw)
- Локальна папка на диску (для тестування)

---

### Структура репозиторію

```
my-repository/
├── repository.json               # Обов'язковий — опис репозиторію
│
├── early_access_mods/            # Папка категорії (шлях задається в repository.json)
│   ├── featured.json             # Опціонально — список рекомендованих модів
│   ├── MyMod/                    # Папка мода (ім'я папки = ідентифікатор)
│   │   ├── mod.json              # Обов'язковий — метадані мода
│   │   ├── description.md        # Опціонально — опис (Markdown)
│   │   ├── files.json             # Обов'язковий — список файлів з версіями та посиланнями
│   │   ├── requirements.json     # Опціонально — залежності
│   │   ├── changelog.json        # Опціонально — історія змін
│   │   └── preview.png           # Опціонально — зображення прев'ю
│   └── AnotherMod/
│       ├── mod.json
│       └── files.json
│
├── early_access_translations/    # Папка перекладів
│   ├── featured.json
│   └── MyTranslation/
│       ├── mod.json
│       └── files.json
│
├── nexusmods_mods/               # Категорія nexus_api (посилання на Nexusmods)
│   ├── featured.json
│   └── 12345/                    # Ім'я папки = nexusmods ID мода
│       └── nexusmods_id.json
│
└── nexusmods_translations/       # Переклади з Nexusmods
    ├── featured.json
    └── 67890/
        └── nexusmods_id.json
```

---

### repository.json

Кореневий файл опису репозиторію. **Обов'язковий.**

```json
{
  "name": "My MW5 Repository",
  "categories": {
    "1": {
      "name": "early_access_mods",
      "type": "repository",
      "is_translation": false,
      "path": "early_access_mods",
      "display_name": "Моди раннього доступу",
      "mods": ["WeaponPack", "BalanceMod"]
    },
    "2": {
      "name": "early_access_translations",
      "type": "repository",
      "is_translation": true,
      "path": "early_access_translations",
      "display_name": "Переклади",
      "mods": ["RussianTranslation"]
    },
    "3": {
      "name": "nexusmods_mods",
      "type": "nexus_api",
      "is_translation": false,
      "path": "nexusmods_mods",
      "display_name": "Популярні моди з Nexusmods",
      "mods": ["12345"]
    },
    "4": {
      "name": "nexusmods_translations",
      "type": "nexus_api",
      "is_translation": true,
      "path": "nexusmods_translations",
      "display_name": "Переклади з Nexusmods",
      "mods": ["67890"]
    }
  }
}
```

#### Поля repository.json

| Поле | Тип | Обов'язковість | Опис |
|---|---|---|---|
| `name` | string | обов'язково | Назва репозиторію для відображення |
| `categories` | object | обов'язково | Об'єкт категорій (ключ — довільний ідентифікатор) |

#### Поля категорії

| Поле | Тип | Обов'язковість | Опис |
|---|---|---|---|
| `name` | string | обов'язково | Ім'я категорії — будь-який рядок. Використовується як внутрішній ідентифікатор. Також використовується як шлях до папки, якщо `path` не вказано |
| `type` | string | обов'язково | `repository` — повні метадані в папці, `nexus_api` — тільки ID для запиту до Nexusmods API |
| `is_translation` | bool | обов'язково | `true` якщо категорія містить переклади |
| `path` | string | обов'язково | Відносний шлях до папки категорії від кореня репозиторію |
| `display_name` | string | опціонально | Користувацьке ім'я для відображення в інтерфейсі |
| `mods` | масив рядків | обов'язково для віддалених | Список імен папок модів. **Обов'язковий** для віддалених (HTTP) репозиторіїв — без нього програма не зможе виявити моди. Для локальних репозиторіїв опціональний (програма читає файлову систему). |

> **Важливо:** ключі категорій (`"1"`, `"2"`, ...) — довільні рядки. Програма використовує поле `name` всередині об'єкта як канонічний ідентифікатор.

---

### Категорії репозиторію

#### Тип `repository`

Програма завантажує метадані мода з папок з `mod.json`. Весь опис, версії, залежності — в самому репозиторії. Підходить для модів, що розповсюджуються поза Nexusmods.

#### Тип `nexus_api`

Програма використовує `nexusmods_id.json` з папки для отримання ID мода, потім завантажує повні дані через Nexusmods GraphQL API. Використовується для відображення модів з Nexusmods у каталозі репозиторію.

---

### Тип `repository` — структура мода

Кожен мод — це папка всередині папки категорії.

```
CategoryFolder/
└── MyModFolderName/     ← ім'я папки = ідентифікатор мода в програмі
    ├── mod.json          ← обов'язково
    ├── files.json        ← обов'язково
    ├── description.md    ← опціонально
    ├── requirements.json ← опціонально
    ├── changelog.json    ← опціонально
    └── preview.png       ← опціонально
```

> Ім'я папки мода використовується як унікальний ідентифікатор — воно повинно залишатися постійним. Перейменування папки порушить зв'язок зі встановленим модом для користувачів.

---

### Тип `nexus_api` — структура мода

```
nexusmods_mods/
└── 12345/                      ← ім'я папки = nexusmods ID (рекомендується)
    └── nexusmods_id.json        ← обов'язково
```

**nexusmods_id.json:**

```json
{
  "nexusmods_id": 12345
}
```

Програма використовує це число для запиту до Nexusmods API та отримання назви, опису, зображень і посилань на файли мода.

---

### Файли метаданих мода

#### mod.json — обов'язковий

Основні метадані мода в репозиторії. **Не є** `mod.json` гри — це окремий формат.
Версії зберігаються окремо в `files.json`.

**Приклад для мода:**
```json
{
  "name": "My Awesome Mod",
  "author": "AuthorName",
  "mod_page": "https://github.com/author/my-awesome-mod",
  "images": {
    "preview": "preview.png"
  }
}
```

**Приклад для перекладу:**
```json
{
  "for_mod_name": "Target Mod Name",
  "name": "Target Mod Name / Translation UKR",
  "author": "AuthorName",
  "images": {
    "preview": "preview.png"
  }
}
```

| Поле | Тип | Обов'язковість | Опис |
|---|---|---|---|
| `name` | string | обов'язково | Назва мода для відображення |
| `author` | string | рекомендується | Автор мода |
| `for_mod_name` | string | тільки для перекладів | Ім'я цільового мода для перекладів. Встановіть `"Original_game"` для перевірки сумісності з версією гри з налаштувань |
| `mod_page` | string | опціонально | URL сторінки мода (GitHub, форум тощо) |
| `images.preview` | string | опціонально | Ім'я файлу або URL зображення прев'ю |

---

#### description.md — опціональний

Опис мода у форматі Markdown або звичайного тексту. Якщо файл існує — програма використовує його замість поля `description` з `mod.json`.

---

#### files.json — обов'язковий

Містить список файлів мода, згрупованих за категоріями, кожен зі своїми версіями, посиланнями на завантаження, розмірами та хешами.

**Приклад для мода:**
```json
{
  "files": [
    {
      "display_name": "Main Files",
      "category": "MAIN",
      "versions": [
        {
          "version": "2.1.0",
          "description": "Основні файли мода",
          "expected_files": { "1": "MyMod_v2.1.0.7z" },
          "url": { "1": "https://example.com/releases/v2.1.0/MyMod_v2.1.0.7z" },
          "size": { "1": 5242880 },
          "hash": { "1": "sha256:abcdef1234567890..." }
        },
        {
          "version": "2.0.0",
          "description": "Попередня стабільна версія",
          "expected_files": { "1": "MyMod_v2.0.0.7z" },
          "url": { "1": "https://example.com/releases/v2.0.0/MyMod_v2.0.0.7z" },
          "size": { "1": 4800000 },
          "hash": { "1": "sha256:fedcba0987654321..." }
        }
      ]
    }
  ]
}
```

> Кожна файлова група має `display_name` та `category` на рівні групи. Масив `versions` всередині групи містить дані, специфічні для кожної версії. Це створює картку файлу з випадаючим списком версій для кожної групи.

**Приклад для перекладу:**
```json
{
  "files": [
    {
      "display_name": "Translation",
      "versions": [
        {
          "version": "1.0.0",
          "compatibility": [
            { "version": "2.0.0", "build": "2000" }
          ],
          "expected_files": { "1": "MyTranslation_v1.0.0.7z" },
          "url": { "1": "https://example.com/releases/v1.0.0/MyTranslation_v1.0.0.7z" },
          "size": { "1": 1048576 },
          "hash": { "1": "sha256:abc123..." }
        }
      ]
    }
  ]
}
```

#### Поля файлової групи

| Поле | Тип | Опис |
|---|---|---|
| `display_name` | string | Відображуване ім'я картки файлу. Якщо не вказано, використовується ім'я архіву з `expected_files` першої версії |
| `category` | string | Категорія файлу: `"MAIN"` (за замовчуванням) або `"OPTIONAL"`. Тільки для модів |

#### Поля версії

| Поле | Тип | Опис |
|---|---|---|
| `version` | string | Номер версії (наприклад, `"2.1.0"`) |
| `compatibility` | array | Список сумісних версій цільового мода (або версій гри, якщо `for_mod_name` = `"Original_game"`). Тільки для перекладів |
| `description` | string | Опис версії/файлу (опціонально) |
| `expected_files` | object | Очікувані імена файлів, формат словника: `{"1": "file.7z", "2": "part2.7z"}` |
| `url` | object | Посилання на завантаження, формат словника: `{"1": "https://..."}`. Ключі відповідають `expected_files` |
| `size` | object | Розміри файлів у **байтах**, формат словника: `{"1": 5242880}`. Приклад: `5242880` = 5 МБ |
| `hash` | object | Хеші файлів, формат словника: `{"1": "sha256:..."}` (опціонально, для перевірки) |

> Всі поля, пов'язані з файлами (`expected_files`, `url`, `size`, `hash`), використовують нумерований формат словника, де ключі (`"1"`, `"2"`, ...) відповідають частинам файлів. Для завантаження одного файлу використовуйте ключ `"1"`.

---

#### requirements.json — опціональний

Залежності мода від інших модів.

```json
{
  "requirements": [
    {
      "name": "YetAnotherWeaponCompleteEdition",
      "folder": "YetAnotherWeaponCompleteEdition",
      "required": true,
      "description": "Обов'язкова залежність"
    },
    {
      "name": "MW5 Compatibility Framework",
      "folder": "MW5Compatibility",
      "required": false,
      "description": "Рекомендується для повної сумісності"
    }
  ]
}
```

| Поле | Тип | Опис |
|---|---|---|
| `name` | string | Назва залежності для відображення |
| `folder` | string | Ім'я папки мода-залежності (для пошуку серед встановлених) |
| `required` | bool | `true` — обов'язкова, `false` — рекомендується |
| `description` | string | Пояснення до залежності |

---

#### changelog.json — опціональний

Історія змін мода.

```json
{
  "changelog": [
    {
      "version": "2.1.0",
      "changes": [
        "Додано HAG 20",
        "Виправлено баланс Gauss Rifle",
        "Сумісність з патчем 1.1.380"
      ]
    }
  ]
}
```

---

### Сумісність перекладів (for_mod_name)

Переклади можуть вказувати, для якого мода (або самої гри) вони призначені та з якими версіями сумісні.

У `mod.json` перекладу використовуйте поле `for_mod_name`:
- Вкажіть **ім'я папки** цільового мода — сумісність перевірятиметься за версією встановленого мода.
- Вкажіть `"Original_game"` — сумісність перевірятиметься за **версією гри** з налаштувань програми.

Масив `compatibility` у кожному записі версії містить пари версія/збірка, з якими переклад сумісний.

#### Приклад: переклад для базової гри

**mod.json:**
```json
{
  "for_mod_name": "Original_game",
  "name": "Game Translation UKR",
  "author": "Translator"
}
```

**files.json:**
```json
{
  "files": [
    {
      "display_name": "Game Translation UKR",
      "versions": [
        {
          "version": "1.1.383",
          "compatibility": [
            { "version": "1.1.383", "build": "" },
            { "version": "1.1.380", "build": "" }
          ],
          "expected_files": { "1": "translation_v1.1.383.7z" },
          "url": { "1": "https://example.com/releases/translation_v1.1.383.7z" },
          "size": { "1": 102400 },
          "hash": { "1": "sha256:abc123..." }
        }
      ]
    }
  ]
}
```

Коли `for_mod_name` = `"Original_game"`:
- Поле `build` всередині записів `compatibility` можна залишити **порожнім** (`""`), оскільки версія гри в налаштуваннях зазвичай не містить номер збірки.
- Програма перетворює `"Original_game"` → `"Game"` та використовує наявний механізм перевірки версії гри (`is_game_version_requirement()`).
- Версія гри береться з **Налаштування → Версія гри** (налаштовується користувачем).

#### Приклад: переклад для конкретного мода

**mod.json:**
```json
{
  "for_mod_name": "YetAnotherWeaponCompleteEdition",
  "name": "YAWCE / Translation UKR",
  "author": "Translator"
}
```

**files.json:**
```json
{
  "files": [
    {
      "display_name": "YAWCE / Translation UKR",
      "versions": [
        {
          "version": "3.0.0",
          "compatibility": [
            { "version": "3.0.0", "build": "300" },
            { "version": "2.9.0", "build": "290" }
          ],
          "expected_files": { "1": "YAWCE_UKR_v3.0.0.7z" },
          "url": { "1": "https://example.com/releases/YAWCE_UKR_v3.0.0.7z" },
          "size": { "1": 204800 },
          "hash": { "1": "sha256:def456..." }
        }
      ]
    }
  ]
}
```

У цьому випадку програма перевіряє сумісність за версією та номером збірки встановленого мода з записів `compatibility`.

#### Як це працює всередині

При встановленні перекладу з каталогу:
1. `for_mod_name` зчитується з `mod.json` репозиторію.
2. `"Original_game"` перетворюється на `"Game"` та записується в `translation_requirements_mod_name` у `mod_manager_properties.json`.
3. Масив `compatibility` перетворюється на рядок `"version|build;version|build"` з розділенням крапкою з комою та записується в `translation_requirements_mod_version_build`.
4. На сторінках «Встановлені»/«Файли» програма перевіряє сумісність — для `"Game"` порівнює з `config.game_version`; для звичайних модів шукає встановлені моди за `file_name`.

> Якщо `mod_manager_properties.json` всередині архіву вже містить поля `translation_requirements_*`, значення з архіву мають пріоритет і не перезаписуються даними з репозиторію.

---

### featured.json — рекомендовані моди

Файл `featured.json` у папці категорії задає список рекомендованих модів. Вони відображаються першими в каталозі та позначаються особливим чином.

```json
["MyBestMod", "AnotherGreatMod", "EssentialTool"]
```

Значення в масиві — **імена папок** модів (для `repository`) або **імена папок** (не ID) для `nexus_api`.

> Порядок у `featured.json` — це порядок відображення в каталозі. Інші моди йдуть після рекомендованих у довільному порядку.

---

### mod_manager_properties.json

Цей файл створюється програмою в папці кожного встановленого мода. Він зберігає метадані, що зв'язують мод з його джерелом (Nexusmods, репозиторій або ручне встановлення).

**Файл керується автоматично** — він створюється та оновлюється при встановленні модів з каталогу, створенні зв'язків або оновленні модів. Автори модів також можуть включити його в свій архів для попереднього налаштування зв'язків.

> **Примітка для користувачів:** Якщо автор мода включає `mod_manager_properties.json` в архів, вам потрібно увімкнути галочку **«Копіювати mod_manager_properties.json»** на етапі завантаження архівів при встановленні. Або можна увімкнути цю галочку за замовчуванням у **Налаштуваннях**, щоб вона завжди була активна.

#### Приклад

```json
{
  "file_name": "My Awesome Mod",
  "installed_version": "2.1.0",
  "is_files_mod": false,
  "files_mod_move_to": "",
  "files_mod_backup_on_replace": true,
  "files_mod_files_moved": false,
  "files_mod_files_list": [],
  "is_nexusmods": true,
  "nexusmods_mod_id": 12345,
  "nexusmods_mod_name": "My Awesome Mod",
  "nexusmods_mod_url": "https://www.nexusmods.com/mechwarrior5mercenaries/mods/12345",
  "is_repo": false,
  "repo_url": "",
  "repo_mod_category": "",
  "repo_mod_name": "",
  "repo_file_display_name": "",
  "is_translation": false,
  "translation_requirements_mod_name": "",
  "translation_requirements_mod_version_build": ""
}
```

#### Поля

| Поле | Тип | Опис |
|---|---|---|
| `file_name` | string | Назва мода для відображення в менеджері |
| `installed_version` | string | Поточна встановлена версія |
| `is_files_mod` | bool | `true` якщо це файловий мод (без `mod.json`, файли розміщуються напряму) |
| `is_nexusmods` | bool | `true` якщо зв'язаний з модом на Nexusmods |
| `nexusmods_mod_id` | int | ID мода на Nexusmods |
| `nexusmods_mod_name` | string | Ім'я мода на Nexusmods |
| `nexusmods_mod_url` | string | Повний URL сторінки мода на Nexusmods |
| `is_repo` | bool | `true` якщо встановлений з репозиторію |
| `repo_url` | string | URL репозиторію |
| `repo_mod_category` | string | ID категорії в репозиторії (наприклад, `"1"`, `"2"`) |
| `repo_mod_name` | string | Ім'я папки мода в репозиторії |
| `repo_file_display_name` | string | `display_name` файлової групи з `files.json` (використовується для співставлення при оновленні) |
| `is_translation` | bool | `true` якщо мод є перекладом |
| `translation_requirements_mod_name` | string | Ім'я потрібного мода (`"Game"` = потрібна певна версія гри) |
| `translation_requirements_mod_version_build` | string | Пари версія\|білд через крапку з комою (наприклад, `"1.2.0\|123;1.3.0\|456"`) |
| `files_mod_move_to` | string | Цільовий шлях для розміщення файлів файлового мода |
| `files_mod_backup_on_replace` | bool | Чи створювати резервну копію файлів, що замінюються |
| `files_mod_files_moved` | bool | `true` якщо файли вже переміщено з папки файлового мода |
| `files_mod_files_list` | array | Список файлів, керованих цим файловим модом |

---

### mod_manager_install_rules.json

Цей файл може бути **включений автором мода** в архів мода. При встановленні мода програма автоматично імпортує правила в систему порядку завантаження, а потім **видаляє цей файл** з папки встановленого мода.

Це дозволяє авторам модів постачати рекомендовані правила порядку завантаження разом зі своїми модами.

#### Формат

```json
{
  "rules": [
    {
      "mod_name": "My Translation Mod",
      "mod_folder": "MyTranslationMod",
      "rule_type": "after",
      "target_name": "Original Mod",
      "target_folder": "OriginalMod"
    },
    {
      "mod_name": "My Translation Mod",
      "mod_folder": "MyTranslationMod",
      "rule_type": "last"
    }
  ]
}
```

#### Поля правила

| Поле | Тип | Обов'язковість | Опис |
|---|---|---|---|
| `mod_folder` | string | обов'язково | Папка мода, до якого застосовується правило |
| `rule_type` | string | обов'язково | Тип правила: `after`, `before`, `first`, `last` |
| `target_folder` | string | для `after`/`before` | Цільова папка мода (не потрібно для `first`/`last`) |
| `mod_name` | string | ні | Назва мода для відображення (інформаційне, не використовується програмою) |
| `target_name` | string | ні | Назва цільового мода для відображення (інформаційне, не використовується програмою) |
| `enabled` | bool | ні | Ігнорується при імпорті — всі правила завжди імпортуються як **вимкнені** |

#### Типи правил

| Тип | Опис |
|---|---|
| `after` | Мод завантажується **після** цільового мода (більший номер порядку завантаження) |
| `before` | Мод завантажується **перед** цільовим модом (менший номер порядку завантаження) |
| `first` | Мод розміщується у **першій** групі завантаження (найменший пріоритет) |
| `last` | Мод розміщується в **останній** групі завантаження (найвищий пріоритет) |

#### Як це працює

1. Автор мода розміщує `mod_manager_install_rules.json` в корені архіву мода (поряд з `mod.json`)
2. Користувач встановлює мод через програму
3. Програма читає файл правил та додає правила до глобального `mod_manager_rules.json`
4. Усі імпортовані правила додаються як **вимкнені** (користувач повинен увімкнути їх вручну)
5. Дублікати правил (збіг за `mod_folder` + `rule_type` + `target_folder`) пропускаються
6. Файл `mod_manager_install_rules.json` **видаляється** з папки встановленого мода після обробки

> **Примітка для користувачів:** Якщо автор мода включає `mod_manager_install_rules.json` в архів, вам потрібно увімкнути галочку **«Копіювати mod_manager_install_rules.json»** на етапі завантаження архівів при встановленні. Або можна увімкнути цю галочку за замовчуванням у **Налаштуваннях**, щоб вона завжди була активна.

---

### Ігровий mod.json (формат MW5)

Цей файл — стандартний дескриптор мода MechWarrior 5. Він **створюється автором мода** та включається в архів мода. Програма читає його для отримання імені мода, версії та порядку завантаження. При зміні порядку завантаження через програму оновлюється поле `defaultLoadOrder`.

**Розташування:** `<папка_модів>/<ІмʼяМода>/mod.json`

> **Важливо:** Не плутайте з `mod.json` репозиторію (описаний вище). Ігровий `mod.json` має зовсім інший формат з полями `displayName`, `buildNumber` тощо.

#### Приклад

```json
{
  "displayName": "My Awesome Mod",
  "version": "2.1.0",
  "buildNumber": 210,
  "description": "A great mod for MW5",
  "author": "ModAuthor",
  "authorURL": "https://github.com/modauthor",
  "defaultLoadOrder": 5,
  "gameVersion": "1.1.383",
  "manifest": [],
  "steamPublishedFileId": 0,
  "steamLastSubmittedBuildNumber": 0,
  "steamModVisibility": "Public"
}
```

#### Поля

| Поле | Тип | За замовчуванням | Опис |
|---|---|---|---|
| `displayName` | string | `"Unknown Mod"` | Назва мода для відображення (у грі та менеджері) |
| `version` | string | `"1.0.0"` | Версія мода |
| `buildNumber` | int | `0` | Номер збірки |
| `description` | string | `""` | Опис мода |
| `author` | string | `""` | Ім'я автора |
| `authorURL` | string | `""` | URL автора |
| `defaultLoadOrder` | int | `0` | Пріоритет порядку завантаження — керується програмою при переставленні модів |
| `gameVersion` | string | `""` | Цільова версія гри |
| `manifest` | array | `[]` | Список шляхів файлів мода |
| `steamPublishedFileId` | int | `0` | ID файлу у Steam Workshop |
| `steamLastSubmittedBuildNumber` | int | `0` | Останній надісланий до Steam номер збірки |
| `steamModVisibility` | string | `"Public"` | Видимість у Steam Workshop |

> **Примітка:** Поле `defaultLoadOrder` — основний механізм, за яким гра визначає порядок завантаження модів. Програма змінює це поле при переставленні модів на сторінці «Моди».

---

### backup.json

Автоматична **копія оригінального ігрового `mod.json`**, що створюється при першій зміні порядку завантаження мода. Зберігає вихідне значення `defaultLoadOrder` для можливості відновлення.

**Розташування:** `<папка_модів>/<ІмʼяМода>/backup.json`

Формат ідентичний ігровому `mod.json`, описаному вище. Файл створюється одноразово і більше не оновлюється.

---

### modlist.json

Зберігає стан увімкнення/вимкнення всіх модів. Цей файл читається грою для визначення активних модів.

**Розташування:** `<папка_модів>/modlist.json`

#### Приклад

```json
{
  "gameVersion": "1.1.383",
  "modStatus": {
    "MyMod": {
      "bEnabled": true
    },
    "AnotherMod": {
      "bEnabled": false
    },
    "DisabledMod": {
      "bEnabled": false
    }
  }
}
```

#### Поля

| Поле | Тип | Опис |
|---|---|---|
| `gameVersion` | string | Рядок версії гри |
| `modStatus` | object | Словник імен папок модів та їхніх статусів |
| `modStatus.<папка>.bEnabled` | bool | `true` — мод увімкнений, `false` — вимкнений |

> **Примітка:** Якщо папка мода відсутня в `modStatus`, мод вважається **увімкненим** за замовчуванням.

---

### mod_manager_rules.json

Зберігає правила порядку завантаження, налаштовані користувачем через сторінку «Правила» в програмі. Цей файл розміщується в папці модів.

**Розташування:** `<папка_модів>/mod_manager_rules.json`

#### Приклад

```json
{
  "rules_enabled": true,
  "rules": [
    {
      "mod_folder": "TranslationMod",
      "rule_type": "after",
      "target_folder": "OriginalMod",
      "enabled": true
    },
    {
      "mod_folder": "CoreFramework",
      "rule_type": "first",
      "target_folder": "",
      "enabled": true
    },
    {
      "mod_folder": "VisualOverhaul",
      "rule_type": "last",
      "target_folder": "",
      "enabled": false
    },
    {
      "mod_folder": "WeaponMod",
      "rule_type": "before",
      "target_folder": "BalanceMod",
      "enabled": true
    }
  ]
}
```

#### Поля верхнього рівня

| Поле | Тип | За замовчуванням | Опис |
|---|---|---|---|
| `rules_enabled` | bool | `true` | Глобальний перемикач системи правил. Коли `false`, всі правила ігноруються |
| `rules` | array | `[]` | Масив правил порядку завантаження |

#### Поля правила

| Поле | Тип | Опис |
|---|---|---|
| `mod_folder` | string | Ім'я папки мода, до якого застосовується правило |
| `rule_type` | string | Тип правила (див. таблицю нижче) |
| `target_folder` | string | Цільова папка мода (для `after`/`before`; порожньо для `first`/`last`) |
| `enabled` | bool | Чи активне дане правило |

#### Типи правил

| Тип | Опис |
|---|---|
| `after` | Мод завантажується **після** цільового мода (більший номер порядку завантаження) |
| `before` | Мод завантажується **перед** цільовим модом (менший номер порядку завантаження) |
| `first` | Мод розміщується у **першій** групі завантаження (найменший пріоритет) |
| `last` | Мод розміщується в **останній** групі завантаження (найвищий пріоритет) |

---

### Файли стану завантаження

Тимчасові файли, що відстежують прогрес завантаження для відновлюваних скачувань. Створюються при завантаженні архівів модів та видаляються після успішного завершення.

**Розташування:** `<папка_архівів>/<ім'я_файлу>.download_state.json`

#### Приклад

```json
{
  "url": "https://example.com/releases/MyMod_v2.0.7z",
  "filename": "MyMod_v2.0.7z",
  "total_bytes": 5242880,
  "downloaded_bytes": 2621440,
  "expected_md5": "d41d8cd98f00b204e9800998ecf8427e"
}
```

#### Поля

| Поле | Тип | Опис |
|---|---|---|
| `url` | string | URL завантаження |
| `filename` | string | Ім'я цільового файлу |
| `total_bytes` | int | Загальний розмір файлу в байтах |
| `downloaded_bytes` | int | Завантажено байтів на даний момент |
| `expected_md5` | string/null | Очікуваний MD5-хеш для перевірки (може бути `null`) |

> Ці файли автоматично видаляються після успішного завантаження. При перериванні завантаження файл стану дозволяє програмі відновити скачування з того місця, де воно було перервано.

---

### config.json

Основний файл конфігурації додатку. Зберігає всі налаштування користувача, стан вікна та список репозиторіїв.

**Розташування:** `config/config.json`

#### Приклад

```json
{
  "game_folder": "D:/Games/Steam/steamapps/common/MechWarrior 5 Mercenaries",
  "mods_folder": "D:/Games/Steam/steamapps/common/MechWarrior 5 Mercenaries/MW5Mercs/Mods",
  "steam_mods_folder": "D:/Games/Steam/steamapps/workshop/content/784080",
  "game_version": "1.1.383",
  "language": "uk",
  "check_nexusmods_updates": true,
  "check_repo_updates": true,
  "close_on_launch": false,
  "copy_mod_rules": false,
  "copy_mod_properties": false,
  "archives_folder": "data/downloads",
  "card_styles": {},
  "panel_position_mods": "right",
  "panel_position_catalog": "right",
  "conflict_display": "conflicts_tab",
  "repositories": [
    {
      "name": "Community Repository",
      "url": "https://raw.githubusercontent.com/user/mw5-repo/main",
      "enabled": true
    }
  ],
  "window_width": 1280,
  "window_height": 720,
  "window_x": 100,
  "window_y": 100,
  "window_maximized": false,
  "first_run": false
}
```

#### Поля

| Поле | Тип | За замовчуванням | Опис |
|---|---|---|---|
| `game_folder` | string | `""` | Шлях до папки встановлення гри |
| `mods_folder` | string | `""` | Шлях до папки модів (зазвичай `<game_folder>/MW5Mercs/Mods`) |
| `steam_mods_folder` | string | `""` | Шлях до папки модів Steam Workshop (опціонально) |
| `game_version` | string | `""` | Версія гри (вводиться користувачем вручну) |
| `language` | string | `"en"` | Код мови інтерфейсу (`"en"`, `"ru"`, `"uk"`) |
| `check_nexusmods_updates` | bool | `true` | Перевіряти оновлення Nexusmods при запуску |
| `check_repo_updates` | bool | `true` | Перевіряти оновлення репозиторіїв при запуску |
| `close_on_launch` | bool | `false` | Закривати додаток при запуску гри |
| `copy_mod_rules` | bool | `false` | Стан за замовчуванням чекбоксу «Копіювати правила мода» на сторінці завантаження |
| `copy_mod_properties` | bool | `false` | Стан за замовчуванням чекбоксу «Копіювати властивості мода» на сторінці завантаження |
| `archives_folder` | string | `"data/downloads"` | Папка для завантажених архівів |
| `card_styles` | object | `{}` | Користувацькі перевизначення кольорів карток |
| `panel_position_mods` | string | `"right"` | Позиція панелі інформації на сторінці модів (`"left"` або `"right"`) |
| `panel_position_catalog` | string | `"right"` | Позиція панелі інформації на сторінці каталогу (`"left"` або `"right"`) |
| `conflict_display` | string | `"conflicts_tab"` | Режим відображення конфліктів: `"always"` або `"conflicts_tab"` |
| `repositories` | array | `[]` | Список налаштованих репозиторіїв (див. нижче) |
| `window_width` | int | `1280` | Ширина вікна в пікселях |
| `window_height` | int | `720` | Висота вікна в пікселях |
| `window_x` | int | `100` | Позиція вікна X |
| `window_y` | int | `100` | Позиція вікна Y |
| `window_maximized` | bool | `false` | Чи розгорнуте вікно на весь екран |
| `first_run` | bool | `true` | Прапорець першого запуску (запускає майстер налаштування) |

#### Поля запису репозиторію

| Поле | Тип | За замовчуванням | Опис |
|---|---|---|---|
| `name` | string | `""` | Назва репозиторію для відображення |
| `url` | string | `""` | URL або локальний шлях до кореня репозиторію |
| `enabled` | bool | `true` | Чи активний репозиторій |

---

### Модпаки

Модпаки зберігають знімок конфігурації модів користувача для обміну або відновлення.

**Розташування:** `config/modpacks/<ім'я>.json`

#### Приклад

```json
{
  "name": "My Battle Setup",
  "mods": [
    {
      "folder_name": "WeaponPack",
      "display_name": "Yet Another Weapon",
      "version": "26.0",
      "author": "Author",
      "is_installed": true,
      "is_translation": false,
      "source_type": "nexusmods",
      "nexusmods_mod_id": 1080,
      "nexusmods_mod_name": "Yet Another Weapon",
      "installed_version": "26.0",
      "is_nexusmods_linked": true,
      "is_repo_linked": false
    }
  ],
  "mods_preset": ["1"],
  "rules_preset": ["2"],
  "repositories": ["https://raw.githubusercontent.com/user/mw5-repo/main"],
  "mods_preset_data": {},
  "rules_preset_data": {}
}
```

#### Поля

| Поле | Тип | Опис |
|---|---|---|
| `name` | string | Назва модпаку для відображення |
| `mods` | array | Список записів модів з метаданими |
| `mods_preset` | array | Імена зв'язаних пресетів модів |
| `rules_preset` | array | Імена зв'язаних пресетів правил |
| `repositories` | array | URL-адреси репозиторіїв, що використовуються цим модпаком |
| `mods_preset_data` | object | Вбудовані дані пресетів модів (для обміну) |
| `rules_preset_data` | object | Вбудовані дані пресетів правил (для обміну) |

#### Поля запису мода

| Поле | Тип | Опис |
|---|---|---|
| `folder_name` | string | Ім'я папки мода |
| `display_name` | string | Назва мода для відображення |
| `version` | string | Версія мода |
| `author` | string | Автор мода |
| `is_installed` | bool | Чи був мод встановлений на момент створення модпаку |
| `is_translation` | bool | Чи є мод перекладом |
| `source_type` | string | Тип джерела (наприклад, `"nexusmods"`, `"repository"`) |
| `nexusmods_mod_id` | int | ID мода на Nexusmods (якщо прив'язаний) |
| `nexusmods_mod_name` | string | Ім'я мода на Nexusmods (якщо прив'язаний) |
| `installed_version` | string | Встановлена версія на момент створення |
| `is_nexusmods_linked` | bool | Чи прив'язаний мод до Nexusmods |
| `is_repo_linked` | bool | Чи прив'язаний мод до репозиторію |

---

### Пресети

Пресети зберігають та відновлюють конфігурації порядку модів та правил незалежно одне від одного.

#### Пресети модів

**Розташування:** `config/presets/mods/<ім'я>.json`

Зберігає стан увімкнення та порядок завантаження всіх модів.

```json
{
  "MyPreset": {
    "mods": {
      "CoreFramework": {
        "bEnabled": true,
        "defaultLoadOrder": 1
      },
      "WeaponPack": {
        "bEnabled": true,
        "defaultLoadOrder": 2
      },
      "VisualMod": {
        "bEnabled": false,
        "defaultLoadOrder": 3
      }
    }
  }
}
```

| Поле | Тип | Опис |
|---|---|---|
| `<ім'я_пресету>.mods` | object | Словник імен папок модів та їхніх станів |
| `<ім'я_пресету>.mods.<папка>.bEnabled` | bool | Чи увімкнений мод |
| `<ім'я_пресету>.mods.<папка>.defaultLoadOrder` | int | Позиція в порядку завантаження |

#### Пресети правил

**Розташування:** `config/presets/rules/<ім'я>.json`

Зберігає повну конфігурацію правил.

```json
{
  "MyRulesPreset": {
    "rules_enabled": true,
    "rules": [
      {
        "mod_folder": "TranslationMod",
        "rule_type": "after",
        "target_folder": "OriginalMod",
        "enabled": true
      },
      {
        "mod_folder": "CoreFramework",
        "rule_type": "first",
        "enabled": true
      }
    ]
  }
}
```

| Поле | Тип | Опис |
|---|---|---|
| `<ім'я_пресету>.rules_enabled` | bool | Глобальний перемикач системи правил |
| `<ім'я_пресету>.rules` | array | Масив правил (формат ідентичний `mod_manager_rules.json`) |

> **Примітка:** Поле `target_folder` додається тільки для правил типу `after`/`before`.

---

### mod_manager_backup.json

Повний файл резервної копії додатку для експорту/імпорту всіх налаштувань, пресетів та правил.

**Розташування:** Шлях обирається користувачем (ім'я за замовчуванням: `mod_manager_backup.json`)

#### Приклад

```json
{
  "config": {
    "game_folder": "D:/Games/...",
    "language": "uk",
    "repositories": [
      { "name": "My Repo", "url": "https://...", "enabled": true }
    ]
  },
  "presets_mods": {
    "1.json": { "1": { "mods": { "ModA": { "bEnabled": true, "defaultLoadOrder": 1 } } } }
  },
  "presets_rules": {
    "1.json": { "1": { "rules_enabled": true, "rules": [] } }
  }
}
```

#### Поля

| Поле | Тип | Опис |
|---|---|---|
| `config` | object | Повний вміст `config.json` |
| `presets_mods` | object | Всі пресети модів (ключ = ім'я файлу включаючи `.json`) |
| `presets_rules` | object | Всі пресети правил (ключ = ім'я файлу включаючи `.json`) |

> Цей файл створюється через **Налаштування → Експорт резервної копії** та відновлюється через **Налаштування → Імпорт резервної копії**. Імпорт перезаписує поточну конфігурацію та всі пресети.

---

### Приклад багатофайлового завантаження

Коли архів мода розділений на кілька файлів (наприклад, через обмеження розміру), використовуйте нумеровані ключі в `expected_files`, `url`, `size` та `hash`:

```json
{
  "versions": [
    {
      "version": "2.2",
      "category": "MAIN",
      "description": "Повний мод (3 частини)",
      "expected_files": {
        "1": "MyMod_Part1.7z",
        "2": "MyMod_Part2.7z",
        "3": "MyMod_Part3.7z"
      },
      "url": {
        "1": "https://example.com/releases/MyMod_Part1.7z",
        "2": "https://example.com/releases/MyMod_Part2.7z",
        "3": "https://example.com/releases/MyMod_Part3.7z"
      },
      "size": {
        "1": 1048576000,
        "2": 729978606,
        "3": 524288000
      },
      "hash": {
        "1": "sha256:aaa111...",
        "2": "sha256:bbb222...",
        "3": "sha256:ccc333..."
      }
    }
  ]
}
```

Програма завантажує всі частини послідовно, перевіряючи хеш кожного файлу за його наявності. Потім всі частини видобуваються в папку мода.

---

### Повний приклад репозиторію

```
my-mw5-repo/
├── repository.json
├── early_access_mods/
│   ├── featured.json
│   ├── WeaponPack/
│   │   ├── mod.json
│   │   ├── description.md
│   │   ├── files.json
│   │   ├── requirements.json
│   │   ├── changelog.json
│   │   └── preview.png
│   └── BalanceMod/
│       ├── mod.json
│       └── files.json
├── early_access_translations/
│   ├── featured.json
│   └── RussianTranslation/
│       ├── mod.json
│       └── description.md
├── nexusmods_mods/
│   ├── featured.json
│   └── 12345/
│       └── nexusmods_id.json
└── nexusmods_translations/
    ├── featured.json
    └── 67890/
        └── nexusmods_id.json
```

---

### Публікація репозиторію

#### GitHub / GitLab / Codeberg / Bitbucket / Gitea / Forgejo

Розмістіть папку репозиторію у публічному git-репозиторії. Програма звертається до raw-файлів напряму.

Програма **автоматично конвертує** web-URL у raw URL для таких платформ:

| Платформа | Користувач вводить | Програма конвертує в |
|---|---|---|
| GitHub | `https://github.com/user/repo` | `https://raw.githubusercontent.com/user/repo/main` |
| GitLab | `https://gitlab.com/user/repo` | `https://gitlab.com/user/repo/-/raw/main` |
| Codeberg | `https://codeberg.org/user/repo` | `https://codeberg.org/user/repo/raw/branch/main` |
| Bitbucket | `https://bitbucket.org/user/repo` | `https://bitbucket.org/user/repo/raw/main` |
| Gitea (власний сервер) | `https://gitea.example.com/user/repo/src/branch/main` | `https://gitea.example.com/user/repo/raw/branch/main` |

> **Примітка:** Якщо гілка `main` не знайдена, програма також спробує `master`. Можна вказати гілку явно, напр.: `https://github.com/user/repo/tree/dev`.

> **Самостійний Gitea/Forgejo:** Програма не може автовизначити користувацькі домени. Використовуйте URL з `/src/branch/...` для автоконвертації або вкажіть raw URL напряму: `https://gitea.example.com/user/repo/raw/branch/main`.

**Приклад URL для Forgejo:**
```
http://192.168.3.10:7205/username/mw5-repo/raw/branch/main
```

#### Статичний HTTP-сервер

Будь-який сервер, що віддає файли за прямими URL. Nginx, Apache, Caddy, GitHub Pages тощо.

#### Локальний шлях (для тестування)

```
D:\MyMods\TestRepository
```
або
```
/home/user/mw5-repo
```

---

### Зауваження для розробників репозиторію

1. **Імена папок** модів не повинні змінюватися після публікації — користувачі втратять зв'язок зі встановленими модами.
2. **Посилання на файли** в `url` повинні бути прямими (без редиректів та авторизації). GitHub Releases надає прямі raw-посилання.
3. **Кодування** всіх JSON та Markdown файлів — UTF-8.
4. **`is_translation`** важливий: переклади відображаються окремо від основних модів в інтерфейсі.
5. Поле `name` у категорії може бути будь-яким рядком — програма використовує його як внутрішній ідентифікатор і слідує за шляхом, вказаним у `path` (або за `name`, якщо `path` не задано).
6. Версії в масиві `versions` кожної файлової групи можуть розміщуватися в **будь-якому порядку** — програма автоматично визначає актуальну версію, порівнюючи рядки версій за семантичним версіонуванням.

---

## Інструменти

### repo_file_info.py — генератор розмірів та хешів файлів

Допоміжний скрипт у папці `tools/`, який генерує розміри файлів та SHA-256 хеші для архівів репозиторію. Результат можна використовувати для заповнення полів `size` та `hash` у `files.json` / `mod.json`.

Інструмент має два режими:
- **Інтерактивний** — запуск без аргументів (або через `repo_file_info.bat`). Скрипт покроково проведе через вибір папки, режиму сканування та формату виводу, а потім збереже результат у файл.
- **CLI** — передача шляху та прапорців як аргументів командного рядка.

#### Швидкий старт (Windows)

Двічі клікніть `tools/repo_file_info.bat` — запуститься інтерактивний майстер.

#### Кроки інтерактивного режиму

1. **Вибір папки** — через діалог провідника або введення шляху вручну
2. **Режим сканування** — всі файли або тільки архіви (`.7z`, `.zip`, `.rar`, ...)
3. **Рекурсія** — сканувати підпапки чи ні
4. **Формат виводу** — текстова таблиця, JSON одиночний або JSON мульти-файл
5. **URL-префікс** — опціональний префікс для посилань завантаження (тільки JSON)
6. **Результат** — виводиться в консоль та зберігається у файл поруч зі сканованою папкою

#### Використання CLI

```bash
python tools/repo_file_info.py <шлях> [опції]
```

#### Опції CLI

| Прапорець | Опис |
|---|---|
| `--json` | Вивід у форматі JSON-сніпету для `files.json` |
| `--multi` | Багатофайловий режим: групування всіх файлів в один запис версії з нумерованими ключами (`url_2`, `size_2` тощо) |
| `--recursive`, `-r` | Рекурсивне сканування підкаталогів |
| `--archives-only`, `-a` | Тільки архівні файли (`.7z`, `.zip`, `.rar` тощо) |
| `--url-prefix <url>` | Префікс URL для посилань завантаження у JSON-виводі |
| `--save`, `-s` | Зберегти результат у файл поруч зі сканованою папкою |

#### Приклади CLI

```bash
# Сканування одного архіву
python tools/repo_file_info.py "D:/releases/MyMod_v2.0.7z"

# Сканування папки з JSON-виводом
python tools/repo_file_info.py "D:/releases/" --json

# Рекурсивне сканування, тільки архіви, з URL-префіксом, збереження у файл
python tools/repo_file_info.py "D:/releases/" --recursive --archives-only --json \
  --url-prefix "https://github.com/user/repo/releases/download/v1.0/" --save

# Багатофайловий режим (кілька архівів в одному записі версії)
python tools/repo_file_info.py "D:/releases/" --json --multi
```
