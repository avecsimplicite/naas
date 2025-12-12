# NAAS - Sheet Table Capture Automation

> **Automate the capture and preservation of dynamic web-based spreadsheet content**

Automated periodic capture and preservation of Google Sheets content as high-quality PNG screenshots with timestamped archival.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Architecture](#architecture)
- [Use Cases](#use-cases)
- [API Reference](#api-reference)
- [Performance](#performance)
- [Error Handling](#error-handling)
- [Security & Privacy](#security--privacy)
- [Limitations](#limitations)
- [Future Enhancements](#future-enhancements)
- [Support](#support)

---

## Overview

**NAAS** enables periodic documentation of spreadsheet data states without manual intervention. It's useful for auditing, reporting, historical record-keeping, and compliance purposes.

### Core Purpose

NAAS automates the capture of Google Sheets iframes as high-quality PNG screenshots, generating timestamped filenames for easy archival and tracking of spreadsheet changes over time.

### Key Benefits

✅ Eliminates manual screenshot work
✅ Creates audit trails with automatic timestamps
✅ Preserves spreadsheet states for compliance
✅ Enables visual change tracking over time
✅ Integrates with automation workflows (cron, CI/CD, webhooks)

---

## Features

### Core Capabilities

| Feature | Description |
|---------|-------------|
| **Browser Automation** | Uses Playwright with Chromium for reliable rendering |
| **Dynamic Content Loading** | Waits for network idle state before capture |
| **High-Quality Screenshots** | Configurable viewport dimensions (default 1600x1200) |
| **Timestamped Archival** | Automatic ISO 8601 date-based file naming |
| **Iframe Support** | Captures embedded Google Sheets iframes |
| **Headless Execution** | Runs without UI for server/automation environments |
| **Error Reporting** | Logs bounding box dimensions and file locations |

---

## Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/your-org/naas.git
cd naas

# Install dependencies
pip install playwright

# Download Chromium browser
playwright install chromium
```

### 2. Basic Usage

```python
from postemensuels import capture_sheet_table

# Capture a public Google Sheet
output = capture_sheet_table("https://docs.google.com/spreadsheets/d/e/YOUR_SHEET_ID/pub?gid=0&single=true")
print(f"Saved: {output}")
# Output: 2024-12-12_postemensuels.png
```

### 3. Run as Scheduled Task

```bash
# Daily capture at 9:00 AM (Linux/Mac)
0 9 * * * /usr/bin/python3 /path/to/naas/scheduler.py

# Or use Windows Task Scheduler for Windows systems
```

---

## Installation

### Requirements

- **Python**: 3.8 or higher
- **Playwright**: >= 1.40
- **Chromium**: Auto-installed via Playwright
- **Internet Connection**: For spreadsheet access
- **File System**: Write permissions to execution directory

### Setup Instructions

```bash
# Clone repository
git clone https://github.com/your-org/naas.git
cd naas

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize Playwright browsers
playwright install chromium
```

### requirements.txt

```
playwright>=1.40.0
python-dateutil>=2.8.2
```

---

## Usage

### Basic Function Call

```python
from postemensuels import capture_sheet_table

# Capture a single sheet
output_file = capture_sheet_table("https://docs.google.com/spreadsheets/...")
print(f"Screenshot saved to: {output_file}")
```

### Output Format

- **Filename**: `{YYYY-MM-DD}_postemensuels.png` (ISO 8601 format)
- **Location**: Current working directory (customizable)
- **Format**: PNG image (RGB/RGBA)
- **Dimensions**: Variable (depends on iframe size)

### Console Output

```
Iframe dimensions: 1200x800
Saved screenshot to: 2024-12-12_postemensuels.png
```

---

## Configuration

### Configurable Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `URL` | String | (required) | Public Google Sheets URL |
| `viewport.width` | Integer | 1600 | Browser window width (pixels) |
| `viewport.height` | Integer | 1200 | Browser window height (pixels) |
| `wait_until` | String | "networkidle" | Page load strategy |
| `additional_wait` | Integer | 2000 | Stabilization delay (ms) |
| `iframe_timeout` | Integer | 15000 | Iframe visibility timeout (ms) |
| `headless_mode` | Boolean | True | Run without UI |

### Environment Variables

```bash
# Optional: Override defaults
export NAAS_VIEWPORT_WIDTH=2000
export NAAS_VIEWPORT_HEIGHT=1400
export NAAS_OUTPUT_DIR="/path/to/archives"
```

### Custom Configuration Example

```python
from postemensuels import capture_sheet_table

# Configure custom viewport
config = {
    'viewport': {'width': 2000, 'height': 1400},
    'wait_until': 'networkidle',
    'timeout': 20000,
    'headless': True
}

output = capture_sheet_table(
    url="https://docs.google.com/spreadsheets/...",
    config=config
)
```

---

## Architecture

### System Components

```
┌─────────────────────────────────────────┐
│     NAAS Sheet Capture System           │
├─────────────────────────────────────────┤
│                                         │
│  ┌──────────────────────────────────┐  │
│  │  Browser Automation Engine       │  │
│  │  (Playwright + Chromium)         │  │
│  └──────────────────────────────────┘  │
│              ↓                          │
│  ┌──────────────────────────────────┐  │
│  │  URL Navigation & Content Load   │  │
│  │  (Network Idle Detection)        │  │
│  └──────────────────────────────────┘  │
│              ↓                          │
│  ┌──────────────────────────────────┐  │
│  │  Iframe Locator & Validator      │  │
│  │  (Element Detection)             │  │
│  └──────────────────────────────────┘  │
│              ↓                          │
│  ┌──────────────────────────────────┐  │
│  │  Screenshot Capture              │  │
│  │  (PNG Rendering)                 │  │
│  └──────────────────────────────────┘  │
│              ↓                          │
│  ┌──────────────────────────────────┐  │
│  │  File System Writer              │  │
│  │  (Timestamped Storage)           │  │
│  └──────────────────────────────────┘  │
│                                         │
└─────────────────────────────────────────┘
```

### Execution Flow

1. **Initialize** Playwright + Chromium Browser
2. **Configure** viewport dimensions (1600x1200)
3. **Navigate** to target URL
4. **Wait** for network idle state
5. **Apply** stabilization delay (2000ms)
6. **Locate** iframe element
7. **Wait** for iframe visibility
8. **Retrieve** iframe bounding box dimensions
9. **Capture** iframe as PNG screenshot
10. **Generate** timestamped filename
11. **Save** to disk
12. **Close** browser session
13. **Return** file path reference

---

## Use Cases

### Primary Applications

1. **Periodic Archival** - Daily/weekly sheet snapshots for compliance and audit trails
2. **Change Tracking** - Visual record of data modifications over time
3. **Report Generation** - Automated visual exports for stakeholders
4. **Audit Trails** - Document historical spreadsheet states
5. **Data Backup** - Preserve sheet appearance and content state

### Integration Scenarios

- **Scheduled Jobs**: Cron (Linux/Mac) or Task Scheduler (Windows)
- **CI/CD Pipelines**: Automated screenshot capture during deployments
- **Webhook Triggers**: Event-driven capture on schedule changes
- **Batch Processing**: Multiple sheets in workflow automation
- **Cloud Functions**: Serverless execution (AWS Lambda, Google Cloud Functions)

### Example Workflows

```python
# Scheduled daily capture (using schedule library)
import schedule
from postemensuels import capture_sheet_table

def daily_capture():
    urls = [
        "https://docs.google.com/spreadsheets/d/SHEET_1/...",
        "https://docs.google.com/spreadsheets/d/SHEET_2/...",
    ]
    for url in urls:
        output = capture_sheet_table(url)
        print(f"Captured: {output}")

schedule.every().day.at("09:00").do(daily_capture)

# Run scheduler
while True:
    schedule.run_pending()
    time.sleep(60)
```

---

## API Reference

### Function Signature

```python
def capture_sheet_table(url: str) -> str:
    """
    Capture a Google Sheets iframe as a timestamped PNG screenshot.

    Parameters:
        url (str): Public Google Sheets URL with iframe
                   Example: "https://docs.google.com/spreadsheets/d/e/2PACX-1v.../pub?gid=0"

    Returns:
        str: Path to generated PNG file
             Example: "2024-12-12_postemensuels.png"

    Raises:
        PlaywrightException: If browser fails to launch or navigate
        TimeoutError: If iframe doesn't appear within timeout (15s default)
        FileNotFoundError: If output directory doesn't exist
        PermissionError: If no write access to output directory

    Example:
        >>> output = capture_sheet_table("https://docs.google.com/spreadsheets/...")
        >>> print(output)
        2024-12-12_postemensuels.png
    """
```

### Return Value

```python
# Returns the filename as a string
"2024-12-12_postemensuels.png"
```

### Exception Handling

```python
from postemensuels import capture_sheet_table
import playwright

try:
    output = capture_sheet_table("https://docs.google.com/spreadsheets/...")
    print(f"Success: {output}")
except TimeoutError:
    print("Error: Iframe not found or took too long to load")
except playwright.sync_api.PlaywrightException as e:
    print(f"Browser error: {e}")
except PermissionError:
    print("Error: No write permission to output directory")
```

---

## Performance

### Execution Metrics

| Metric | Typical Value | Notes |
|--------|---------------|-------|
| **Execution Time** | 8-15 seconds | Includes browser startup + page load |
| **Memory Usage** | 200-400 MB | Chromium process overhead |
| **Disk I/O** | Single PNG write | Size varies (500KB - 5MB typical) |
| **Network Dependency** | Full sheet load | Required for dynamic content |
| **Parallelization** | Sequential | Can run multiple instances with separate processes |

### Performance Tips

- **Batch Multiple Captures**: Run several URLs in sequence to amortize startup cost
- **Warm Up Browser**: Keep browser instances warm for repeated captures
- **Optimize Viewport**: Use exact dimensions needed (smaller = faster)
- **Increase Timeout**: If content is heavy, increase `additional_wait`
- **Use Headless Mode**: Always use headless=true for production

---

## Error Handling

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| **TimeoutError** | Iframe not found within timeout | Verify URL is public, increase timeout |
| **PlaywrightException** | Browser launch failed | Check Chromium installation, run `playwright install chromium` |
| **PermissionError** | No write access to directory | Change output directory, check file permissions |
| **FileNotFoundError** | Output directory doesn't exist | Create directory: `mkdir -p output/` |
| **Network Timeout** | Page took too long to load | Verify internet connection, increase wait time |

### Error Recovery

```python
import time
from postemensuels import capture_sheet_table

def capture_with_retry(url, max_retries=3):
    for attempt in range(max_retries):
        try:
            return capture_sheet_table(url)
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"Attempt {attempt + 1} failed, retrying in 5s...")
                time.sleep(5)
            else:
                raise
```

---

## Security & Privacy

### Security Considerations

| Aspect | Risk Level | Mitigation |
|--------|-----------|-----------|
| **Public URL Exposure** | Medium | Use private sharing links with restricted access |
| **Screenshot Storage** | Medium | Encrypt disk, use secure storage location |
| **Browser Automation** | Low | Keep Playwright and Chromium updated |
| **Network Interception** | Low | Always use HTTPS URLs only |

### Data Handling

- ⚠️ Screenshots contain all visible spreadsheet data
- 📁 Store files in secure, restricted-access directories
- 🔐 Use file permissions (chmod 600) to restrict access
- 🗑️ Implement retention policies for archived screenshots
- 🔒 Consider encrypting sensitive snapshot archives

### Privacy Best Practices

```bash
# Restrict file permissions (Linux/Mac)
chmod 600 *.png

# Set restrictive directory permissions
chmod 700 /path/to/archives/

# Use secure storage for sensitive data
# Consider encrypted volumes or cloud storage with access controls
```

---

## Limitations

### Current Limitations

| Limitation | Impact | Workaround |
|-----------|--------|-----------|
| **Iframe Only** | May exclude headers/metadata | Adjust viewport or share settings |
| **Single URL** | No multi-sheet per execution | Run multiple instances or batch in loop |
| **No Error Recovery** | Fails on missing elements | Add try-catch, implement retry logic |
| **Static Viewport** | Content may overflow | Calculate dynamic dimensions |
| **Synchronous** | Blocks on long waits | Queue captures or use async wrapper |

### Technical Constraints

- Requires **publicly shared** Google Sheets
- Dependent on **Google Sheets API** availability
- Network latency affects execution time
- Chromium resource consumption (~200-400 MB per instance)
- File system write permissions mandatory

---

## Future Enhancements

### Planned Features

- [ ] Support multiple sheets in single execution
- [ ] PDF export format option
- [ ] Cloud storage integration (S3, GCS, Azure Blob)
- [ ] Email notification on completion
- [ ] Slack/Teams webhook integration
- [ ] Visual diff comparison (old vs new)
- [ ] OCR-based data extraction to CSV
- [ ] Async/concurrent execution
- [ ] Web UI dashboard
- [ ] REST API endpoint

### Roadmap

**v1.1**: Error handling & retry logic
**v1.2**: Configuration file support
**v2.0**: Multi-sheet & format support
**v3.0**: Cloud integration & REST API

---

## Support

### Documentation

- 📖 [Feature Description](./FEATURE_DESCRIPTION.md) - Comprehensive technical documentation
- 🌍 [Translation Template](./TRANSLATION_TEMPLATE.md) - Internationalization guide
- 🔧 [API Reference](#api-reference) - Function signatures and examples

### Contributing

We welcome contributions! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Bug Reports & Feature Requests

- **Issues**: [GitHub Issues](https://github.com/your-org/naas/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-org/naas/discussions)

### License

This project is licensed under the MIT License - see LICENSE file for details.

---

## Related Tools & Alternatives

| Tool | Type | Use Case |
|------|------|----------|
| **Selenium** | Web Automation | General-purpose automation (slower) |
| **Puppeteer** | Node.js/JS | Browser automation for JavaScript |
| **headless-chrome** | CLI | Direct Chrome automation |
| **Screenshots.com** | SaaS | Cloud-based screenshot service |

---

## Version History

### v1.0 (Current)
- ✅ Basic iframe capture functionality
- ✅ Timestamp-based file naming
- ✅ Network idle detection
- ✅ Fixed viewport dimensions

### Upcoming Versions
- 📋 v1.1: Error handling & retry logic
- 📋 v1.2: Configuration file support
- 📋 v2.0: Multi-sheet & format support

---

## Glossary (Multilingual Terms)

| English | French | Spanish | German | Context |
|---------|--------|---------|--------|---------|
| **Screenshot** | Capture d'écran | Captura de pantalla | Bildschirmfoto | Image file created |
| **Iframe** | Cadre intégré | Marco integrado | Eingebetteter Rahmen | HTML element |
| **Viewport** | Fenêtre d'affichage | Ventana de visualización | Ansichtsfenster | Display area |
| **Network Idle** | Réseau inactif | Red inactiva | Netzwerk untätig | Loading state |
| **Bounding Box** | Boîte englobante | Cuadro delimitador | Begrenzungsrahmen | Element dimensions |
| **Headless** | Sans interface | Sin interfaz | Ohne UI | Browser mode |
| **Timestamp** | Horodatage | Marca de tiempo | Zeitstempel | Time reference |

---

## Project Structure

```
naas/
├── README.md                    # This file
├── LICENSE                      # MIT License
├── requirements.txt             # Python dependencies
├── postemensuels.py            # Main capture script
├── FEATURE_DESCRIPTION.md      # Detailed technical documentation
├── TRANSLATION_TEMPLATE.md     # i18n translation guide
├── examples/
│   ├── basic_capture.py        # Simple usage example
│   ├── scheduled_captures.py   # Cron scheduling example
│   └── batch_processing.py     # Multiple sheets example
├── tests/
│   ├── test_capture.py         # Unit tests
│   └── test_integration.py     # Integration tests
└── docs/
    ├── INSTALLATION.md         # Detailed setup guide
    ├── TROUBLESHOOTING.md      # Common issues & fixes
    └── API.md                  # API reference
```

---

## Quick Links

- 🏠 [Homepage](#)
- 📚 [Documentation](./FEATURE_DESCRIPTION.md)
- 🐛 [Report Bug](https://github.com/your-org/naas/issues)
- 💡 [Request Feature](https://github.com/your-org/naas/discussions)
- 🤝 [Contributing Guide](./CONTRIBUTING.md)

---

**Made with ❤️ for automation enthusiasts**

Last Updated: 2024-12-12
