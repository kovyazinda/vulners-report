import vulners
import sys
import getopt
import re
import json
import xlsxwriter

def main(argv):


 try:
  opts, args = getopt.getopt(argv,"hp:v:l:o:")
#  print opts
 except getopt.GetoptError:
  print ('test.py -p <product> -v <version> -l <recordlimit> -o filename.xlsx')
  sys.exit(2)
 for opt, arg in opts:

  if opt == '-h':
   print ('test.py -p <product> -v <version> -l <recordlimit> -o filename.xlsx')
   sys.exit()
  elif opt in ("-p"):
   product_name = arg
  elif opt in ("-v"):
   product_version = arg
  elif opt in ("-l"):
   record_limit = int(arg)
  elif opt in ("-o"):
   outputfile = arg

 print ('Product:', product_name)
 print ('Version:', product_version)
 print ('Record Limit:', record_limit)
 print ('Outputfile:', outputfile)

 vulners_api = vulners.Vulners(api_key="123456")

# results = vulners_api.softwareVulnerabilities(product_name, product_version)
# exploit_list = results.get('exploit')
# vulnerabilities_list = [results.get(key) for key in results if key not in ['info', 'blog', 'bugbounty','nessus','openvas']]

 if record_limit:
  product_search = vulners_api.search(product_name+" "+product_version, limit=record_limit)
 else:
  product_search = vulners_api.search(product_name+" "+product_version, limit=10)

 if outputfile:
# Writing to excel
  workbook = xlsxwriter.Workbook(outputfile)
  worksheet = workbook.add_worksheet()

#apply default row height
  worksheet.set_default_row(70)

#applying cell format
  cell_format_header = workbook.add_format({'bold': True, 'font_color': 'black'})
  cell_format_normal = workbook.add_format({'bold': False, 'font_color': 'black', 'text_wrap' : True})
  cell_format_bad = workbook.add_format({'bold': False, 'font_color': 'black', 'bg_color': 'red','text_wrap' : True})

# writing column headers
  worksheet.write (0,0,"URL",cell_format_header)
  worksheet.write (0,1,"Title",cell_format_header)
  worksheet.write (0,2,"Description",cell_format_header)
  worksheet.write (0,3,"Type",cell_format_header)
  worksheet.write (0,4,"CVSS",cell_format_header)  
  
# to start writing to next rown
  rownum=1
 
# print ("Search:")

# print(product_search[0])
 search_string=json.dumps(product_search)

# regexp parsing
# procline = re.sub(r'\[', r'', search_string)
# procline = re.sub(r'\]', r'', procline)

# print line
# print procline

 search_json=json.loads(search_string)

# print type(search_json)

 for vulnerabilities in search_json:
  try:
#  search_json=json.loads(procline) 
   valuearr=[vulnerabilities["vhref"],vulnerabilities["title"],vulnerabilities["description"],vulnerabilities["type"],str(vulnerabilities["cvss"]["score"])]

   colnum=0
   for colvalue in valuearr:
    worksheet.write (rownum,colnum,colvalue,cell_format_normal)  
    colnum=colnum+1  

# incrementing row
   rownum=rownum+1
  except:
   try:
    print (vulnerabilities["vhref"]+" "+vulnerabilities["title"]+" "+vulnerabilities["description"]+" "+vulnerabilities["type"]+" "+str(vulnerabilities["cvss"]["score"]))
   except:
    pass
 
 workbook.close()
#  print(procline)
#   print ("Something wrong")

# regexp parsing
# line = re.sub(r"u'", r'"', str(product_search[0]))
# line = re.sub(r"'", r'"', line)
# print line

# m = re.findall(r"u'[a..z]++'", product_search[0])
# if m:
#  print(re.group(1))

if __name__ == "__main__":
   main(sys.argv[1:])
