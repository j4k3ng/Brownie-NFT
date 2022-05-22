
from brownie import AdvanceCollectible
from brownie import network
from scripts.helpful_scripts import OPENSEA_URL, get_account


def main():
    print(f"Working on {network.show_active()}")
    advanced_collectible = AdvanceCollectible[-1]
    number_of_collectibles = advanced_collectible.tokenCounter()
    print(f"You have {number_of_collectibles} tokenIds")
    for token_id in range(number_of_collectibles):
        if not advanced_collectible.tokenURI(token_id).startswith("https://"):
            print(f"Setting tokenURI of {token_id}")
            metadata = "./metadata/{network.show_active()}/{token_id}.json"
            set_tokenURI(token_id, advanced_collectible, metadata)


def set_tokenURI(token_id, nft_contract, tokenURI):
    account = get_account()
    tx = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
    tx.wait(1)
    print(
        f"Awesome! You can view your NFT at {OPENSEA_URL.format(network.show_active(), nft_contract.address, token_id)}"
    )
    print("Please wait up to 20 minutes, and hit the refresh metadata button")
