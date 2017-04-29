# unzipping using zipfile
    
print "Hello World!\n"
import zipfile 
import urllib, json
url = "https://data.police.uk/api/forces"
print url
zipped = 'https://data.police.uk/data/archive/2016-01.zip'
zip_ref = zipfile.ZipFile(zipped, 'r')
directory_to_extract_to = ''
zip_ref.extractall(directory_to_extract_to)
zip_ref.close()
