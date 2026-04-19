#!/usr/bin/env python3
"""
Interactive script to add a new group to the reusable minimal.html system.

This script:
1. Asks for group information
2. Validates all inputs
3. Generates minimal.html from template
4. Updates groups.config.json
5. Commits and pushes to main automatically

Usage:
    python setup_new_group.py
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse


class Colors:
    """ANSI color codes for terminal output"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_header(text):
    """Print styled header"""
    print(f"\n{Colors.BOLD}{Colors.HEADER}🚀 {text}{Colors.ENDC}\n")


def print_success(text):
    """Print success message"""
    print(f"{Colors.OKGREEN}✅ {text}{Colors.ENDC}")


def print_error(text):
    """Print error message"""
    print(f"{Colors.FAIL}❌ {text}{Colors.ENDC}")


def print_warning(text):
    """Print warning message"""
    print(f"{Colors.WARNING}⚠️  {text}{Colors.ENDC}")


def print_info(text):
    """Print info message"""
    print(f"{Colors.OKCYAN}ℹ️  {text}{Colors.ENDC}")


def prompt(question, default=""):
    """Prompt user for input with optional default"""
    if default:
        prompt_text = f"{question} [{default}]: "
    else:
        prompt_text = f"{question}: "

    answer = input(prompt_text).strip()
    return answer if answer else default


def validate_group_name(name):
    """Validate group name format (lowercase, alphanumeric, hyphens)"""
    if not re.match(r'^[a-z0-9\-]+$', name):
        print_error("Group name must be lowercase, alphanumeric, and hyphens only")
        return False
    if name.startswith('-') or name.endswith('-'):
        print_error("Group name cannot start or end with a hyphen")
        return False
    return True


def validate_display_name(name):
    """Validate display name (not empty)"""
    if not name or len(name.strip()) == 0:
        print_error("Display name cannot be empty")
        return False
    return True


def validate_url(url, url_type="Google Sheet"):
    """Validate URL format"""
    try:
        result = urlparse(url)
        is_valid = all([result.scheme, result.netloc])

        if not is_valid:
            print_error(f"Invalid {url_type} URL format")
            return False

        # Additional checks for Google Sheet URLs
        if "google" in url.lower() and "spreadsheets" in url.lower():
            if "pub" not in url.lower():
                print_warning(f"Google Sheet URL might not be published. Make sure it contains '/pub?'")
            if "&" not in url:
                print_warning(f"Google Sheet URL should end with '&' so we can add query parameters")

        return True
    except Exception as e:
        print_error(f"Invalid URL: {e}")
        return False


def load_config():
    """Load configuration from groups.config.json"""
    config_path = Path(__file__).parent / 'groups.config.json'
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print_error(f"Failed to load groups.config.json: {e}")
        sys.exit(1)


def save_config(config):
    """Save configuration to groups.config.json"""
    config_path = Path(__file__).parent / 'groups.config.json'
    try:
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
        return True
    except Exception as e:
        print_error(f"Failed to save groups.config.json: {e}")
        return False


def load_template():
    """Load HTML template"""
    template_path = Path(__file__).parent / 'minimal.template.html'
    try:
        with open(template_path, 'r') as f:
            return f.read()
    except Exception as e:
        print_error(f"Failed to load template: {e}")
        sys.exit(1)


def generate_html(group_config, template):
    """Generate HTML from template"""
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


def create_output_folder(folder_name):
    """Create output folder if it doesn't exist"""
    folder_path = Path(__file__).parent / folder_name
    try:
        folder_path.mkdir(parents=True, exist_ok=True)
        return folder_path
    except Exception as e:
        print_error(f"Failed to create folder: {e}")
        return None


def write_html_file(folder_path, html_content):
    """Write HTML file to folder"""
    file_path = folder_path / 'minimal.html'
    try:
        with open(file_path, 'w') as f:
            f.write(html_content)
        return file_path
    except Exception as e:
        print_error(f"Failed to write HTML file: {e}")
        return None


def git_commit_and_push(group_name, folder_name):
    """Commit and push changes to git"""
    try:
        # Stage files
        subprocess.run(['git', 'add', 'groups.config.json', f'{folder_name}/minimal.html'],
                      check=True, capture_output=True)

        # Commit
        commit_msg = f"""Enhancement #X: Add "{group_name}" group to minimal.html system

- Configure {group_name} in groups.config.json
- Generate {folder_name}/minimal.html from template
- Ready for deployment

🤖 Generated with Claude Code

Co-Authored-By: Claude <noreply@anthropic.com>"""

        subprocess.run(['git', 'commit', '-m', commit_msg],
                      check=True, capture_output=True)

        # Push to current branch
        result = subprocess.run(['git', 'push'], capture_output=True, text=True)

        if result.returncode == 0:
            return True
        else:
            print_warning(f"Git push output: {result.stderr}")
            return False

    except subprocess.CalledProcessError as e:
        print_error(f"Git operation failed: {e}")
        return False


def get_deployed_url(folder_name):
    """Generate the deployed URL for the group"""
    # Assuming GitHub Pages deployment to avecsimplicite/naas
    return f"https://avecsimplicite.github.io/naas/{folder_name}/minimal.html"


def main():
    print_header("New Group Setup - Reusable minimal.html System")
    print_info("This script will guide you through adding a new group.")
    print_info("Make sure you have git configured and are ready to push.")

    # Step 1: Get group name
    print("\n" + "─" * 50)
    while True:
        group_name = prompt("Group name (lowercase, e.g., 'mycommunity')")
        if validate_group_name(group_name):
            break
        print()

    # Check if group already exists
    config = load_config()
    if group_name in config['groups']:
        print_error(f"Group '{group_name}' already exists!")
        sys.exit(1)

    # Step 2: Get display name
    while True:
        display_name = prompt("Group display name (e.g., 'My Community')")
        if validate_display_name(display_name):
            break
        print()

    # Step 3: Get Google Sheet URL
    print()
    print_info("Please provide the PUBLISHED Google Sheet URL.")
    print_info("Instructions: File → Share → Publish to web → Copy the URL")
    while True:
        sheet_url = prompt("Google Sheet URL")
        if validate_url(sheet_url, "Google Sheet"):
            # Ensure URL ends with &
            if not sheet_url.endswith('&'):
                sheet_url = sheet_url.rstrip('?') + '&'
            break
        print()

    # Step 4: Get group website URL
    while True:
        group_url = prompt("Group website URL (e.g., 'https://mygroup.example.com')")
        if validate_url(group_url, "Group website"):
            break
        print()

    # Step 5: Generate download name
    download_name = group_name.replace('-', '_')
    custom_name = prompt("Download filename prefix (auto-generated)", download_name)
    if custom_name:
        download_name = custom_name

    # Summary
    print("\n" + "─" * 50)
    print_info("Review your configuration:")
    print(f"  Group name:        {Colors.BOLD}{group_name}{Colors.ENDC}")
    print(f"  Display name:      {Colors.BOLD}{display_name}{Colors.ENDC}")
    print(f"  Sheet URL:         {Colors.BOLD}{sheet_url[:50]}...{Colors.ENDC}")
    print(f"  Group website:     {Colors.BOLD}{group_url}{Colors.ENDC}")
    print(f"  Download name:     {Colors.BOLD}{download_name}{Colors.ENDC}")
    print(f"  Output folder:     {Colors.BOLD}{group_name}_static/{Colors.ENDC}")

    proceed = prompt("\nProceed with setup? (yes/no)", "yes")
    if proceed.lower() not in ['yes', 'y']:
        print_error("Setup cancelled.")
        sys.exit(0)

    # Step 6: Update configuration
    print("\n" + "─" * 50)
    print_info("Setting up group...")

    group_config = {
        "name": display_name,
        "description": f"Publications for {display_name}",
        "googleSheetUrl": sheet_url,
        "groupSiteUrl": group_url,
        "outputFolder": f"{group_name}_static",
        "filename": "minimal.html",
        "downloadName": download_name
    }

    config['groups'][group_name] = group_config

    if not save_config(config):
        sys.exit(1)
    print_success("Updated groups.config.json")

    # Step 7: Generate HTML
    template = load_template()
    html_content = generate_html(group_config, template)

    folder_path = create_output_folder(group_config['outputFolder'])
    if not folder_path:
        sys.exit(1)

    html_file = write_html_file(folder_path, html_content)
    if not html_file:
        sys.exit(1)
    print_success(f"Generated {html_file}")

    # Step 8: Commit and push
    print_info("Committing and pushing to main...")
    if git_commit_and_push(group_name, group_config['outputFolder']):
        print_success("Committed and pushed to main")
    else:
        print_warning("Could not auto-push. Please run: git push")

    # Final summary
    print("\n" + "─" * 50)
    print_header(f"✨ {group_name} is ready!")
    deployed_url = get_deployed_url(group_config['outputFolder'])
    print(f"Live URL: {Colors.BOLD}{deployed_url}{Colors.ENDC}")
    print(f"\nThe page will be available shortly after GitHub Pages rebuilds.")
    print(f"Check: https://github.com/avecsimplicite/naas/deployments")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print_error("Setup cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print_error(f"Unexpected error: {e}")
        sys.exit(1)
