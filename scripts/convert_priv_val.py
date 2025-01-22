import json
import sys
import base64
from eth_utils import keccak

def convert_priv_validator_key(file_path):
    try:
        # Leggi il file JSON
        with open(file_path, 'r') as file:
            priv_validator_key = json.load(file)

        # Estrarre chiave pubblica in formato Base64
        pub_key_base64 = priv_validator_key['pub_key']['value']

        # Decodificare Base64 in byte e convertire in esadecimale
        pub_key_bytes = base64.b64decode(pub_key_base64)
        pub_key_hex = f"0x{pub_key_bytes.hex()}"  # Aggiungi prefisso 0x

        # Calcolare l'indirizzo Ethereum (signer)
        # Passo 1: Rimuovi il primo byte della chiave pubblica
        compressed_pub_key_bytes = pub_key_bytes[1:]

        # Passo 2: Calcola il Keccak-256 hash
        hashed_pub_key = keccak(compressed_pub_key_bytes)

        # Passo 3: Prendi gli ultimi 20 byte
        signer = "0x" + hashed_pub_key[-20:].hex()

        # Creare l'output
        result = {
            "pubKey": pub_key_hex,
            "signer": signer
        }

        # Stampare il risultato in formato JSON
        print(json.dumps(result, indent=4))

    except FileNotFoundError:
        print(f"Errore: Il file {file_path} non esiste.")
    except KeyError as e:
        print(f"Errore: Chiave mancante nel file JSON - {e}")
    except Exception as e:
        print(f"Errore: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <percorso_file_json>")
    else:
        file_path = sys.argv[1]
        convert_priv_validator_key(file_path)
