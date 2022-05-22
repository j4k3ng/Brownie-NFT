from brownie import AdvanceCollectible
from brownie import network
from metadata.sample_metadata import metadata_template
from pathlib import Path
import requests
import json
import os

PINATA_BASE_URL = "https://api.pinata.cloud/"
endpoint = "pinning/pinFileToIPFS"
# Change this filepath
filepath = "./img/oga.jpg"
filename = filepath.split("/")[-1:][0]
headers = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_API_SECRET"),
}


def main():
    advanced_collectible = AdvanceCollectible[-1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(f"You have created {number_of_advanced_collectibles} collectibles!")
    for token_id in range(number_of_advanced_collectibles):
        metadata_file_name = (
            f"./metadata/{network.show_active()}/{token_id}.json"
        )
        collectible_metadata = metadata_template
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} already exists! Delete it to overwrite")
        else:
            print(f"Creating Metadata file: {metadata_file_name}")
            collectible_metadata["name"] = "OGA"
            collectible_metadata["description"] = f"An adorable OGA"
            image_path = "./img/oga.jpg"
            image_uri = upload_to_pinata(image_path)
            collectible_metadata["image"] = image_uri
            with open(metadata_file_name, "w") as file:
                json.dump(collectible_metadata, file)
            upload_to_pinata(metadata_file_name)


# curl -X POST -F file=@metadata/rinkeby/0-SHIBA_INU.json http://localhost:5001/api/v0/add


# def upload_to_ipfs(filepath):
#     with Path(filepath).open("rb") as fp:
#         image_binary = fp.read()
#         ipfs_url = "http://127.0.0.1:5001"
#         endpoint = "/api/v0/add"
#         response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
#         ipfs_hash = response.json()["Hash"]
#         # "./img/0-PUG.png" -> "0-PUG.png"
#         filename = filepath.split("/")[-1:][0]
#         image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
#         print(image_uri)
#         return image_uri

def upload_to_pinata(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        filename = filepath.split("/")[-1:][0] # + "-" + token_id
        response = requests.post(
            PINATA_BASE_URL + endpoint,
            files={"file": (filename, image_binary)},
            headers=headers,
        )
        response_json = response.json()
        print(response_json)
        print(response_json["IpfsHash"])
        image_uri = f"https://gateway.pinata.cloud/ipfs/{response_json['IpfsHash']}"
        print(image_uri)
        return image_uri 


