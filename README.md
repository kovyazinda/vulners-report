# vulners-report
Queries Vulners DB and reports found CVE by defined criteria such Product and Version to MS Excel. Please, register at https://vulners.com to receive API key and update variable vulners_api = vulners.Vulners(api_key="123456")

Usage:
 python3 vuln-single-pub.py -p <ProductName> -v <Version> -l <LineCount> -f somefile.xlsx

Example:
 python3 vuln-single-pub.py -p "Windows Server" -v "2019"  -l 50 -o testwin.xlsx
