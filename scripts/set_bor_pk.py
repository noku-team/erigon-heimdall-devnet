import json
import base64
import binascii
import sys

def convert_validator_key(json_file_path):
    try:
        # Leggi il file JSON
        with open(json_file_path, 'r') as file:
            key_data = json.load(file)
        
        # Estrai la chiave privata in base64
        base64_key = key_data['priv_key']['value']
        
        # Decodifica da base64 e converti in hex
        decoded = base64.b64decode(base64_key)
        hex_key = binascii.hexlify(decoded).decode('utf-8')
        
        print(f"Indirizzo validatore: {key_data['address']}")
        print(f"Chiave privata (hex): {hex_key}")
        
        # Crea il file per l'importazione in Bor
        with open('out/privatekey.txt', 'w') as f:
            f.write(hex_key)
        
        print("\nFile 'out/privatekey.txt' creato con successo.")
        print("\nPer importare la chiave in Bor, esegui:")
        print(f"./bin/bor/bor --datadir ./erigon_data/datadir_1 account import scripts/out/privatekey.txt")
        print("\nDopo l'importazione, elimina il file out/privatekey.txt")
        
        # Crea anche il comando completo per avviare Bor
        bor_command = f"""./bin/bor/bor \\
  --datadir ./erigon_data/datadir_1 \\
  --chain ./erigon_data/genesis.json \\
  --mine \\
  --miner.validator "0x{key_data['address'].lower()}" \\
  --miner.gaslimit "30000000" \\
  --unlock "0x{key_data['address'].lower()}" \\
  --password password.txt \\
  --allow-insecure-unlock"""
        
        print("\nComando per avviare Bor:")
        print(bor_command)

    except FileNotFoundError:
        print(f"Errore: File {json_file_path} non trovato")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Errore: Il file {json_file_path} non è un JSON valido")
        sys.exit(1)
    except KeyError as e:
        print(f"Errore: Chiave {e} non trovata nel JSON")
        sys.exit(1)
    except Exception as e:
        print(f"Errore: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py path/to/priv_validator_key.json")
        sys.exit(1)
    
    convert_validator_key(sys.argv[1])