from scripts.helpful_scripts import get_account, OPENSEA_URL
from brownie import AdvanceCollectible
from brownie import network


def main():
    account = get_account()
    advance_collectible = AdvanceCollectible[-1]
    tx = advance_collectible.createCollectible({"from": account})
    tx.wait(1)
    print(
        f"Awesome, you can view your NFT at {OPENSEA_URL.format(network.show_active(), advance_collectible.address, advance_collectible.tokenCounter() - 1)}")
