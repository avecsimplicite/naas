from playwright.sync_api import sync_playwright
from datetime import datetime
import os


URL_DEFAULT = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRnl8-YerEduI_wn45FLg36yEr2_na23Hrlk-txjYKuz5DxABxZcnuKxsNiqYNcMv3ulGEPveEKiAtP/pub?gid=665461249&single=true&"


def capture_sheet_table(url: str = URL_DEFAULT, table_only: bool = True, output_dir: str | None = None) -> str:
    """
    Capture a Google Sheets table and save as PNG.

    Args:
        url: Public Google Sheets URL
        table_only: If True, captures only the table area. If False, captures entire iframe.
        output_dir: Directory where the PNG will be saved. If None, uses current working dir.

    Returns:
        Path to generated PNG file
    """
    # Generate filename with current date
    today = datetime.now().strftime("%Y-%m-%d")
    output_file = f"{today}_postemensuels.png"

    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, output_file)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1200, "height": 800})

        page.goto(url, wait_until="networkidle")
        page.wait_for_timeout(2000)

        # Find the iframe containing the spreadsheet
        iframe = page.locator("iframe").first
        iframe.wait_for(state="visible", timeout=15000)

        if table_only:
            iframe_element = page.frame_locator("iframe").first
            table = iframe_element.locator("table").first
            try:
                table.wait_for(state="visible", timeout=10000)
            except Exception:
                # If table isn't found, fall back to iframe screenshot
                iframe.screenshot(path=output_file, type="png")
                browser.close()
                return output_file

            box = table.bounding_box()
            if box:
                table.screenshot(path=output_file, type="png")
            else:
                iframe.screenshot(path=output_file, type="png")
        else:
            iframe.screenshot(path=output_file, type="png")

        browser.close()

    return output_file
