import requests
import json

def pin_to_ipfs(data):
    assert isinstance(data, dict), f"Error pin_to_ipfs expects a dictionary"

    url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
    headers = {
        "Content-Type": "application/json",
        "pinata_api_key": str('15483632193b7220ad68'), 
        "pinata_secret_api_key": str('5a8bb8c116af5a7532c3531f88fb71e8b537f254ac8678e7dc678b5a49fe86f4')
    }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        cid = response.json()["IpfsHash"]
        return cid
    else:
        raise Exception(f"Failed to pin to IPFS: {response.status_code}, {response.text}")

def get_from_ipfs(cid, content_type="json"):
    assert isinstance(cid, str), f"get_from_ipfs accepts a cid in the form of a string"

    url = f"https://gateway.pinata.cloud/ipfs/{cid}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        assert isinstance(data, dict), f"get_from_ipfs should return a dict"
        return data
    else:
        raise Exception(f"Failed to get from IPFS: {response.status_code}, {response.text}")
