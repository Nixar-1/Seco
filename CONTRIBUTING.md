# Contributing to Seco

> ⚠️ **Development Status**: Seco is currently in active development (alpha stage). The codebase is rapidly evolving, and breaking changes may occur. Contributors should be aware that:
> - Features may be incomplete or change significantly
> - APIs and command-line interfaces might be unstable
> - Test coverage may be incomplete
> - Documentation might lag behind implementation
>
> Last updated: 2025-05-25 20:50:23 UTC

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Pull Requests](#pull-requests)
- [Development Process](#development-process)
  - [Code Style](#code-style)
  - [Running Tests](#running-tests)
  - [Documentation](#documentation)
- [Project Structure](#project-structure)
- [Git Commit Messages](#git-commit-messages)
- [Recognition](#recognition)
- [Questions?](#questions)

## Code of Conduct

By participating in this project, you are expected to uphold our Code of Conduct:

- Use welcoming and inclusive language
- Be respectful of different viewpoints and experiences
- Accept constructive criticism gracefully
- Focus on what is best for the community
- Show empathy towards other community members

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* Your Python version (`python --version`)
* Your operating system
* Steps to reproduce the issue
* Expected behavior
* Actual behavior
* Any error messages or stack traces

### Suggesting Enhancements

If you have a suggestion for a new feature or an enhancement to existing functionality:

1. Check the roadmap in README.md to see if it's already planned
2. Search through the issues to see if someone else has suggested it
3. If not, create a new issue describing:
   - The use case for the feature
   - How it would work
   - Why it would be useful

### Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. Ensure the test suite passes
4. Make sure your code follows the existing style
5. Update the documentation if needed

## Development Process

1. Clone the repository:
```bash
git clone https://github.com/Nixar-1/Seco.git
cd Seco
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

### Code Style

We use Black for code formatting. Please ensure your code follows this style:

- Maximum line length of 88 characters
- Use double quotes for strings
- Follow PEP 8 guidelines

To format your code:

```bash
black .
```

### Running Tests

```bash
pytest
```

### Documentation

- Update the README.md if you change any user-facing functionality
- Add docstrings to new functions and classes
- Comment complex code sections

## Project Structure

```
seco/
├── seco.py          # Main script
├── tests/           # Test suite
├── requirements.txt # Production dependencies
└── docs/           # Documentation
```

## Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Reference issues and pull requests liberally after the first line
- Consider starting the commit message with an applicable emoji:
  - 🚀 :rocket: when adding features
  - 🐛 :bug: when fixing bugs
  - 📝 :memo: when adding documentation
  - 🎨 :art: when improving code structure
  - ⚡️ :zap: when improving performance
  - 🔒 :lock: when dealing with security

## Recognition

Contributors will be recognized in our README.md and project documentation. Thank you for your contributions!

## Questions?

Feel free to create an issue with your question or contact the maintainer directly through GitHub.

<p align="center">Remember that this is an open source project. Consider the people who will read your code, and make it look nice for them! 😊</p>
<p align="center">Last updated: 2025-05-25 20:50:23 UTC</p>
