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
