# import requests
# import json

# def pin_to_ipfs(data):
#  assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
#  #YOUR CODE HERE
# url = "https://api.pinata.cloud/pinning/pinJSONToIPFS'"

# headers = {
#     "Content-Type": "application/json",
#     "pinata_api_key": "50805c212bce9f9a5058",
# }

# response = requests.post(url, headers = headers, json = data)

# if response.status_code == 200:
#     cid = response.json()["IpfHash"]
#     return cid
# else:
#     raise Exception(f"Error pinning to IPFS: {response.content}")
# #  return cid


# def get_from_ipfs(cid,content_type="json"):
#  assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
#  #YOUR CODE HERE
# url = f"https://gateway.pinata.cloud/ipfs/{cid}"
# response = requests.get(url)

# if response.status_code == 200:
#     if content_type == "json":
#         data = response.json()
#         assert isinstance(data,dict), f"get_from_ipfs should return a dict"
#         return data
#     else:
#         raise Exception(f"Unsupported content type: {content_type}")
# else:
#     raise Exception(f"Error fetching from IPFS: {response.content}")

# if __name__ == "__main__":
#     test_data = {"name": "Bored Ape", "description": "Test Data"}

#     cid = pin_to_ipfs(test_data)
#     retrieved_data = get_from_ipfs(cid)

# import requests
# import json

# Pinata_api_key = '50805c212bce9f9a5058'

# def pin_to_ipfs(data):
#     assert isinstance(data, dict), "Error pin_to_ipfs expects a dictionary"
    

#     url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
    
   
#     headers = {
#         "Content-Type": "application/json",
#         "pinata_api_key": Pinata_api_key
#     }
    
   
#     response = requests.post(url, headers=headers, json=data)
    
    
#     if response.status_code == 200:
        
#         cid = response.json()["IpfsHash"]
#         return cid
#     else:
#         raise Exception(f"Error pinning to IPFS: {response.content}")

# def get_from_ipfs(cid, content_type="json"):
#     assert isinstance(cid, str), "get_from_ipfs accepts a cid in the form of a string"
    
   
#     url = f"https://gateway.pinata.cloud/ipfs/{cid}"
    
  
#     response = requests.get(url)
    
    
#     if response.status_code == 200:
#         if content_type == "json":
            
#             data = response.json()
#             assert isinstance(data, dict), "get_from_ipfs should return a dict"
#             return data
#         else:
#             raise Exception(f"Unsupported content type: {content_type}")
#     else:
#         raise Exception(f"Error fetching from IPFS: {response.content}")


# if __name__ == "__main__":
#     test_data = {"name": "Bored Ape", "description": "Test Data"}
    
    
#     cid = pin_to_ipfs(test_data)
#     print(f"Data pinned to IPFS with CID: {cid}")
    
  
#     retrieved_data = get_from_ipfs(cid)
#     print(f"Data retrieved from IPFS: {retrieved_data}")

# import requests
# import json

# # Ensure the API key is defined as a string
# pinata_api_key = '50805c212bce9f9a5058'

# def pin_to_ipfs(data):
#     assert isinstance(data, dict), "Error pin_to_ipfs expects a dictionary"
    
#     url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
    
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {pinata_api_key}"
#     }
    
#     response = requests.post(url, headers=headers, json=data)
    
#     if response.status_code == 200:
#         cid = response.json()["IpfsHash"]
#         return cid
#     else:
#         raise Exception(f"Error pinning to IPFS: {response.content}")

# def get_from_ipfs(cid, content_type="json"):
#     assert isinstance(cid, str), "get_from_ipfs accepts a cid in the form of a string"
    
#     url = f"https://gateway.pinata.cloud/ipfs/{cid}"
    
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         if content_type == "json":
#             data = response.json()
#             assert isinstance(data, dict), "get_from_ipfs should return a dict"
#             return data
#         else:
#             raise Exception(f"Unsupported content type: {content_type}")
#     else:
#         raise Exception(f"Error fetching from IPFS: {response.content}")

# if __name__ == "__main__":
#     test_data = {"name": "Bored Ape", "description": "Test Data"}
    
#     cid = pin_to_ipfs(test_data)
#     print(f"Data pinned to IPFS with CID: {cid}")
    
#     retrieved_data = get_from_ipfs(cid)
#     print(f"Data retrieved from IPFS: {retrieved_data}")

# import requests
# import json

# pinata_api_key = '09e278d268fd8cafef67'  # Replace with your actual Pinata API key

# def pin_to_ipfs(data):
#     assert isinstance(data, dict), "Error pin_to_ipfs expects a dictionary"

#     url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"

#     payload = {
#         "pinataMetadata": {
#             "name": "Pinnie.json"
#         },
#         "pinataOptions": {
#             "cidVersion": 1
#         },
#         "pinataContent": data
#     }

#     headers = {
#         "Authorization": f"Bearer {pinata_api_key}",
#         "Content-Type": "application/json"
#     }

#     response = requests.post(url, json=payload, headers=headers)

#     if response.status_code == 200:
#         cid = response.json()["IpfsHash"]
#         return cid
#     else:
#         raise Exception(f"Error pinning to IPFS: {response.content}")

# def get_from_ipfs(cid, content_type="json"):
#     assert isinstance(cid, str), "get_from_ipfs accepts a cid in the form of a string"

#     url = f"https://gateway.pinata.cloud/ipfs/{cid}"

#     response = requests.get(url)

#     if response.status_code == 200:
#         if content_type == "json":
#             data = response.json()
#             assert isinstance(data, dict), "get_from_ipfs should return a dict"
#             return data
#         else:
#             raise Exception(f"Unsupported content type: {content_type}")
#     else:
#         raise Exception(f"Error fetching from IPFS: {response.content}")

# if __name__ == "__main__":
#     test_data = {"name": "Bored Ape", "description": "Test Data"}

#     cid = pin_to_ipfs(test_data)
#     print(f"Data pinned to IPFS with CID: {cid}")

#     retrieved_data = get_from_ipfs(cid)
#     print(f"Data retrieved from IPFS: {retrieved_data}")

import requests
import json

pinata_api_key = '09e278d268fd8cafef67'  

def pin_to_ipfs(data):
    assert isinstance(data, dict), "Error pin_to_ipfs expects a dictionary"

    url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"

    payload = {
        "pinataMetadata": {
            "name": "PinnedData.json"
        },
        "pinataOptions": {
            "cidVersion": 1
        },
        "pinataContent": data
    }

    headers = {
        "Authorization": f"Bearer {pinata_api_key}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        cid = response.json()["IpfsHash"]
        return cid
    else:
        raise Exception(f"Error pinning to IPFS: {response.content}")

def get_from_ipfs(cid, content_type="json"):
    assert isinstance(cid, str), "get_from_ipfs accepts a cid in the form of a string"

    url = f"https://gateway.pinata.cloud/ipfs/{cid}"

    response = requests.get(url)

    if response.status_code == 200:
        if content_type == "json":
            data = response.json()
            assert isinstance(data, dict), "get_from_ipfs should return a dict"
            return data
        else:
            raise Exception(f"Unsupported content type: {content_type}")
    else:
        raise Exception(f"Error fetching from IPFS: {response.content}")

# Example usage
if __name__ == "__main__":
    test_data = {"name": "Bored Ape", "description": "Test Data"}

    try:
        cid = pin_to_ipfs(test_data)
        print(f"Data pinned to IPFS with CID: {cid}")

        retrieved_data = get_from_ipfs(cid)
        print(f"Data retrieved from IPFS: {retrieved_data}")
    except Exception as e:
        print(f"Error: {e}")



