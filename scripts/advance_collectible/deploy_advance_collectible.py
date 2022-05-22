from scripts.helpful_scripts import get_account
from brownie import AdvanceCollectible
from brownie import network

def main():
    account = get_account()
    advance_collectible = AdvanceCollectible.deploy({"from": account})