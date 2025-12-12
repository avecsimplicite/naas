
from playwright.sync_api import sync_playwright
from datetime import datetime

URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRnl8-YerEduI_wn45FLg36yEr2_na23Hrlk-txjYKuz5DxABxZcnuKxsNiqYNcMv3ulGEPveEKiAtP/pub?gid=665461249&single=true&"

def capture_sheet_table(url: str):
    # Generate filename with current date
    today = datetime.now().strftime("%Y-%m-%d")
    output_file = f"{today}_postemensuels.png"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Use a larger viewport to capture the full content
        page = browser.new_page(viewport={"width": 1600, "height": 1200})

        # Load the page and wait for network to be mostly idle
        page.goto(url, wait_until="networkidle")

        # Wait a bit more for any dynamic content to settle
        page.wait_for_timeout(2000)

        # Find and capture the iframe
        iframe = page.locator("iframe").first
        iframe.wait_for(state="visible", timeout=15000)

        # Get the iframe's bounding box to capture it
        box = iframe.bounding_box()
        if box:
            print(f"Iframe dimensions: {box['width']}x{box['height']}")

        # Screenshot the iframe
        iframe.screenshot(path=output_file, type="png")

        browser.close()

        return output_file

output_file = capture_sheet_table(URL)
print(f"Saved screenshot to: {output_file}")
