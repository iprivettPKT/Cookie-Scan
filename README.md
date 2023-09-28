# Cookie-Scan

Cookie Scan is a Python tool designed to automate the process of fetching cookies from a list of domains using Playwright. It provides an intuitive interface to view details of cookies such as their names, security attributes, and expiry.

# Features
Fetch cookies from multiple domains in a batch.
Detailed cookie attributes: Domain, Name, Secure, HttpOnly, and Expiry.
Colored terminal output for better visibility.
Uses the powerful Playwright library to simulate a real browser environment.
Installation

# Requirements
Python 3.8 or higher.
Playwright Python library.
Step-by-Step Installation:
Clone the Repository


```
git clone https://path-to-your-repo/cookie-scan.git
cd cookie-scan
```

Replace path-to-your-repo with your actual repository path if you're hosting this on a platform like GitHub.

# Set Up a Virtual Environment (Recommended)

```
python3 -m venv venv
source venv/bin/activate
```

# Install Required Python Libraries


```
pip install playwright
```

# Install Playwright Drivers


```
playwright install
```

# Usage

## Prepare Domains List

Create a domains.txt file in the root directory.
Add each domain you want to scan on a new line.

Example:

```
example.com
test.com
domain.org
```

# Run Cookie Scan

```
python cookiescan.py
```

Review Results

After processing, the tool will display a table of cookies for each domain. Review the results for cookie details.
 
# Troubleshooting
If you encounter any issues while using the tool, consider the following:

Ensure all dependencies are correctly installed.
Make sure you're using the supported Python version.
Check the domain format in domains.txt.
Run Playwright in non-headless mode (headless=False) for debugging.

# Contributing
If you'd like to contribute to Cookie Scan, feel free to fork the repository and submit a pull request!
