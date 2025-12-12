# Feature: Sheet Table Capture Automation

## 1. Feature Overview

### Core Purpose
Automate the capture and preservation of dynamic web-based spreadsheet content (Google Sheets) as high-quality PNG screenshots with timestamped archival.

### Key Benefit
Enables periodic documentation of spreadsheet data states without manual intervention, useful for auditing, reporting, and historical record-keeping.

---

## 2. Technical Architecture

### 2.1 Core Components

| Component | Purpose | Technology |
|-----------|---------|------------|
| **Browser Automation Engine** | Automate user interactions with web pages | Playwright (Chromium) |
| **URL Handler** | Manage target spreadsheet location | URL configuration |
| **Viewport Manager** | Control capture dimensions | Browser viewport settings |
| **Content Loader** | Wait for dynamic content rendering | Network idle detection |
| **Screenshot Capture** | Convert iframe content to image | Playwright screenshot API |
| **File Naming System** | Generate unique, timestamped filenames | datetime module |

### 2.2 Execution Flow

```
1. Initialize Playwright + Chromium Browser
2. Configure viewport dimensions (1600x1200)
3. Navigate to target URL
4. Wait for network idle state
5. Apply additional stabilization delay (2000ms)
6. Locate iframe element
7. Wait for iframe visibility
8. Retrieve iframe bounding box dimensions
9. Capture iframe as PNG screenshot
10. Generate timestamped filename
11. Save to disk
12. Close browser session
13. Return file path reference
```

---

## 3. Input Parameters

### 3.1 Configuration

| Parameter | Type | Current Value | Description |
|-----------|------|---------------|-------------|
| `URL` | String | Google Sheets publink | Target spreadsheet URL (must be publicly shared) |
| `viewport.width` | Integer | 1600 | Browser window width in pixels |
| `viewport.height` | Integer | 1200 | Browser window height in pixels |
| `wait_until` | String | "networkidle" | Page load completion strategy |
| `additional_wait` | Integer | 2000 | Extra stabilization time in milliseconds |
| `iframe_timeout` | Integer | 15000 | Maximum iframe visibility wait time (ms) |
| `headless_mode` | Boolean | True | Run browser without UI |

---

## 4. Output Specification

### 4.1 File Output

| Property | Value | Format |
|----------|-------|--------|
| **Filename Format** | `{YYYY-MM-DD}_postemensuels.png` | Date-prefixed |
| **File Type** | PNG image | Raster graphics |
| **Color Space** | RGB/RGBA | Standard web image |
| **Location** | Current working directory | Relative path |
| **Naming Convention** | ISO 8601 date format | International standard |

### 4.2 Console Output

- **Iframe Dimensions**: Logged bounding box (width × height in pixels)
- **Completion Message**: File save confirmation with path

---

## 5. Dependencies

### 5.1 Python Libraries

| Library | Version | Purpose |
|---------|---------|---------|
| `playwright` | >= 1.40 | Browser automation framework |
| `datetime` | Built-in | Timestamp generation |

### 5.2 External Requirements

- **Chromium Browser**: Downloaded automatically by Playwright
- **Internet Connection**: Required for URL access
- **File System Access**: Write permissions to execution directory

---

## 6. Error Handling

### 6.1 Current Handling

| Scenario | Behavior |
|----------|----------|
| Network timeout | Waits up to networkidle threshold |
| Iframe not found | Script fails (no current error handling) |
| Iframe invisible | Waits up to 15000ms |
| Missing permissions | File write error raised |

### 6.2 Recommended Enhancements

- [ ] Timeout exception handling with retry logic
- [ ] Invalid URL validation before execution
- [ ] Iframe element verification with fallback
- [ ] Write permission pre-flight check
- [ ] Network error recovery mechanism

---

## 7. Performance Characteristics

### 7.1 Execution Metrics

| Aspect | Details |
|--------|---------|
| **Typical Duration** | 8-15 seconds per capture |
| **Memory Usage** | ~200-400MB (Chromium process) |
| **Disk I/O** | Single PNG write (size varies) |
| **Network Dependency** | Full sheet load required |
| **Parallelization** | Can run multiple instances sequentially |

### 7.2 Scalability Considerations

- Single-threaded execution model
- Sequential processing limitation
- Browser instance per execution
- Suitable for scheduled batch operations

---

## 8. Use Cases

### 8.1 Primary Uses

1. **Periodic Archival**: Daily/weekly sheet snapshots for compliance
2. **Change Tracking**: Visual record of data modifications over time
3. **Report Generation**: Automated visual exports for stakeholders
4. **Audit Trails**: Document historical spreadsheet states
5. **Data Backup**: Preserve sheet appearance and content state

### 8.2 Integration Scenarios

- Scheduled cron jobs (Linux/Mac)
- Task scheduler (Windows)
- CI/CD pipeline integration
- Webhook-triggered automation
- Batch processing workflows

---

## 9. Limitations & Constraints

### 9.1 Current Limitations

| Limitation | Impact | Workaround |
|-----------|--------|-----------|
| Captures iframe only | May exclude headers/metadata | Adjust viewport or URL |
| Single URL hardcoded | No multi-sheet support | Parameterize function |
| No error recovery | Fails on missing elements | Add try-catch blocks |
| Static viewport | Content may overflow/truncate | Calculate dynamic dimensions |
| Synchronous execution | Blocks on long waits | Convert to async/await |

### 9.2 Technical Constraints

- Requires public spreadsheet sharing
- Dependent on Google Sheets API availability
- Network latency affects execution time
- Chromium resource consumption
- File system write permissions mandatory

---

## 10. Configuration & Customization

### 10.1 Configurable Elements

```python
# URL Configuration
URL = "https://docs.google.com/spreadsheets/..."

# Viewport Dimensions
viewport = {"width": 1600, "height": 1200}

# Timing Parameters
network_idle_timeout = "networkidle"
stabilization_delay = 2000  # ms
iframe_visibility_timeout = 15000  # ms

# Output Format
filename_format = "{YYYY-MM-DD}_postemensuels.png"
file_type = "png"
```

### 10.2 Extension Points

- Custom URL source (database, config file)
- Dynamic viewport calculation
- Multiple export formats (PDF, SVG, WebP)
- Cloud storage upload
- Email delivery integration
- Slack notification webhooks

---

## 11. Security & Privacy

### 11.1 Considerations

| Aspect | Risk Level | Mitigation |
|--------|-----------|-----------|
| Public URL exposure | Medium | Use private sharing link |
| Screenshot storage | Medium | Encrypt disk, secure location |
| Browser automation | Low | Keep Playwright updated |
| Network interception | Low | Use HTTPS URLs only |

### 11.2 Data Handling

- Captures only visible/rendered content
- No external data transmission (local save only)
- Screenshot files contain sensitive spreadsheet data
- Proper file permissions recommended (0600)

---

## 12. Maintenance & Updates

### 12.1 Version Compatibility

- **Python**: 3.8+
- **Playwright**: API stable (1.40+)
- **Chromium**: Auto-updated by Playwright

### 12.2 Known Issues

- None documented currently
- Test against Google Sheets UI changes annually

---

## 13. API Reference

### 13.1 Function Signature

```python
def capture_sheet_table(url: str) -> str:
    """
    Capture a Google Sheets iframe as a timestamped PNG screenshot.

    Parameters:
        url (str): Public Google Sheets URL with iframe

    Returns:
        str: Path to generated PNG file (e.g., "2024-12-12_postemensuels.png")

    Raises:
        PlaywrightException: If browser or navigation fails
        TimeoutError: If iframe doesn't appear within timeout
    """
```

### 13.2 Usage Example

```python
from postemensuels import capture_sheet_table

# Single capture
output = capture_sheet_table("https://docs.google.com/spreadsheets/...")
print(f"Saved: {output}")

# Scheduled automation (pseudocode)
import schedule
schedule.every().day.at("09:00").do(
    capture_sheet_table,
    url="https://docs.google.com/spreadsheets/..."
)
```

---

## 14. Testing & Validation

### 14.1 Test Scenarios

- [ ] Valid public spreadsheet URL
- [ ] Network timeout handling
- [ ] Iframe dimensions verification
- [ ] PNG file format validation
- [ ] Filename timestamp format
- [ ] File overwrite behavior
- [ ] Permission error handling
- [ ] Browser crash recovery

### 14.2 Success Criteria

- PNG file created with correct filename
- Iframe content fully visible in screenshot
- Bounding box dimensions logged
- No exceptions or warnings in console
- File readable and valid PNG format

---

## 15. Glossary (Multilingual Terms)

### Core Terminology

| English | French | Spanish | German | Context |
|---------|--------|---------|--------|---------|
| **Screenshot** | Capture d'écran | Captura de pantalla | Bildschirmfoto | Image file created |
| **Iframe** | Cadre intégré | Marco integrado | Eingebetteter Rahmen | HTML container element |
| **Viewport** | Fenêtre d'affichage | Ventana de visualización | Ansichtsfenster | Browser display area |
| **Network Idle** | Réseau inactif | Red inactiva | Netzwerk untätig | Loading completion state |
| **Bounding Box** | Boîte englobante | Cuadro delimitador | Begrenzungsrahmen | Element dimensions |
| **Headless** | Sans interface | Sin interfaz | Ohne Benutzeroberfläche | Browser mode without UI |
| **Timestamp** | Horodatage | Marca de tiempo | Zeitstempel | Date-time marker |
| **Public Share** | Partage public | Compartición pública | Öffentlicher Link | Open spreadsheet URL |

---

## 16. Internationalization (i18n) Notes

### 16.1 String Resources for Translation

```python
STRINGS = {
    "iframe_dimensions_log": "Iframe dimensions: {width}x{height}",
    "save_complete": "Saved screenshot to: {filepath}",
    "error_iframe_not_found": "Unable to locate iframe element",
    "error_network_timeout": "Page load timeout exceeded",
    "error_file_write": "Failed to write screenshot file",
}
```

### 16.2 Regional Considerations

- Date format: ISO 8601 (locale-independent)
- Numeric separators: Dot (.) for decimals, consistent across regions
- Character encoding: UTF-8 throughout
- Timezone: Use system local time (can be overridden)

---

## 17. Future Enhancements

### 17.1 Planned Features

- [ ] Support multiple sheets in single execution
- [ ] PDF export format option
- [ ] Cloud storage integration (S3, GCS, Azure)
- [ ] Email notification on completion
- [ ] Slack/Teams webhook integration
- [ ] Comparison mode (visual diff between captures)
- [ ] Data extraction (OCR to CSV)
- [ ] Async/concurrent execution
- [ ] Web UI dashboard
- [ ] REST API endpoint

### 17.2 Technical Debt

- Refactor hardcoded URL to configuration management
- Add comprehensive error handling
- Implement logging framework
- Add unit and integration tests
- Create Docker container
- Add CLI argument parsing

---

## 18. References & Resources

### 18.1 Documentation Links

- [Playwright Python Docs](https://playwright.dev/python/)
- [Google Sheets Public Sharing](https://support.google.com/docs/answer/183965)
- [PNG Image Format Spec](https://www.w3.org/TR/png/)

### 18.2 Related Tools

- Selenium (alternative automation)
- Puppeteer (Node.js equivalent)
- headless-chrome (direct CLI tool)
- Screenshots.com (SaaS alternative)

---

## 19. Version History

### v1.0 (Current)
- Basic iframe capture functionality
- Timestamp-based file naming
- Network idle detection
- Fixed viewport dimensions

### Planned Versions
- v1.1: Error handling & retry logic
- v1.2: Configuration file support
- v2.0: Multi-sheet & format support

---

## 20. Support & Contact

- **Issue Tracking**: GitHub Issues
- **Documentation**: This file
- **Changelog**: Commit history
- **Maintenance**: Community contributions welcome
