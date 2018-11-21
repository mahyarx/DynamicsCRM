from flask import Flask
from flask import jsonify
from flask import request
import requests
from requests_ntlm import HttpNtlmAuth
import json

def conadd( str ):
    userpassword = 'PASSWORD'
    payload = {"name": "Mahyar TajDini"}
    crmwebapi = 'http://URL/ORGANIZATION/api/data/v8.0/'
    crmrequestheaders = {
        'OData-MaxVersion': '4.0',
        'OData-Version': '4.0',
        'Accept': 'application/json',
        'Content-Type': 'application/json; charset=utf-8',
        'Prefer': 'odata.maxpagesize=500',
        'Prefer': 'odata.include-annotations=OData.Community.Display.V1.FormattedValue',
        }
    username = 'DOMAIN\\USERNAME'
    payload = str
    crmins = requests.post(crmwebapi+'/accounts',data=json.dumps(payload),auth=HttpNtlmAuth(username, userpassword),headers=crmrequestheaders)
    return crmins
		
app = Flask(__name__)
	
@app.route('/v2/api/', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        content = request.get_json()
        response = conadd (content)
        return str(response)

    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"

if __name__ == "__main__":
    app.run(debug=True)
	
