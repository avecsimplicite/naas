# Contributing to NAAS

Thank you for your interest in contributing to NAAS! This document provides guidelines and instructions for contributing.

## Code of Conduct

Please be respectful and constructive in all interactions with the community.

## Getting Started

### 1. Fork & Clone

```bash
# Fork the repository on GitHub
# Clone your fork
git clone https://github.com/your-username/naas.git
cd naas
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install pytest pytest-cov  # For testing

# Install pre-commit hooks (optional)
pip install pre-commit
pre-commit install
```

## Development Workflow

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

Use descriptive branch names:
- `feature/add-email-notifications`
- `fix/timeout-handling`
- `docs/update-readme`

### 2. Make Changes

- Follow PEP 8 style guidelines
- Write clear, descriptive commit messages
- Add comments for complex logic
- Keep changes focused and atomic

### 3. Test Your Changes

```bash
# Run unit tests
pytest tests/

# Run with coverage
pytest --cov=postemensuels tests/
```

### 4. Commit & Push

```bash
git add .
git commit -m "Clear description of changes"
git push origin feature/your-feature-name
```

## Pull Request Process

1. **Before Submitting**:
   - Ensure all tests pass: `pytest`
   - Format code: Check for PEP 8 compliance
   - Update documentation if needed
   - Add tests for new functionality

2. **Create PR**:
   - Use a descriptive title
   - Reference related issues (#123)
   - Describe what changed and why
   - Include test results

3. **Review Process**:
   - At least one approval required
   - All CI/CD checks must pass
   - Address feedback promptly

## Types of Contributions

### Bug Fixes
- Create an issue describing the bug
- Reference the issue in your PR
- Include reproduction steps
- Add test case that fails before fix

### Features
- Discuss in issues before starting
- Keep scope focused
- Add documentation
- Include unit tests

### Documentation
- Grammar and clarity fixes
- Clarify complex sections
- Add examples
- Translate content

### Tests
- Increase code coverage
- Add edge case tests
- Improve error scenario coverage

## Coding Standards

### Python Style

```python
# Follow PEP 8
# Use type hints where appropriate
from typing import Optional

def capture_sheet_table(url: str, config: Optional[dict] = None) -> str:
    """
    Clear docstring with type information.

    Args:
        url: The Google Sheets URL
        config: Optional configuration dictionary

    Returns:
        Path to generated PNG file
    """
    pass
```

### Naming Conventions

- Variables: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Private methods: `_leading_underscore`

## Testing

### Test Structure

```python
# tests/test_capture.py
import pytest
from postemensuels import capture_sheet_table

class TestCaptureSheetTable:
    def test_successful_capture(self):
        # Arrange
        url = "https://docs.google.com/spreadsheets/..."

        # Act
        result = capture_sheet_table(url)

        # Assert
        assert result.endswith('.png')
        assert result.startswith('20')  # Date format

    def test_invalid_url_raises_error(self):
        with pytest.raises(Exception):
            capture_sheet_table("invalid-url")
```

### Test Coverage Requirements

- Minimum 80% code coverage
- All public functions tested
- Error cases covered

## Documentation

### Update These Files

- `README.md` - For user-facing changes
- `FEATURE_DESCRIPTION.md` - For technical details
- Docstrings - For function documentation
- `CHANGELOG.md` - For release notes

### Documentation Style

```python
def capture_sheet_table(url: str) -> str:
    """
    Capture a Google Sheets iframe as a timestamped PNG screenshot.

    This is a detailed description of what the function does,
    including any important behaviors or side effects.

    Args:
        url (str): Public Google Sheets URL with iframe
                   Example: "https://docs.google.com/spreadsheets/d/e/2PACX-1v.../pub?gid=0"

    Returns:
        str: Path to generated PNG file
             Example: "2024-12-12_postemensuels.png"

    Raises:
        PlaywrightException: If browser fails to launch or navigate
        TimeoutError: If iframe doesn't appear within timeout

    Examples:
        >>> output = capture_sheet_table("https://docs.google.com/spreadsheets/...")
        >>> print(output)
        2024-12-12_postemensuels.png
    """
```

## Release Process

### Version Numbering

Uses semantic versioning: `MAJOR.MINOR.PATCH`

- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes

### Release Steps

1. Update version in code
2. Update `CHANGELOG.md`
3. Create git tag: `git tag v1.0.0`
4. Push: `git push origin v1.0.0`
5. Create GitHub release

## Reporting Bugs

### Issue Template

```markdown
**Describe the bug**
A clear description of what happened.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. See error

**Expected behavior**
What should happen instead.

**Environment**
- OS: [e.g. macOS, Windows]
- Python: [e.g. 3.9]
- Playwright: [e.g. 1.40.0]

**Error logs**
```
[Paste error messages/stack trace]
```
```

## Feature Requests

### Issue Template

```markdown
**Is your feature request related to a problem?**
Describe the use case.

**Describe the solution you'd like**
Clear description of desired behavior.

**Describe alternatives you've considered**
Other solutions you've explored.

**Additional context**
Any other relevant information.
```

## Getting Help

- **Questions**: Use GitHub Discussions
- **Bug Reports**: Open GitHub Issues
- **Documentation**: Check README and FEATURE_DESCRIPTION.md

## Questions?

Feel free to ask questions in:
- GitHub Issues (for bug/feature related)
- GitHub Discussions (for questions/ideas)
- Email: [maintainer email]

---

Thank you for contributing to NAAS! 🙏
