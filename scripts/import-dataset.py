#!/usr/bin/env python
# !pip install requests
import json
import requests

token = 'my-secret'
server_url = 'http://localhost:5000/api/action/package_create'

dataset_dict = {
    'name': 'my_dataset_names',
    'notes': 'A long description of my dataset',
    'owner_org': 'org-name'
}

headers = {'Authorization': token}
response = requests.post(server_url, data=dataset_dict, headers=headers)
response_json = json.loads(response.text)
assert response_json['success'] is True
