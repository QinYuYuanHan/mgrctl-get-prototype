import json

def fetch_resource(resource):
    with open("mock_data.json") as f:
        data = json.load(f)
    return data.get(resource, [])
