# vulners-report

Queries Vulners DB and reports found CVE by defined criteria such Product and Version to MS Excel. Please, register at https://vulners.com to receive API key and update variable vulners_api = vulners.Vulners(api_key="123456")

# Install modules via pip install <modulename> command

pip install vulners sys getopt re json xlsxwriter

# Usage:
 python3 vuln-cve-list-pub.py -i <innputfile.txt> -o <outputfile.xlsx>

# Example:
 python3 vuln-single-pub.py -i queries.txt -o test.xlsx
 
# Queries Example:

Sharepoint 2016

Moxa EDS*
