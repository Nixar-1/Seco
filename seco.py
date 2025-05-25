#!/usr/bin/env python3
"""
Seco - Code Security Scanner

A CLI tool that performs security checks on your project's code.
"""

import argparse
import json
import os
import subprocess
import sys
from typing import Dict, List, Optional, Any, Union
from pathlib import Path
from datetime import datetime

try:
    from rich.console import Console
    from rich.table import Table
    from rich.progress import Progress
    from rich.panel import Panel
except ImportError:
    print("Rich library is not installed. Please install it using: pip install rich")
    sys.exit(1)

# Initialize Rich console
console = Console()

class SecurityScan:
    """
    Class to handle security scanning operations.
    """
    
    def __init__(self, target_path: str, output_format: Optional[str] = None, output_file: Optional[str] = None):
        """
        Initialize the SecurityScan object.
        
        Args:
            target_path: Path to the directory to scan
            output_format: Format for the output report (json, html, or None for terminal only)
            output_file: Path to save the output report
        """
        self.target_path = Path(target_path).resolve()
        self.output_format = output_format
        self.output_file = output_file
        self.results: List[Dict[str, Any]] = []
        
        # Check if target path exists
        if not self.target_path.exists():
            console.print(f"[bold red]Error:[/] Path '{self.target_path}' does not exist.")
            sys.exit(1)
        
        # Check if bandit is installed
        try:
            subprocess.run(["python", "-m", "bandit", "--version"], capture_output=True, text=True, check=True)
        except (subprocess.SubprocessError, FileNotFoundError):
            console.print("[bold red]Error:[/] Bandit is not installed. Please install it using: pip install bandit")
            sys.exit(1)
    
    def scan(self) -> List[Dict[str, Any]]:
        """
        Perform the security scan using Bandit.
        
        Returns:
            List of vulnerabilities found
        """
        console.print(Panel(f"[bold green]Scanning [/]{self.target_path}", title="Seco Security Scanner"))
        
        # Run Bandit scan with JSON output
        with Progress() as progress:
            task = progress.add_task("[cyan]Running security scan...", total=100)
            
            try:
                # Run bandit with JSON output format using Python module
                result = subprocess.run(
                    ["python", "-m", "bandit", "-r", str(self.target_path), "-f", "json"],
                    capture_output=True,
                    text=True,
                    check=False
                )
                progress.update(task, completed=100)
            except subprocess.SubprocessError as e:
                console.print(f"[bold red]Error running bandit:[/] {str(e)}")
                return []
        
        try:
            scan_data = json.loads(result.stdout)
            self.results = [
                {
                    "filename": result["filename"],
                    "line_number": result["line_number"],
                    "issue_severity": result["issue_severity"],
                    "issue_confidence": result["issue_confidence"],
                    "issue_text": result["issue_text"],
                    "test_id": result["test_id"],
                    "test_name": result["test_name"],
                    "code": result.get("code", "")
                }
                for result in scan_data.get("results", [])
            ]
            return self.results
        except json.JSONDecodeError:
            console.print("[bold red]Error:[/] Failed to parse bandit output.")
            console.print(result.stdout)
            console.print(result.stderr)
            return []
    
    def display_results(self) -> None:
        """Display the scan results in the terminal using Rich."""
        if not self.results:
            console.print("[bold green]No security issues found![/]")
            return
        
        table = Table(title="Security Scan Results")
        table.add_column("Severity", style="bold")
        table.add_column("Confidence", style="bold")
        table.add_column("File", style="cyan")
        table.add_column("Line", style="magenta")
        table.add_column("Issue", style="yellow")
        
        for result in self.results:
            severity = result["issue_severity"]
            severity_style = {
                "HIGH": "[bold red]HIGH[/]",
                "MEDIUM": "[bold yellow]MEDIUM[/]",
                "LOW": "[bold green]LOW[/]"
            }.get(severity, severity)
            
            confidence = result["issue_confidence"]
            confidence_style = {
                "HIGH": "[bold red]HIGH[/]",
                "MEDIUM": "[bold yellow]MEDIUM[/]",
                "LOW": "[bold green]LOW[/]"
            }.get(confidence, confidence)
            
            table.add_row(
                severity_style,
                confidence_style,
                str(result["filename"]),
                str(result["line_number"]),
                result["issue_text"]
            )
        
        console.print(table)
        console.print(f"[bold]Total issues found:[/] {len(self.results)}")
    
    def export_results(self) -> None:
        """Export the scan results to a file in the specified format."""
        if not self.output_format or not self.output_file:
            return
        
        if not self.results:
            console.print("[yellow]No results to export.[/]")
            return
        
        output_path = Path(self.output_file)
        
        try:
            if self.output_format.lower() == "json":
                with open(output_path, "w") as f:
                    json.dump({
                        "scan_info": {
                            "date": datetime.now().isoformat(),
                            "target": str(self.target_path)
                        },
                        "results": self.results
                    }, f, indent=2)
            
            elif self.output_format.lower() == "html":
                html_content = self._generate_html_report()
                with open(output_path, "w") as f:
                    f.write(html_content)
            
            else:
                console.print(f"[bold red]Error:[/] Unsupported output format: {self.output_format}")
                return
            
            console.print(f"[bold green]Results exported to:[/] {output_path}")
        
        except Exception as e:
            console.print(f"[bold red]Error exporting results:[/] {str(e)}")
    
    def _generate_html_report(self) -> str:
        """
        Generate an HTML report from the scan results.
        
        Returns:
            HTML content as a string
        """
        severity_colors = {
            "HIGH": "red",
            "MEDIUM": "orange",
            "LOW": "green"
        }
        
        issues_html = ""
        for result in self.results:
            severity = result["issue_severity"]
            severity_color = severity_colors.get(severity, "black")
            
            issues_html += f"""
            <tr>
                <td style="color: {severity_color}; font-weight: bold;">{severity}</td>
                <td>{result["issue_confidence"]}</td>
                <td>{result["filename"]}</td>
                <td>{result["line_number"]}</td>
                <td>{result["issue_text"]}</td>
                <td>{result["test_id"]}</td>
            </tr>
            """
        
        html = f"""<!DOCTYPE html>
        <html>
        <head>
            <title>Seco Security Scan Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                h1 {{ color: #2c3e50; }}
                table {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                th {{ background-color: #2c3e50; color: white; }}
                tr:nth-child(even) {{ background-color: #f2f2f2; }}
                .info {{ background-color: #eef; padding: 10px; border-radius: 5px; }}
            </style>
        </head>
        <body>
            <h1>Seco Security Scan Report</h1>
            <div class="info">
                <p><strong>Date:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                <p><strong>Target:</strong> {str(self.target_path)}</p>
                <p><strong>Total Issues:</strong> {len(self.results)}</p>
            </div>
            
            <h2>Issues Found</h2>
            <table>
                <tr>
                    <th>Severity</th>
                    <th>Confidence</th>
                    <th>File</th>
                    <th>Line</th>
                    <th>Issue</th>
                    <th>Test ID</th>
                </tr>
                {issues_html}
            </table>
        </body>
        </html>
        """
        return html


def main():
    """Main function for the Seco security scanner."""
    parser = argparse.ArgumentParser(description="Seco - Code Security Scanner")
    parser.add_argument("path", help="Path to the directory to scan")
    parser.add_argument(
        "--output", "-o",
        choices=["json", "html"],
        help="Output format for the report (json or html)"
    )
    parser.add_argument(
        "--file", "-f",
        help="Output file path for the report"
    )
    
    args = parser.parse_args()
    
    # If output format is specified but file is not, create a default filename
    if args.output and not args.file:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        args.file = f"seco_report_{timestamp}.{args.output}"
    
    # Ensure that if file is specified, output format is also specified
    if args.file and not args.output:
        extension = os.path.splitext(args.file)[1].lstrip(".")
        if extension in ["json", "html"]:
            args.output = extension
        else:
            console.print("[bold red]Error:[/] Output format must be specified with --output when using --file")
            sys.exit(1)
    
    # Create and run the scanner
    scanner = SecurityScan(args.path, args.output, args.file)
    scanner.scan()
    scanner.display_results()
    
    if args.output:
        scanner.export_results()


if __name__ == "__main__":
    main()