#!/usr/bin/env python3
"""
Generator script to create minimal.html files for different groups.

Usage:
    python generate_minimal.py                  # Generate all groups
    python generate_minimal.py naas            # Generate specific group
    python generate_minimal.py naas onqt       # Generate multiple groups
"""

import json
import os
import sys
from pathlib import Path

def load_config():
    """Load group configuration from groups.config.json"""
    config_path = Path(__file__).parent / 'groups.config.json'
    with open(config_path, 'r') as f:
        return json.load(f)

def load_template():
    """Load the HTML template"""
    template_path = Path(__file__).parent / 'minimal.template.html'
    with open(template_path, 'r') as f:
        return f.read()

def generate_html(group_config, template):
    """Generate HTML by replacing placeholders in template"""
    html = template

    replacements = {
        '{{GROUP_NAME}}': group_config['name'],
        '{{GOOGLE_SHEET_URL}}': group_config['googleSheetUrl'],
        '{{GROUP_SITE_URL}}': group_config['groupSiteUrl'],
        '{{DOWNLOAD_NAME}}': group_config['downloadName'],
    }

    for placeholder, value in replacements.items():
        html = html.replace(placeholder, value)

    return html

def ensure_directory(dir_path):
    """Ensure directory exists"""
    Path(dir_path).mkdir(parents=True, exist_ok=True)

def generate_group(group_name, group_config, template):
    """Generate HTML file for a specific group"""

    # Validate configuration
    required_fields = ['googleSheetUrl', 'groupSiteUrl', 'outputFolder', 'filename', 'downloadName']
    missing = [f for f in required_fields if f not in group_config or group_config[f].startswith('YOUR_')]

    if missing:
        print(f"❌ {group_name}: Missing or incomplete config: {', '.join(missing)}")
        return False

    # Generate HTML
    html = generate_html(group_config, template)

    # Ensure output directory exists
    output_folder = Path(__file__).parent / group_config['outputFolder']
    ensure_directory(output_folder)

    # Write file
    output_path = output_folder / group_config['filename']
    with open(output_path, 'w') as f:
        f.write(html)

    print(f"✅ {group_name}: Generated {output_path}")
    return True

def main():
    config = load_config()
    template = load_template()

    # Determine which groups to generate
    if len(sys.argv) > 1:
        requested_groups = sys.argv[1:]
    else:
        requested_groups = list(config['groups'].keys())

    # Generate selected groups
    success_count = 0
    for group_name in requested_groups:
        if group_name not in config['groups']:
            print(f"❌ Unknown group: {group_name}")
            continue

        if generate_group(group_name, config['groups'][group_name], template):
            success_count += 1

    print(f"\n✓ Generated {success_count}/{len(requested_groups)} files")
    return 0 if success_count == len(requested_groups) else 1

if __name__ == '__main__':
    sys.exit(main())
