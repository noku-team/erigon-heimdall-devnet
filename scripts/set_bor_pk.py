import json
import base64
import binascii
import sys

def convert_validator_key(json_file_path):
    try:
        # Read the JSON file
        with open(json_file_path, 'r') as file:
            key_data = json.load(file)
        
        # Extract the private key in base64
        base64_key = key_data['priv_key']['value']
        
        # Decode from base64 and convert to hex
        decoded = base64.b64decode(base64_key)
        hex_key = binascii.hexlify(decoded).decode('utf-8')
        
        print(f"Validator address: {key_data['address']}")
        print(f"Private key (hex): {hex_key}")
        
        # Create the file for Bor key import
        with open('out/privatekey.txt', 'w') as f:
            f.write(hex_key)
        
        print("\nFile 'out/privatekey.txt' successfully created.")
        print("\nTo import the key into Bor, run:")
        print(f"./bin/bor --datadir ./erigon_data/bor_datadir_1 account import scripts/out/privatekey.txt")
        print("\nAfter the import, delete the file 'out/privatekey.txt'.")

    except FileNotFoundError:
        print(f"Error: File {json_file_path} not found")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: The file {json_file_path} is not a valid JSON")
        sys.exit(1)
    except KeyError as e:
        print(f"Error: Key {e} not found in JSON")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py path/to/priv_validator_key.json")
        sys.exit(1)
    
    convert_validator_key(sys.argv[1])
