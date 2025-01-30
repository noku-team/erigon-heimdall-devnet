# Convert Priv Validator Key to Ethereum Address

## Descrizione

`convert_priv_val.py` è uno script Python che converte una chiave pubblica contenuta in un file JSON di tipo `priv_validator_key` in due output principali:

- **pubKey**: La chiave pubblica in formato esadecimale con prefisso `0x`.
- **signer**: L'indirizzo Ethereum calcolato dalla chiave pubblica utilizzando l'hash Keccak-256.

## Prerequisiti

- Python 3.x

Per installare le dipendenze:

```bash
pip install -r requirements.txt
```

## Utilizzo

### 1. Formato del file JSON in input

Il file JSON deve avere il seguente formato:

```json
{
  "address": "048D975E40D9D9E8931B9EC38F404B8E36BE3218",
  "pub_key": {
    "type": "tendermint/PubKeySecp256k1",
    "value": "BDJF1m78p5iGCI4+RUprEqeAipRBVmokpJ2wYoR9ipdXNO9sgdn9FLU/TPRJn61REchsmRNyXnuTmXeHX91scSw="
  },
  "priv_key": {
    "type": "tendermint/PrivKeySecp256k1",
    "value": "<BASE_64>"
  }
}
```

- **`pub_key.value`**: Deve essere codificato in Base64.

### 2. Esecuzione dello script

Esegui lo script specificando il percorso del file JSON come parametro:

```bash
python convert_priv_val.py <path_to_json_file>
```

### 3. Output

Lo script stampa un oggetto JSON con i seguenti campi:

- **`pubKey`**: La chiave pubblica convertita in formato esadecimale.
- **`signer`**: L'indirizzo Ethereum derivato dalla chiave pubblica.

#### Esempio di output

```json
{
    "pubKey": "0x042425d66efca79886088e3e454a6b12a7808a9441566a24a49db062847d8a975734ef6c81d9fd14b53f4cf4499fad5111c86c9913725e7b939977875fdd6c712c",
    "signer": "0x048d975e40d9d9e8931b9ec38f404b8e36be3218"
}
```

## Note Tecniche

1. **Decodifica Base64**: La chiave pubblica viene prima decodificata da Base64 in byte.
2. **Conversione in formato esadecimale**: I byte vengono convertiti in formato esadecimale con prefisso `0x`.
3. **Calcolo dell'indirizzo Ethereum**:
   - Il primo byte della chiave pubblica viene rimosso (indicatore di compressione).
   - L'hash Keccak-256 viene calcolato sui byte rimanenti.
   - Gli ultimi 20 byte dell'hash vengono utilizzati come indirizzo Ethereum.

## Gestione degli errori

Lo script gestisce i seguenti errori:

- **File non trovato**: Mostra un messaggio d'errore se il file JSON specificato non esiste.
- **Chiavi mancanti**: Notifica l'assenza di campi obbligatori nel file JSON.
- **Errori generici**: Mostra dettagli dell'errore per facilitare il debug.

## Esempio di comando

```bash
python convert_priv_val.py priv_validator_key.json
```

# Polygon Validator Setup Tool

Questo strumento facilita la configurazione dei validatori per una rete Polygon, convertendo le chiavi private dal formato Heimdall al formato richiesto da Bor.

## Prerequisiti

- Python 3.6 o superiore
- File `priv_validator_key.json` generato da Heimdall
- Bor installato nel sistema

## Installazione

1. Clona o scarica questo repository
2. Non sono richieste dipendenze Python aggiuntive

## Utilizzo

### 1. Preparazione

Assicurati di avere il file `priv_validator_key.json` generato da Heimdall. Questo file ha solitamente questa struttura:

```json
{
  "address": "YOUR_VALIDATOR_ADDRESS",
  "pub_key": {
    "type": "tendermint/PubKeySecp256k1",
    "value": "BASE64_ENCODED_PUBLIC_KEY"
  },
  "priv_key": {
    "type": "tendermint/PrivKeySecp256k1",
    "value": "BASE64_ENCODED_PRIVATE_KEY"
  }
}
```

### 2. Conversione della Chiave

Esegui lo script passando il path del file JSON:

```bash
python convert_key.py path/to/priv_validator_key.json
```

Lo script:

- Legge il file JSON
- Converte la chiave privata da base64 a formato hex
- Crea un file `privatekey.txt` con la chiave convertita
- Mostra l'indirizzo del validatore
- Genera i comandi necessari per la configurazione di Bor

### 3. Configurazione di Bor

#### 1. Crea un file `password.txt` con una password sicura

```bash
echo "your_secure_password" > password.txt
```

#### 2. Importa la chiave privata in Bor usando il comando generato dallo script

```bash
./bin/bor account import -datadir ./erigon_data/bor_datadir_1 scripts/out/privatekey.txt
```

#### 3. Elimina il file privatekey.txt

```bash
rm out/privatekey.txt
```

#### 4. Avvia Bor usando il comando completo generato dallo script

```bash
./bin/bor \
  --datadir ./erigon_data/bor_datadir_1 \
  --chain ./erigon_data/genesis.json \
  --mine \
  --miner.validator "0xYOUR_VALIDATOR_ADDRESS" \
  --miner.gaslimit "30000000" \
  --unlock "0xYOUR_VALIDATOR_ADDRESS" \
  --password password.txt \
  --allow-insecure-unlockt
```

## Note sulla Sicurezza

- Mai condividere o esporre le chiavi private
- Eliminare immediatamente il file `privatekey.txt` dopo l'importazione
- Mantenere al sicuro il file `password.txt`
- Usare password diverse per ogni validatore
- Considerare l'uso di un key management system in produzione

## Struttura del file

```bash
.
├── set_bor_pk.py        # Script principale
├── password.txt          # File con la password (da creare)
└── SET_BOR.md       # Questo file
```
