#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import hashlib

excel_file = './partners.xlsx'
pt = pd.read_excel(excel_file)
print(pt.head())

partners = set(pt['Partner'])

cities = set(pt["Contact address"].apply(lambda x: x.split()[-1])) | \
         set(pt["Delivery address"].apply(lambda x: x.split()[-1]))

streets = set(pt['Contact address'].apply(lambda x: (x.split())[0]+' '+(x.split())[-1])) | \
          set(pt['Delivery address'].apply(lambda x: (x.split())[0]+' '+(x.split())[-1]))

party_types = {'wholesaler', 'breeder', 'producer'}

truck_types = {'regular', 'massive'}

def hashInstances(file, baseURI, group):
	for i in group:
		file.write(f'<{baseURI}/{hashlib.md5(i.encode()).hexdigest()}> a <{baseURI}> . ({i})\n\n')

with open('thehappydog.txt', 'w+', encoding='utf-8') as f:
    hashInstances(f,'http://thehappydog.io/#le/legal_entity', partners)
    hashInstances(f,'http://thehappydog.io/#le/party_type', party_types)
    hashInstances(f,'http://thehappydog.io/#geo/city', cities)
    hashInstances(f,'http://thehappydog.io/#geo/street', streets)
    hashInstances(f,'http://thehappydog.io/#ast/truck_type', truck_types)
