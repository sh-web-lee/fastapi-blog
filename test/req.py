import requests
import json


data = {
    "email":"cheng@test.com",
    "password":"123"
}
resp = requests.post('http://127.0.0.1:8000/u/login', data=json.dumps(data))
print(resp.text)