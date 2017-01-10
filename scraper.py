#import sqlite3
#connection = sqlite3.connect("company.db")

import scraperwiki
import lxml.html
import urllib, json

record = {}

url = "https://data.police.uk/api/forces"
response = urllib.urlopen(url)
data = json.loads(response.read())
#print data
for i in data:
    print i
    print i['name']
    record['idcode'] = i['id']
    record['fullname'] = i['name']
    if i['id'] == 'wiltshire':
        print 'THIS IS WILTSHIRE2'
    if 'wilt' in i['id']:
        print 'CONTAINS WILT'
    print record
    scraperwiki.sqlite.save(['id'], record)
