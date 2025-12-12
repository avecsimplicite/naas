# Translation Template: postemensuels Feature

## Purpose
This document provides a structured template for translating the `postemensuels` feature description into different languages. It ensures consistency, completeness, and technical accuracy across all language versions.

---

## Language: [LANGUAGE_NAME]
**Language Code**: [ISO_639-1_CODE]
**Translated By**: [TRANSLATOR_NAME]
**Translation Date**: [DATE]
**Status**: [DRAFT / REVIEW / APPROVED]

---

## 1. Feature Title & Overview

### Original (English)
**Title**: Sheet Table Capture Automation
**Subtitle**: Automated periodic capture and preservation of dynamic web-based spreadsheet content

### Translation
**Title**: [TRANSLATE]
**Subtitle**: [TRANSLATE]

---

## 2. Core Concepts (Key Terms)

| English | [LANGUAGE] | Context | Notes |
|---------|-----------|---------|-------|
| Browser Automation | [TRANSLATE] | Core technology | |
| Screenshot | [TRANSLATE] | Output format | |
| Iframe | [TRANSLATE] | HTML element | |
| Viewport | [TRANSLATE] | Display dimension | |
| Network Idle | [TRANSLATE] | Loading state | |
| Headless Mode | [TRANSLATE] | Browser operation | |
| Bounding Box | [TRANSLATE] | Geometry/dimensions | |
| Timestamp | [TRANSLATE] | Time reference | |
| Playwright | [TRANSLATE] | Tool name | (May remain unchanged) |
| Google Sheets | [TRANSLATE] | Service name | (May remain unchanged) |

---

## 3. Feature Description

### Original (English)
```
Automate the capture and preservation of dynamic web-based spreadsheet content
(Google Sheets) as high-quality PNG screenshots with timestamped archival.
This enables periodic documentation of spreadsheet data states without manual
intervention, useful for auditing, reporting, and historical record-keeping.
```

### Translation
```
[TRANSLATE THE ABOVE PARAGRAPH]
```

---

## 4. Use Cases

### Original (English)
1. **Periodic Archival**: Daily/weekly sheet snapshots for compliance
2. **Change Tracking**: Visual record of data modifications over time
3. **Report Generation**: Automated visual exports for stakeholders
4. **Audit Trails**: Document historical spreadsheet states
5. **Data Backup**: Preserve sheet appearance and content state

### Translation
1. **[TRANSLATE]**: [TRANSLATE]
2. **[TRANSLATE]**: [TRANSLATE]
3. **[TRANSLATE]**: [TRANSLATE]
4. **[TRANSLATE]**: [TRANSLATE]
5. **[TRANSLATE]**: [TRANSLATE]

---

## 5. Technical Components

| Component | Original | Translation | Notes |
|-----------|----------|-------------|-------|
| Browser Automation Engine | Automate user interactions with web pages | [TRANSLATE] | |
| URL Handler | Manage target spreadsheet location | [TRANSLATE] | |
| Viewport Manager | Control capture dimensions | [TRANSLATE] | |
| Content Loader | Wait for dynamic content rendering | [TRANSLATE] | |
| Screenshot Capture | Convert iframe content to image | [TRANSLATE] | |
| File Naming System | Generate unique, timestamped filenames | [TRANSLATE] | |

---

## 6. Execution Flow Steps

### Original (English)
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

### Translation
```
1. [TRANSLATE]
2. [TRANSLATE]
3. [TRANSLATE]
4. [TRANSLATE]
5. [TRANSLATE]
6. [TRANSLATE]
7. [TRANSLATE]
8. [TRANSLATE]
9. [TRANSLATE]
10. [TRANSLATE]
11. [TRANSLATE]
12. [TRANSLATE]
13. [TRANSLATE]
```

---

## 7. Configuration Parameters

| Parameter | English Description | [LANGUAGE] Translation | Example |
|-----------|-------------------|---------------------|---------|
| URL | Target spreadsheet URL | [TRANSLATE] | Public Sheets publink |
| viewport.width | Browser window width in pixels | [TRANSLATE] | 1600 |
| viewport.height | Browser window height in pixels | [TRANSLATE] | 1200 |
| wait_until | Page load completion strategy | [TRANSLATE] | "networkidle" |
| additional_wait | Extra stabilization time in milliseconds | [TRANSLATE] | 2000 |

---

## 8. Output Specification

### File Naming

**English Description**:
- Filename format: `{YYYY-MM-DD}_postemensuels.png`
- Uses ISO 8601 date format
- Automatically prefixes with current date

**[Language] Translation**:
```
[TRANSLATE THE ABOVE]
```

---

## 9. Error Messages

| Error Type | English | [Language] |
|-----------|---------|-----------|
| Iframe Not Found | Unable to locate iframe element | [TRANSLATE] |
| Network Timeout | Page load timeout exceeded | [TRANSLATE] |
| File Write Error | Failed to write screenshot file | [TRANSLATE] |
| Permission Error | Permission denied - check write access | [TRANSLATE] |

---

## 10. Limitations & Constraints

### Original (English)

| Limitation | Impact | Workaround |
|-----------|--------|-----------|
| Captures iframe only | May exclude headers/metadata | Adjust viewport or URL |
| Single URL hardcoded | No multi-sheet support | Parameterize function |
| No error recovery | Fails on missing elements | Add try-catch blocks |
| Static viewport | Content may overflow/truncate | Calculate dynamic dimensions |
| Synchronous execution | Blocks on long waits | Convert to async/await |

### Translation

| [TRANSLATE] | [TRANSLATE] | [TRANSLATE] |
|-----------|--------|-----------|
| [TRANSLATE] | [TRANSLATE] | [TRANSLATE] |
| [TRANSLATE] | [TRANSLATE] | [TRANSLATE] |
| [TRANSLATE] | [TRANSLATE] | [TRANSLATE] |
| [TRANSLATE] | [TRANSLATE] | [TRANSLATE] |
| [TRANSLATE] | [TRANSLATE] | [TRANSLATE] |

---

## 11. Function Signature & API

### Original (English)
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

### Translation (Docstring)
```python
def capture_sheet_table(url: str) -> str:
    """
    [TRANSLATE DOCSTRING]

    [TRANSLATE] (Parameters):
        url (str): [TRANSLATE]

    [TRANSLATE] (Returns):
        str: [TRANSLATE]

    [TRANSLATE] (Raises):
        PlaywrightException: [TRANSLATE]
        TimeoutError: [TRANSLATE]
    """
```

---

## 12. Usage Examples

### Original (English)
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

### Translation (Comments)
```python
# [TRANSLATE: Single capture]
output = capture_sheet_table("https://docs.google.com/spreadsheets/...")
print(f"[TRANSLATE: Saved:] {output}")

# [TRANSLATE: Scheduled automation]
```

---

## 13. Security Considerations

### Original (English)

| Aspect | Risk Level | Mitigation |
|--------|-----------|-----------|
| Public URL exposure | Medium | Use private sharing link |
| Screenshot storage | Medium | Encrypt disk, secure location |
| Browser automation | Low | Keep Playwright updated |
| Network interception | Low | Use HTTPS URLs only |

### Translation

| [TRANSLATE] | [TRANSLATE] | [TRANSLATE] |
|--------|-----------|-----------|
| [TRANSLATE] | [TRANSLATE] | [TRANSLATE] |
| [TRANSLATE] | [TRANSLATE] | [TRANSLATE] |
| [TRANSLATE] | [TRANSLATE] | [TRANSLATE] |
| [TRANSLATE] | [TRANSLATE] | [TRANSLATE] |

---

## 14. File Structure & Naming

### Original (English)
```
project/
├── postemensuels.py          (Main script)
├── FEATURE_DESCRIPTION.md    (Feature documentation)
├── TECHNICAL_GLOSSARY.json   (Multilingual glossary)
├── TRANSLATION_TEMPLATE.md   (Translation guide)
└── [YYYY-MM-DD]_postemensuels.png  (Output files)
```

### Translation (Folder names if applicable)
```
[TRANSLATED_PROJECT_NAME]/
├── postemensuels.py
├── [TRANSLATED]_FEATURE_DESCRIPTION.md
├── [TRANSLATED]_TECHNICAL_GLOSSARY.json
├── [TRANSLATED]_TRANSLATION_TEMPLATE.md
└── [YYYY-MM-DD]_postemensuels.png
```

---

## 15. Common Phrases for Reuse

| English | [Language] | Context |
|---------|-----------|---------|
| Capture a screenshot | [TRANSLATE] | Action verb |
| Wait for page to load | [TRANSLATE] | Status description |
| Check file permissions | [TRANSLATE] | Instruction |
| Clear browser cache | [TRANSLATE] | Maintenance action |
| Run in background | [TRANSLATE] | Execution mode |
| Generate report | [TRANSLATE] | Output action |
| Schedule task | [TRANSLATE] | Automation setup |
| Handle error gracefully | [TRANSLATE] | Error management |

---

## 16. Glossary Verification Checklist

- [ ] All technical terms translated consistently
- [ ] Tool names (Playwright, Chromium, Google Sheets) verified
- [ ] Error messages are clear and actionable
- [ ] Date/time formats appropriately localized
- [ ] Measurement units (pixels, milliseconds) remain unchanged
- [ ] Code examples remain readable and unmodified
- [ ] Links and URLs preserved as-is
- [ ] Cultural context considered (date formats, terminology)

---

## 17. Translation Notes & Conventions

### Terminology Standards
```
This [LANGUAGE] translation follows these conventions:

- **Product Names**: Keep original names (e.g., "Playwright", "Google Sheets")
- **Technical Terms**: [SPECIFY CONVENTIONS FOR YOUR LANGUAGE]
- **Date Format**: [SPECIFY LOCAL FORMAT, e.g., DD/MM/YYYY]
- **Numbers**: [SPECIFY SEPARATOR, e.g., . or , for decimals]
- **Capitalization**: [SPECIFY RULES FOR YOUR LANGUAGE]
```

### Translation Conventions
- Maintain gender neutrality where possible
- Use formal/informal tone as appropriate for audience
- Preserve code comments in technical sections
- Keep line breaks and formatting of tables
- Translate section headers and labels
- Localize examples where culturally relevant

---

## 18. Review & Quality Assurance

### Pre-Submission Checklist
- [ ] All text sections translated
- [ ] Technical terms verified against glossary
- [ ] Error messages tested for clarity
- [ ] Code examples remain functional
- [ ] Links and references intact
- [ ] Formatting preserved
- [ ] Proofreading completed
- [ ] Cultural appropriateness verified

### Peer Review (if applicable)
- [ ] Second translator review completed
- [ ] Technical accuracy verified
- [ ] Terminology consistency checked
- [ ] Style guide compliance confirmed

---

## 19. Version Control

**Original Version**: FEATURE_DESCRIPTION.md v1.0
**This Translation Version**: [VERSION_NUMBER]
**Base Translation Date**: [DATE]
**Last Updated**: [DATE]
**Translator(s)**: [NAMES]
**Reviewer(s)**: [NAMES]

---

## 20. Feedback & Improvements

### Known Issues with This Translation
```
[LIST ANY AMBIGUITIES OR CHALLENGING TRANSLATIONS]

Example:
- "Network Idle" - technical term with no direct equivalent
  → Proposed: "[LANGUAGE EQUIVALENT]"
  → Context: Refers to network activity completion state
```

### Suggestions for Future Versions
```
[DOCUMENT IMPROVEMENTS FOR NEXT ITERATION]
```

---

## 21. Support & Contact Information

- **Translation Coordinator**: [NAME / EMAIL]
- **Technical Review**: [NAME / EMAIL]
- **Quality Assurance**: [NAME / EMAIL]

For questions about translations, please contact the translation coordinator.

---

## Appendix A: Glossary Reference

Refer to `TECHNICAL_GLOSSARY.json` for complete multilingual term definitions.

Key terms to verify:
- Browser Automation
- Screenshot
- Iframe
- Viewport
- Network Idle
- And 20+ more technical terms

---

## Appendix B: Resources for Translators

### Useful References
- [Playwright Documentation](https://playwright.dev/python/) (for technical accuracy)
- [Google Sheets Help](https://support.google.com/docs) (for service-specific terms)
- ISO 8601 Standard (for date format references)

### Translation Tools
- [Technical Glossary](./TECHNICAL_GLOSSARY.json) - JSON format, computer-readable
- [Feature Description](./FEATURE_DESCRIPTION.md) - Comprehensive source document
- Dictionary/terminology databases in your language

---

**END OF TRANSLATION TEMPLATE**

*This template ensures systematic, accurate translation while maintaining technical precision and cultural appropriateness across all language versions.*
