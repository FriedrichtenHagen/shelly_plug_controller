import requests

# https://shelly-api-docs.shelly.cloud/gen2/ComponentsAndServices/Switch

url = "http://192.168.178.56/rpc/Switch.Toggle?id=0"
params = {"param1": "value1", "param2": "value2"}
response = requests.get(url, params=params)

if response.status_code == 200:
    print("Request was successful!")
    print(response.text)
else:
    print(f"Request failed with status code {response.status_code}")
