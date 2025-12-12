# NAAS Quick Start Guide

Get up and running with NAAS in 5 minutes!

## Installation (2 minutes)

```bash
# Clone the repository
git clone https://github.com/your-org/naas.git
cd naas

# Install dependencies
pip install -r requirements.txt

# Set up Playwright browsers
playwright install chromium
```

## Basic Usage (3 minutes)

### Option 1: Direct Python

```python
from postemensuels import capture_sheet_table

# Capture your spreadsheet
output = capture_sheet_table("https://docs.google.com/spreadsheets/d/e/YOUR_SHEET_ID/pub?gid=0")
print(f"Screenshot saved: {output}")
```

### Option 2: Command Line (future version)

```bash
python postemensuels.py "https://docs.google.com/spreadsheets/..."
```

### Option 3: Scheduled Capture

```python
import schedule
import time
from postemensuels import capture_sheet_table

def daily_capture():
    output = capture_sheet_table("https://docs.google.com/spreadsheets/...")
    print(f"Captured: {output}")

# Run every day at 9 AM
schedule.every().day.at("09:00").do(daily_capture)

while True:
    schedule.run_pending()
    time.sleep(60)
```

## Output

Your screenshot will be saved as:
```
2024-12-12_postemensuels.png
```

## Configuration

### Custom Viewport Size

```python
# Future enhancement - currently uses fixed 1600x1200
# Modify postemensuels.py line 15:
page = browser.new_page(viewport={"width": 2000, "height": 1400})
```

### Custom Output Directory

```python
# Future enhancement - currently saves to current directory
# Plan to add config support in v1.1
```

## Common Issues

### Issue: "Iframe not found" error
**Solution**: Ensure the Google Sheet is publicly shared
- Open Google Sheet → Share → Change to "Anyone with the link"
- Verify URL is accessible in browser

### Issue: "playwright module not found"
**Solution**: Install Playwright
```bash
pip install playwright
playwright install chromium
```

### Issue: Permission denied when saving
**Solution**: Check write permissions
```bash
ls -la .  # Check current directory permissions
chmod 755 .  # Add write permission if needed
```

## Next Steps

1. **Read the README**: Full documentation and API reference
2. **Check FEATURE_DESCRIPTION.md**: Technical deep dive
3. **Review CONTRIBUTING.md**: Development guidelines
4. **Explore examples**: Coming in v1.1

## Support

- 📖 [Full Documentation](./README.md)
- 🐛 [Report Issues](https://github.com/your-org/naas/issues)
- 💡 [Request Features](https://github.com/your-org/naas/discussions)

---

**Ready to capture?** 🚀

```python
from postemensuels import capture_sheet_table
output = capture_sheet_table("YOUR_SHEET_URL")
```

Happy automating! 📊
