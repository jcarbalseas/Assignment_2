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

# import requests
# import json

# pinata_api_key = '09e278d268fd8cafef67'  

# def pin_to_ipfs(data):
#     assert isinstance(data, dict), "Error pin_to_ipfs expects a dictionary"

#     url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"

#     payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"\r\n\r\nreadstream\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"pinataMetadata\"\r\n\r\n{\n  \"name\": \"Pinnie.json\"\n}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"pinataOptions\"\r\n\r\n{\n  \"cidVersion\": 1\n}\r\n-----011000010111000001101001--\r\n\r\n"
#     headers = {
#         "Authorization": "Bearer <token>",
#         "Content-Type": "multipart/form-data"
#     }

#     response = requests.request("POST", url, data=payload, headers=headers)

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

#     try:
#         cid = pin_to_ipfs(test_data)
#         print(f"Data pinned to IPFS with CID: {cid}")

#         retrieved_data = get_from_ipfs(cid)
#         print(f"Data retrieved from IPFS: {retrieved_data}")
#     except Exception as e:
#         print(f"Error: {e}")


# import requests
# import json

# pinata_api_key = '09e278d268fd8cafef67'  

# def pin_to_ipfs(data):
#     assert isinstance(data, dict), "Error pin_to_ipfs expects a dictionary"

#     url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"

#     # payload = {
#     #     "pinataMetadata": {
#     #         "name": "PinnedData.json"
#     #     },
#     #     "pinataOptions": {
#     #         "cidVersion": 1
#     #     },
#     #     "pinataContent": data
#     # }

#     # headers = {
#     #     "Authorization": f"Bearer {pinata_api_key}",
#     #     "Content-Type": "application/json"
#     # }

#     # response = requests.post(url, json=payload, headers=headers)

#     payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"\r\n\r\nreadstream\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"pinataMetadata\"\r\n\r\n{\n  \"name\": \"Pinnie.json\"\n}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"pinataOptions\"\r\n\r\n{\n  \"cidVersion\": 1\n}\r\n-----011000010111000001101001--\r\n\r\n"
#     headers = {
#         "Authorization": "Bearer <eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiIyNmM1NmJjMS0yNGY0LTQ0ZjQtYjA0MC04N2ZjOGY4OTA5NmQiLCJlbWFpbCI6ImpjYXJiYWxAc2Vhcy51cGVubi5lZHUiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicGluX3BvbGljeSI6eyJyZWdpb25zIjpbeyJkZXNpcmVkUmVwbGljYXRpb25Db3VudCI6MSwiaWQiOiJGUkExIn0seyJkZXNpcmVkUmVwbGljYXRpb25Db3VudCI6MSwiaWQiOiJOWUMxIn1dLCJ2ZXJzaW9uIjoxfSwibWZhX2VuYWJsZWQiOmZhbHNlLCJzdGF0dXMiOiJBQ1RJVkUifSwiYXV0aGVudGljYXRpb25UeXBlIjoic2NvcGVkS2V5Iiwic2NvcGVkS2V5S2V5IjoiMTRiMWQ2Zjc3MTYwY2I0MTJkODkiLCJzY29wZWRLZXlTZWNyZXQiOiI1MDczNGZmMmI2MjMzM2Q3ZGQwNmM1OTNkOTE5Mjg0YmVkYjRkZDM1OWJkZjYxYzJjZTFjMzg0ZDA4MmY1YTJiIiwiZXhwIjoxNzUxMzk2Mjk5fQ.w4GB3zPx0m3tQH8DcI5uMvgQvcnP-t1suAKhQwR8WK8>",
#         "Content-Type": "multipart/form-data"
#     }

#     response = requests.request("POST", url, data=payload, headers=headers)

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

#     try:
#         cid = pin_to_ipfs(test_data)
#         print(f"Data pinned to IPFS with CID: {cid}")

#         retrieved_data = get_from_ipfs(cid)
#         print(f"Data retrieved from IPFS: {retrieved_data}")
#     except Exception as e:
#         print(f"Error: {e}")

# import requests
# import json

# PINATA_API_KEY = '14b1d6f77160cb412d89'
# PINATA_SECRET_API_KEY = '50734ff2b62333d7dd06c593d919284bedb4dd359bdf61c2ce1c384d082f5a2b'

# def pin_to_ipfs(data):
#     assert isinstance(data, dict), f"Error pin_to_ipfs expects a dictionary"
    
#     url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
#     headers = {
#         "pinata_api_key": PINATA_API_KEY,
#         "pinata_secret_api_key": PINATA_SECRET_API_KEY
#     }
#     response = requests.post(url, json=data, headers=headers)
#     if response.status_code == 200:
#         cid = response.json()["IpfsHash"]
#         return cid
#     else:
#         raise Exception(f"Error pinning to IPFS: {response.status_code} {response.text}")

# def get_from_ipfs(cid, content_type="json"):
#     assert isinstance(cid, str), f"get_from_ipfs accepts a cid in the form of a string"
    
#     url = f"https://gateway.pinata.cloud/ipfs/{cid}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         assert isinstance(data, dict), f"get_from_ipfs should return a dict"
#         return data
#     else:
#         raise Exception(f"Error fetching from IPFS: {response.status_code} {response.text}")

# # Example usage:
# data_to_pin = {
#     "name": "Bored Ape #489",
#     "description": "Bored Ape Yacht Club",
#     "image": "https://ipfs.io/ipfs/QmeSjSinHpPnmXmspMjwiXyN6zS4E9zccariGR3jxcaWtq/489.png"
# }

# # Pin the data to IPFS
# cid = pin_to_ipfs(data_to_pin)
# print("Pinned CID:", cid)

# # Retrieve the data from IPFS
# retrieved_data = get_from_ipfs(cid)
# print("Retrieved Data:", retrieved_data)

import requests
import json

# Replace these with your Pinata API key and secret
PINATA_API_KEY = 'YOUR_PINATA_API_KEY'
PINATA_SECRET_API_KEY = 'YOUR_PINATA_SECRET_API_KEY'

def pin_to_ipfs(data):
    assert isinstance(data, dict), f"Error pin_to_ipfs expects a dictionary"

    url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
    headers = {
        "Content-Type": "application/json",
        "cc7702120b0c25b5ebb3": PINATA_API_KEY,
        "aa66dd2d412cd48df633a5023e7fd4a59d181ca6a14897c70e0bbf5b56766593": PINATA_SECRET_API_KEY
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
