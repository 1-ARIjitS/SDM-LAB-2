import requests

graphdb_url = "http://localhost:7200/rest/repositories"

repository_name = "sdm_lab_2"
repository_payload = {
    "id": repository_name,
    "location": "",
    "title": "SDM Lab 2 Repository",
    "type": "free",
    "params": {
        "ruleset": "rdfsplus", 
        "disable-context-index": "false",
        "storage-folder": "",
        "enable-context-index": "true"
    }
}

headers = {"Content-Type": "application/json"}
response = requests.post(graphdb_url, json=repository_payload, headers=headers)

if response.status_code == 201:
    print(f"Repository '{repository_name}' created successfully.")
else:
    print(f"Failed to create repository. Status code: {response.status_code}, Message: {response.text}")
