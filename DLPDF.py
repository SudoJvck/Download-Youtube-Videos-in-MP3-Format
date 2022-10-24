#Download & Save PDF Files

import urllib.request
url=input("Enter Link to Download PDF : ")
Name=input("Enter a Name for the PDF File : ")
FileName = Name+".pdf"
urllib.request.urlretrieve(url,FileName)
