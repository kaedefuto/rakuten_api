# -*- coding: utf-8 -*-

import requests
list = []
list = "METAL GEAR SURVIVE"
url = 'https://app.rakuten.co.jp/services/api/BooksGame/Search/20170404'

payload = {
    'applicationId': [xxxxxxxxxxxxxxxxxxx],
    'hardware': "PS4",
    'sort': 'standard',
    #"title": "METAL GEAR SURVIVE"
    }

r = requests.get(url, params=payload)

resp = r.json()

print ("検索数",resp['pageCount'])

for i in resp['Items']:
    item = i['Item']
    print (item['title'])
    print (item['itemPrice'], '円')
    print (item["itemUrl"])
    print(item["jan"])
    print(item["largeImageUrl"])
    
