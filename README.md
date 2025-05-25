# Seco - Security Code Scanner

Seco is a simple CLI tool that performs security code analysis on your projects. It helps developers identify potential security vulnerabilities in their codebase directly from the terminal.

## Features

- Scan code for security vulnerabilities using static analysis
- Display results in a beautiful, colored terminal output
- Export reports in JSON or HTML format
- Simple, intuitive command-line interface

## Installation

```bash
# Clone the repository
git clone https://github.com/Nixar-1
cd seco

# Install dependencies
pip install -r requirements.txt

# Make the script executable (Linux/Mac)
chmod +x seco.py
```

## Usage

Basic usage:

```bash
python seco.py /path/to/your/project
```

Export results to a file:

```bash
# Export to JSON
python seco.py /path/to/your/project --output json

# Export to HTML with a specific filename
python seco.py /path/to/your/project --output html --file report.html
```

### Command-line Options

- `path`: The path to the directory to scan (required)
- `--output, -o`: Output format for the report (`json` or `html`)
- `--file, -f`: Output file path for the report

## How It Works

Seco uses Bandit, a comprehensive Python security analysis tool, to perform static code analysis. It identifies common security issues like:

- Hardcoded passwords and secrets
- SQL injection vulnerabilities
- Command injection vulnerabilities
- Use of insecure functions
- And more...

The results are presented in an easy-to-read format with color-coding for severity levels.

## Future Enhancements

- Scan dependencies with pip-audit
- Partial auto-fixing of security issues
- Support for additional languages (JavaScript, etc.)
- Integration with CI/CD pipelines
- Custom rule configuration

## Requirements

- Python 3.6+
- Bandit
- Rich

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.