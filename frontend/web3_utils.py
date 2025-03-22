from web3 import Web3
import os
import json

# Load environment variables
RPC_URL = os.getenv("ALCHEMY_RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")

web3 = Web3(Web3.HTTPProvider(RPC_URL))

# Load Contract ABI
with open("../blockchain/abi/Bounty.json") as f:
    contract_abi = json.load(f)

contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)
account = web3.eth.account.from_key(PRIVATE_KEY)

def submit_solution(bounty_id, solution_text):
    nonce = web3.eth.get_transaction_count(account.address)
    txn = contract.functions.submitSolution(bounty_id, solution_text).build_transaction({
        "from": account.address,
        "nonce": nonce,
        "gas": 2000000,
        "gasPrice": web3.eth.gas_price
    })

    signed_txn = web3.eth.account.sign_transaction(txn, PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return web3.to_hex(tx_hash)

def get_all_bounties():
    count = contract.functions.getBountyCount().call()
    bounties = []
    for i in range(count):
        bounty = contract.functions.bounties(i).call()
        bounties.append({
            "title": bounty[0],
            "description": bounty[1],
            "reward": web3.from_wei(bounty[2], "ether"),
            "creator": bounty[3]
        })
    return bounties