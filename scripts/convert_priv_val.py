import json
import sys
import base64
from eth_utils import keccak

def convert_priv_validator_key(file_path):
    try:
        # Read the JSON file
        with open(file_path, 'r') as file:
            priv_validator_key = json.load(file)

        # Extract the public key in Base64 format
        pub_key_base64 = priv_validator_key['pub_key']['value']

        # Decode Base64 to bytes and convert to hexadecimal
        pub_key_bytes = base64.b64decode(pub_key_base64)
        pub_key_hex = f"0x{pub_key_bytes.hex()}"  # Add 0x prefix

        # Calculate the Ethereum address (signer)
        # Step 1: Remove the first byte of the public key
        compressed_pub_key_bytes = pub_key_bytes[1:]

        # Step 2: Compute the Keccak-256 hash
        hashed_pub_key = keccak(compressed_pub_key_bytes)

        # Step 3: Take the last 20 bytes
        signer = "0x" + hashed_pub_key[-20:].hex()

        # Create the output
        result = {
            "pubKey": pub_key_hex,
            "signer": signer
        }

        # Print the result in JSON format
        print(json.dumps(result, indent=4))

    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except KeyError as e:
        print(f"Error: Missing key in the JSON file - {e}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <json_file_path>")
    else:
        file_path = sys.argv[1]
        convert_priv_validator_key(file_path)
