from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3 import Web3
import json
import argparse
from datetime import datetime, timezone

def create_keystore(private_key: str, password: str) -> None:
    # Remove '0x' if present
    private_key = private_key.replace('0x', '')
    
    # Create the account
    account: LocalAccount = Account.from_key(private_key)
    
    # Generate the keystore
    encrypted = Account.encrypt(private_key, password)
    
    # Generate timestamp in the correct format
    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H-%M-%S.%f')[:-3] + 'Z'
    
    # Remove '0x' from the address if present
    address = account.address.lower().replace('0x', '')
    
    # Create the filename in the required format
    keystore_file = f"out/UTC--{timestamp}--{address}"
    
    with open(keystore_file, 'w') as f:
        json.dump(encrypted, f)
    
    print(f"Keystore created: {keystore_file}")

def main():
    parser = argparse.ArgumentParser(description='Create an Ethereum keystore from a private key')
    parser.add_argument('--private-key', '-k', required=True, help='Ethereum private key')
    parser.add_argument('--password', '-p', required=False, help='Password to encrypt the keystore')
    
    args = parser.parse_args()
    create_keystore(args.private_key, args.password or '')

if __name__ == "__main__":
    main()
