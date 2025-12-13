
from playwright.sync_api import sync_playwright
from datetime import datetime

URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRnl8-YerEduI_wn45FLg36yEr2_na23Hrlk-txjYKuz5DxABxZcnuKxsNiqYNcMv3ulGEPveEKiAtP/pub?gid=665461249&single=true&"

def capture_sheet_table(url: str, table_only: bool = True):
    """
    Capture a Google Sheets table with improved clarity.

    Args:
        url (str): Public Google Sheets URL
        table_only (bool): If True, captures only the table area. If False, captures entire iframe.

    Returns:
        str: Path to generated PNG file
    """
    # Generate filename with current date
    today = datetime.now().strftime("%Y-%m-%d")
    output_file = f"{today}_postemensuels.png"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Use a smaller, more focused viewport for table capture
        page = browser.new_page(viewport={"width": 1200, "height": 800})

        # Load the page and wait for network to be mostly idle
        page.goto(url, wait_until="networkidle")

        # Wait a bit more for any dynamic content to settle
        page.wait_for_timeout(2000)

        # Find the iframe containing the spreadsheet
        iframe = page.locator("iframe").first
        iframe.wait_for(state="visible", timeout=15000)

        if table_only:
            # Switch to iframe context to find the table
            iframe_element = page.frame_locator("iframe").first

            # Wait for table to be visible
            table = iframe_element.locator("table").first
            table.wait_for(state="visible", timeout=10000)

            # Get table's bounding box
            box = table.bounding_box()
            if box:
                print(f"Table dimensions: {box['width']}x{box['height']}")
                print(f"Table position: x={box['x']}, y={box['y']}")

                # Screenshot just the table
                table.screenshot(path=output_file, type="png")
            else:
                print("Warning: Could not get table bounding box, capturing entire iframe")
                iframe.screenshot(path=output_file, type="png")
        else:
            # Capture entire iframe
            box = iframe.bounding_box()
            if box:
                print(f"Iframe dimensions: {box['width']}x{box['height']}")

            iframe.screenshot(path=output_file, type="png")

        browser.close()

        return output_file

output_file = capture_sheet_table(URL, table_only=True)
print(f"Saved screenshot to: {output_file}")
