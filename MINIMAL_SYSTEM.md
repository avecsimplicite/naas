# Minimal Sheet Template System

This is a reusable system to generate `minimal.html` files for different groups. Each group connects to its own Google Sheet and can be deployed independently.

## System Structure

```
naas/
├── groups.config.json           # Configuration for all groups
├── minimal.template.html         # Base template with placeholders
├── generate_minimal.py           # Generator script
├── o_static/                     # NAAS output folder
│   └── minimal.html             # Generated for NAAS
├── onqt_static/                 # ONQT output folder (example)
│   └── minimal.html             # Generated for ONQT
└── MINIMAL_SYSTEM.md            # This file
```

## Adding a New Group

### ⭐ RECOMMENDED: Interactive Setup (Easiest)

Just run the interactive setup script - it handles everything!

```bash
python setup_new_group.py
```

The script will:
1. ✅ Ask for group name
2. ✅ Ask for display name
3. ✅ Ask for Google Sheet URL (validates it's published)
4. ✅ Ask for group website URL
5. ✅ Generate `minimal.html` automatically
6. ✅ Update `groups.config.json`
7. ✅ Commit and push to main
8. ✅ Show you the final deployed URL

**Example interaction:**
```
🚀 New Group Setup
──────────────────
Group name (lowercase, e.g., 'mycommunity'): mycommunity
Group display name (e.g., 'My Community'): My Community
Google Sheet URL: https://docs.google.com/spreadsheets/d/e/2PACX-1v.../pub?gid=123456&single=true
Group website URL (e.g., 'https://mygroup.example.com'): https://mycommunity.example.com

✅ Updated groups.config.json
✅ Generated mycommunity_static/minimal.html
✅ Committed and pushed to main

✨ mycommunity is ready!
Live URL: https://avecsimplicite.github.io/naas/mycommunity_static/minimal.html
```

---

### Alternative: Manual Configuration

If you prefer manual control, you can edit files directly:

#### Step 1: Update Configuration

Edit `groups.config.json` and add your group:

```json
{
  "groups": {
    "yourgroup": {
      "name": "Your Group Name",
      "description": "Description",
      "googleSheetUrl": "https://docs.google.com/spreadsheets/d/e/YOUR_SHEET_ID/pub?gid=YOUR_GID&single=true&",
      "groupSiteUrl": "https://yourgroup.example.com",
      "outputFolder": "yourgroup_static",
      "filename": "minimal.html",
      "downloadName": "yourgroup_data"
    }
  }
}
```

**Important**:
- `googleSheetUrl` must be a **published** Google Sheet URL (File > Share > Publish to web)
- Include the `&` at the end so the script can add `output=csv`
- `outputFolder` should follow the pattern `{groupname}_static`

#### Step 2: Generate the HTML

```bash
# Generate all groups
python generate_minimal.py

# Generate specific group
python generate_minimal.py yourgroup

# Generate multiple groups
python generate_minimal.py naas onqt yourgroup
```

The script will:
- ✅ Validate configuration
- ✅ Replace all placeholders in the template
- ✅ Create output folders if needed
- ✅ Write `minimal.html` files

#### Step 3: Deploy

Commit and push your changes:
```bash
git add groups.config.json yourgroup_static/minimal.html
git commit -m "Add yourgroup to minimal.html system"
git push
```

Each group's HTML file is in its own folder and ready to be served:
- NAAS: `o_static/minimal.html`
- ONQT: `onqt_static/minimal.html`
- Your Group: `yourgroup_static/minimal.html`

## How It Works

### Template Placeholders

The template (`minimal.template.html`) contains these replaceable placeholders:

| Placeholder | What it becomes | Example |
|-----------|---|---|
| `{{GROUP_NAME}}` | Group name | NAAS, ONQT |
| `{{GOOGLE_SHEET_URL}}` | Published sheet URL | `https://docs.google.com/spreadsheets/d/e/...` |
| `{{GROUP_SITE_URL}}` | Link for "Back to group" button | `https://sites.google.com/jgwill.com/serviteur/accueil` |
| `{{DOWNLOAD_NAME}}` | Part of downloaded filename | `postemensuels`, `publications_onqt` |

### What Each Generated HTML Does

1. **Auto-loads on page open** - Fetches the Google Sheet and displays table
2. **Shows loading spinner** - While fetching data
3. **Displays table** - With all data from the sheet
4. **Download button** - Converts table to PNG with date prefix
5. **Group link button** - Returns to group's website
6. **Fallback methods** - Tries multiple ways to fetch data (direct, proxy, Google Visualization API)

## File Organization by Group

Each group keeps its own folder structure:
```
{groupname}_static/
└── minimal.html        # Generated file, ready to publish
```

This makes it easy to:
- Deploy each group independently
- Version control separately
- Update one group without affecting others

## Troubleshooting

### "Missing or incomplete config"
- Check that your Google Sheet URL doesn't start with `YOUR_`
- Verify the URL is properly formatted
- Make sure `groupSiteUrl` is filled in

### HTML file not generated
- Ensure `groups.config.json` is valid JSON
- Check that the output folder name is writable
- Run `python generate_minimal.py <groupname>` to see specific errors

### Sheet not loading in browser
- Verify the Google Sheet is published (File > Share > Publish to web)
- Check that the URL in config matches the published URL
- Open browser console to see specific error messages

## Updating the Template

If you want to improve the core template (styling, features, etc.):

1. Edit `minimal.template.html`
2. Keep all `{{PLACEHOLDERS}}` intact
3. Regenerate all groups: `python generate_minimal.py`

All groups will get the improvements automatically!

## Example: Publishing NAAS and ONQT

```bash
# Configure both
# (edit groups.config.json with real URLs)

# Generate both
python generate_minimal.py naas onqt

# Commit and push
git add groups.config.json o_static/minimal.html onqt_static/minimal.html
git commit -m "Generate minimal.html for NAAS and ONQT"
git push

# Each group's HTML is now ready at:
# - https://avecsimplicite.github.io/naas/o_static/minimal.html
# - https://avecsimplicite.github.io/naas/onqt_static/minimal.html
```
