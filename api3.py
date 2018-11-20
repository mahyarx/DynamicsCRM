#!/usr/bin/python
# -*- coding: utf-8 -*-
#Email : Mahyar@TajDini.net
#Web: Http://tajdini.net/resume

import requests
from requests_ntlm import HttpNtlmAuth
import json

username = 'AD_DOMAIN_NAME\\AD_USERNAME'
userpassword = 'PASSWORD'

    # set these values to query your crm data
payload = {"fullname": "Mah","firstname":"mahyar","lastname":"taj"}
crmwebapi = 'http://[URL]/[ORGANIZATION]/api/data/v8.2/'
crmwebapiquery = '/accounts?$select=name'

crmrequestheaders = {
    'OData-MaxVersion': '4.0',
    'OData-Version': '4.0',
    'Accept': 'application/json',
    'Content-Type': 'application/json; charset=utf-8',
    'Prefer': 'odata.maxpagesize=500',
    'Prefer': 'odata.include-annotations=OData.Community.Display.V1.FormattedValue',
    }

print ('making crm request . . .')
crmres = requests.get(crmwebapi + crmwebapiquery,
                      headers=crmrequestheaders,
                      auth=HttpNtlmAuth(username, userpassword))
print ('crm response received . . .')
print ('sending data...')

crmins=requests.post(crmwebapi+'/contacts',data=json.dumps(payload),auth=HttpNtlmAuth(username, userpassword),headers=crmrequestheaders)
print (crmins)
try:
    print ('parsing crm response . . .')
    crmresults = crmres.json()
    for x in crmresults['value']:
        print (x['name'])
except KeyError:
    print ('Could not parse CRM results')


