import os
from dotenv import load_dotenv

load_dotenv()

CONFIG = {
    "ALCHEMY_RPC_URL": os.getenv("ALCHEMY_RPC_URL"),
    "PRIVATE_KEY": os.getenv("PRIVATE_KEY"),
    "CONTRACT_ADDRESS": os.getenv("CONTRACT_ADDRESS")
}