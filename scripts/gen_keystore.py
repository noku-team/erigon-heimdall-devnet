from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3 import Web3
import json
import argparse
from datetime import datetime, timezone

def create_keystore(private_key: str, password: str) -> None:
    # Rimuovi '0x' se presente
    private_key = private_key.replace('0x', '')
    
    # Crea l'account
    account: LocalAccount = Account.from_key(private_key)
    
    # Crea il keystore
    encrypted = Account.encrypt(private_key, password)
    
    # Genera il timestamp nel formato corretto
    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H-%M-%S.%f')[:-3] + 'Z'
    
    # Rimuovi '0x' dall'indirizzo se presente
    address = account.address.lower().replace('0x', '')
    
    # Crea il nome del file nel formato richiesto
    keystore_file = f"out/UTC--{timestamp}--{address}"
    
    with open(keystore_file, 'w') as f:
        json.dump(encrypted, f)
    
    print(f"Keystore creato: {keystore_file}")

def main():
    parser = argparse.ArgumentParser(description='Crea un keystore Ethereum da private key')
    parser.add_argument('--private-key', '-k', required=True, help='Private key Ethereum')
    parser.add_argument('--password', '-p', required=False, help='Password per crittografare il keystore')
    
    args = parser.parse_args()
    create_keystore(args.private_key, args.password or '')

if __name__ == "__main__":
    main()
