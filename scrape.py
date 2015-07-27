import urllib
import urllib2
import json
import unicodecsv

URL = "http://www.co-operative.coop/Controls/StoreFinder/storefinderservice.asmx/GetStoreInfoByID"

headers = [
('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:37.0) Gecko/20100101 Firefox/37.0'),
('Accept', 'application/json, text/javascript, */*; q=0.01'),
('Content-Type', 'application/json; charset=utf-8'),
('Pragma', 'no-cache'),
('X-Requested-With', 'XMLHttpRequest')
]
headers = dict(map(lambda x: (x[0], x[1]), headers))

csv_headers = ['id', 'Name', 'Mon', 'Tues', 'Weds', 'Thurs', 'Fri', 'Sat',
'Sun', 'Address_1', 'Address_2', 'Address_3', 'Address_4', 'Address_5',
'Postcode', 'Tel', 'type', 'part_of']
csvf = open("coop.csv", 'w')
csvout = unicodecsv.DictWriter(csvf, fieldnames=csv_headers)
csvout.writerow(dict(map(lambda k: (k,k), csv_headers)))

# Think they start at this number, but I could be wrong...
for store_id in range(3634501, 3649999):
    print store_id
    data = '{id:"%s"}' % store_id
    req = urllib2.Request(URL, data, headers)
    try:
        response = urllib2.urlopen(req)
    except urllib2.HTTPError:
        continue
    jsond = json.loads(response.read())

    td = json.loads(jsond['d'])[0]
    
    csvout.writerow({
        'id': td[0],
        'Name': td[3],
        'Mon': td[4],
        'Tues': td[5],
        'Weds': td[6],
        'Thurs': td[7],
        'Fri': td[8],
        'Sat': td[9],
        'Sun': td[10],
        'Address_1': td[11],
        'Address_2': td[12],
        'Address_3': td[13],
        'Address_4': td[14],
        'Address_5': td[15],
        'Postcode': td[16],
        'Tel': td[17],
        'type': td[29],
        'part_of': td[30],
    })
