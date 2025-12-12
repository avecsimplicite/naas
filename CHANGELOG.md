# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Multiple sheet capture in single execution
- PDF export format support
- Cloud storage integration (S3, GCS, Azure)
- Email notifications
- Slack/Teams webhook integration
- Visual diff comparison
- OCR-based data extraction
- Async/concurrent execution
- Web UI dashboard
- REST API endpoint

## [1.0.0] - 2024-12-12

### Added
- Initial release of NAAS
- Basic iframe capture functionality
- Timestamp-based PNG file naming (ISO 8601 format)
- Network idle detection for dynamic content
- Configurable viewport dimensions (default 1600x1200)
- Bounding box dimension logging
- Comprehensive documentation (FEATURE_DESCRIPTION.md)
- Translation template for internationalization
- README with quick start guide
- Contributing guidelines
- MIT License

### Features
- Browser automation using Playwright + Chromium
- Support for public Google Sheets URLs
- Headless execution mode
- Automatic browser resource cleanup
- Error reporting for debugging

---

## Versioning

### Current Version: 1.0.0

### Next Planned Releases

**1.1.0** (Q1 2025)
- Error handling improvements
- Retry logic for transient failures
- Configuration file support (.naasrc)
- Logging framework integration
- Unit test suite

**1.2.0** (Q2 2025)
- Multiple sheets per execution
- Batch processing utilities
- Environment variable configuration
- Docker support

**2.0.0** (Q3 2025)
- PDF export format
- Cloud storage backends
- Email/Slack notifications
- REST API endpoint
- Web dashboard

---

## Migration Guides

### From 0.x to 1.0.0

This is the first public release. No migration needed.

---

## Support

For more information:
- 📖 [README](./README.md)
- 📚 [Feature Description](./FEATURE_DESCRIPTION.md)
- 🐛 [Report Issues](https://github.com/your-org/naas/issues)

---

Last Updated: 2024-12-12
