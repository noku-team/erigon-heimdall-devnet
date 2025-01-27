# Configurazione di una chain locale Polygon

## Configurazione Heimdall validator node

### Installazione

Clonare la release più recente da [Github](https://github.com/maticnetwork/heimdall/releases), e installare heimdall seguendone il README.

### Configurazione first node

Inizializzare il primo nodo nella directory dei dati con il seguente comando:

```bash
./bin/heimdalld init --chain-id=heimdall-erigon-<chainid> --chain=local --home=./heimdalld_data
```

Verrà dunque creato un file [genesis.json](./heimdall_data/config/genesis.json) con le configurazioni di default per heimdall, modifichiamone i valori dei validatori e dei proposer con i valori generati dal secondo nodo heimdall (se vogliamo due validatori); per generare i dati da inserire utilizzare gli [scripts](./scripts/README.md) forniti.

Esempio di genesis heimdall con due validatori:

```json
{
  "genesis_time": "2025-01-22T11:12:59.787707Z",
  "chain_id": "erigon-test-2999",
  "consensus_params": {
    "block": {
      "max_bytes": "22020096",
      "max_gas": "-1",
      "time_iota_ms": "1000"
    },
    "evidence": {
      "max_age": "100000"
    },
    "validator": {
      "pub_key_types": [
        "secp256k1"
      ]
    }
  },
  "app_hash": "",
  "app_state": {
    "auth": {
      "params": {
        "max_memo_characters": "256",
        "tx_sig_limit": "7",
        "tx_size_cost_per_byte": "10",
        "sig_verify_cost_ed25519": "590",
        "sig_verify_cost_secp256k1": "1000",
        "max_tx_gas": "1000000",
        "tx_fees": "1000000000000000"
      },
      "accounts": [
        // validatore 1 heimdall
        {
          "address": "0x048d975e40d9d9e8931b9ec38f404b8e36be3218",
          "coins": [
            {
              "denom": "matic",
              "amount": "1000000000000000000000"
            }
          ],
          "sequence_number": "0",
          "account_number": "0",
          "module_name": "",
          "module_permissions": null
        },
        // validatore 2 heimdall
        {
          "address": "0xf5e55a3e66d028c59c12185e2e51cdafe2c53baf",
          "coins": [
            {
              "denom": "matic",
              "amount": "1000000000000000000000"
            }
          ],
          "sequence_number": "0",
          "account_number": "1",
          "module_name": "",
          "module_permissions": null
        }
      ]
    },
    "bank": {
      "send_enabled": true
    },
    "bor": {
      "params": {
        "sprint_duration": "20",
        "span_duration": "2000",
        "producer_count": "4"
      },
      "spans": [
        {
          "span_id": "0",
          "start_block": "0",
          "end_block": "255",
          "validator_set": {
            "validators": [
              // validatore 1 heimdall
              {
                "ID": "1",
                "startEpoch": "0",
                "endEpoch": "0",
                "nonce": "1",
                "power": "1",
                "pubKey": "0x043245d66efca79886088e3e454a6b12a7808a9441566a24a49db062847d8a975734ef6c81d9fd14b53f4cf4499fad5111c86c9913725e7b939977875fdd6c712c",
                "signer": "0x048d975e40d9d9e8931b9ec38f404b8e36be3218",
                "last_updated": "",
                "jailed": false,
                "accum": "0"
              },
              // validatore 2 heimdall
              {
                "ID": "2",
                "startEpoch": "0",
                "endEpoch": "0",
                "nonce": "1",
                "power": "1",
                "pubKey": "0x0432541a747bd596a7b4ee70981b086485cffb9ef25c5d94c716cdecebddbf2768709b069b95ee9dba5d8306bb7253c10020765a8f4dbc418a95f70c0f2709947d",
                "signer": "0xf5e55a3e66d028c59c12185e2e51cdafe2c53baf",
                "last_updated": "",
                "jailed": false,
                "accum": "0"
              }
            ],
            "proposer": {
              "ID": "1",
              "startEpoch": "0",
              "endEpoch": "0",
              "nonce": "1",
              "power": "1",
              "pubKey": "0x043245d66efca79886088e3e454a6b12a7808a9441566a24a49db062847d8a975734ef6c81d9fd14b53f4cf4499fad5111c86c9913725e7b939977875fdd6c712c",
              "signer": "0x048d975e40d9d9e8931b9ec38f404b8e36be3218",
              "last_updated": "",
              "jailed": false,
              "accum": "0"
            }
          },
          "selected_producers": [
            // validatore 1 heimdall
            {
              "ID": "1",
              "startEpoch": "0",
              "endEpoch": "0",
              "nonce": "1",
              "power": "1",
              "pubKey": "0x043245d66efca79886088e3e454a6b12a7808a9441566a24a49db062847d8a975734ef6c81d9fd14b53f4cf4499fad5111c86c9913725e7b939977875fdd6c712c",
              "signer": "0x048d975e40d9d9e8931b9ec38f404b8e36be3218",
              "last_updated": "",
              "jailed": false,
              "accum": "0"
            },
            // validatore 2 heimdall
            {
              "ID": "2",
              "startEpoch": "0",
              "endEpoch": "0",
              "nonce": "1",
              "power": "1",
              "pubKey": "0x0432541a747bd596a7b4ee70981b086485cffb9ef25c5d94c716cdecebddbf2768709b069b95ee9dba5d8306bb7253c10020765a8f4dbc418a95f70c0f2709947d",
              "signer": "0xf5e55a3e66d028c59c12185e2e51cdafe2c53baf",
              "last_updated": "",
              "jailed": false,
              "accum": "0"
            }
          ],
          "bor_chain_id": "2999"
        }
      ]
    },
    "chainmanager": {
      "params": {
        "mainchain_tx_confirmations": "6",
        "maticchain_tx_confirmations": "10",
        "chain_params": {
          "bor_chain_id": "2999",
          "matic_token_address": "0x0000000000000000000000000000000000000000",
          "staking_manager_address": "0x0000000000000000000000000000000000000000",
          "slash_manager_address": "0x0000000000000000000000000000000000000000",
          "root_chain_address": "0x0000000000000000000000000000000000000000",
          "staking_info_address": "0x0000000000000000000000000000000000000000",
          "state_sender_address": "0x0000000000000000000000000000000000000000",
          "state_receiver_address": "0x0000000000000000000000000000000000001001",
          "validator_set_address": "0x0000000000000000000000000000000000001000"
        }
      }
    },
    "checkpoint": {
      "params": {
        "checkpoint_buffer_time": "1000000000000",
        "avg_checkpoint_length": "256",
        "max_checkpoint_length": "1024",
        "child_chain_block_interval": "10000"
      },
      "buffered_checkpoint": null,
      "last_no_ack": "0",
      "ack_count": "0",
      "checkpoints": null
    },
    "clerk": {
      "event_records": [],
      "record_sequences": null
    },
    "gov": {
      "starting_proposal_id": "1",
      "deposits": null,
      "votes": null,
      "proposals": null,
      "deposit_params": {
        "min_deposit": [
          {
            "denom": "matic",
            "amount": "10000000000000000000"
          }
        ],
        "max_deposit_period": "172800000000000"
      },
      "voting_params": {
        "voting_period": "172800000000000"
      },
      "tally_params": {
        "quorum": "0.334000000000000000",
        "threshold": "0.500000000000000000",
        "veto": "0.334000000000000000"
      }
    },
    "params": null,
    "sidechannel": {
      "past_commits": []
    },
    "slashing": {
      "params": {
        "signed_blocks_window": "100",
        "min_signed_per_window": "0.500000000000000000",
        "downtime_jail_duration": "600000000000",
        "slash_fraction_double_sign": "0.050000000000000000",
        "slash_fraction_downtime": "0.010000000000000000",
        "slash_fraction_limit": "0.333333333333333333",
        "jail_fraction_limit": "0.333333333333333333",
        "max_evidence_age": "120000000000",
        "enable_slashing": false
      },
      "signing_infos": {
        "1": {
          "valID": "1",
          "startHeight": "0",
          "indexOffset": "0"
        }
      },
      "missed_blocks": {},
      "buffer_val_slash_info": null,
      "tick_val_slash_info": null,
      "tick_count": "0"
    },
    "staking": {
      "validators": [
        // validatore 1 heimdall
        {
          "ID": "1",
          "startEpoch": "0",
          "endEpoch": "0",
          "nonce": "1",
          "power": "1",
          "pubKey": "0x043245d66efca79886088e3e454a6b12a7808a9441566a24a49db062847d8a975734ef6c81d9fd14b53f4cf4499fad5111c86c9913725e7b939977875fdd6c712c",
          "signer": "0x048d975e40d9d9e8931b9ec38f404b8e36be3218",
          "last_updated": "",
          "jailed": false,
          "accum": "0"
        },
        // validatore 2 heimdall
        {
          "ID": "2",
          "startEpoch": "0",
          "endEpoch": "0",
          "nonce": "1",
          "power": "1",
          "pubKey": "0x0432541a747bd596a7b4ee70981b086485cffb9ef25c5d94c716cdecebddbf2768709b069b95ee9dba5d8306bb7253c10020765a8f4dbc418a95f70c0f2709947d",
          "signer": "0xf5e55a3e66d028c59c12185e2e51cdafe2c53baf",
          "last_updated": "",
          "jailed": false,
          "accum": "0"
        }
      ],
      "current_val_set": {
        "validators": [
          // validatore 1 heimdall
          {
            "ID": "1",
            "startEpoch": "0",
            "endEpoch": "0",
            "nonce": "1",
            "power": "1",
            "pubKey": "0x043245d66efca79886088e3e454a6b12a7808a9441566a24a49db062847d8a975734ef6c81d9fd14b53f4cf4499fad5111c86c9913725e7b939977875fdd6c712c",
            "signer": "0x048d975e40d9d9e8931b9ec38f404b8e36be3218",
            "last_updated": "",
            "jailed": false,
            "accum": "0"
          },
          // validatore 2 heimdall
          {
            "ID": "2",
            "startEpoch": "0",
            "endEpoch": "0",
            "nonce": "1",
            "power": "1",
            "pubKey": "0x0432541a747bd596a7b4ee70981b086485cffb9ef25c5d94c716cdecebddbf2768709b069b95ee9dba5d8306bb7253c10020765a8f4dbc418a95f70c0f2709947d",
            "signer": "0xf5e55a3e66d028c59c12185e2e51cdafe2c53baf",
            "last_updated": "",
            "jailed": false,
            "accum": "0"
          }
        ],
        "proposer": {
          "ID": "1",
          "startEpoch": "0",
          "endEpoch": "0",
          "nonce": "1",
          "power": "1",
          "pubKey": "0x043245d66efca79886088e3e454a6b12a7808a9441566a24a49db062847d8a975734ef6c81d9fd14b53f4cf4499fad5111c86c9913725e7b939977875fdd6c712c",
          "signer": "0x048d975e40d9d9e8931b9ec38f404b8e36be3218",
          "last_updated": "",
          "jailed": false,
          "accum": "0"
        }
      },
      "staking_sequences": null
    },
    "supply": {
      "supply": {
        "total": []
      }
    },
    "topup": {
      "tx_sequences": null,
      "dividend_accounts": [
        // validatore 1 heimdall
        {
          "user": "0x048d975e40d9d9e8931b9ec38f404b8e36be3218",
          "feeAmount": "0"
        },
        // validatore 2 heimdall
        {
          "user": "0xf5e55a3e66d028c59c12185e2e51cdafe2c53baf",
          "feeAmount": "0"
        }
      ]
    }
  }
}

```

--------------------------------------------

Cambiamo inoltre tutti i valori di `bor_chain_id` con il `chain_id` che sceglieremo su Erigon/Bor.

--------------------------------------------

Il nodo eseguira di default il suo servizio p2p sulla porta 26656, e il servizio rpc sulla porta 26657, per cambiarne le configurazioni modificare il file [config.toml](./heimdalld_data/config/config.toml) nella directory `heimdalld_data/config/`.

Eseguiamo dunque il primo nodo con il seguente comando:

```bash
./bin/heimdalld start --home=./heimdalld_data
```

E lanciamo il rest-server con il seguente comando:

```bash
./bin/heimdalld rest-server --home=./heimdalld_data --laddr=tcp://0.0.0.0:1317 --node=tcp://localhost:26657
```

### Configurazione nodes aggiuntivi

Per inizializzare un nodo aggiuntivo dobbiamo copiare le configurazioni del primo nodo, e modificarle per far si che il nodo si connetta al nodo principale. L'esempio sottostante viene fatto sul secondo nodo creato, innanzitutto inizializziamo il nodo con il seguente comando:

```bash
./bin/heimdalld init --chain-id=heimdall-erigon-<chainid> --chain=local --home=./heimdalld_data2
```

Configuriamo il file [genesis.json](./heimdalld_data/config/genesis.json) principale con i dati di questo validatore, se vogliamo più validatori.
Copiare quindi il file [genesis.json](./heimdalld_data/config/genesis.json) dalla directory `heimdalld_data/config/` alla directory `heimdalld_data2/config/`.
Modificare il file [config.toml](./heimdalld_data2/config/config.toml) nella directory `heimdalld_data2/config/` cambiando il valore della chiave `seeds` con l'id (che troviamo a [questo](http://localhost:26657/status?) endpoint) e l'indirizzo ip del nodo principale, es:

```toml
seeds = "f1b1c1b1d1b1e1b1f1b1g1b1@127.0.0.1:26656"
```

Modifichiamo inoltre le porte di servizio (p2p, RPC e gRPC), es:

```toml
prof_laddr = "localhost:6061"

[p2p]
laddr = "tcp://0.0.0.0:26658"

[rpc]
laddr = "tcp://127.0.0.1:26659"
```

Eseguiamo dunque il secondo nodo con il seguente comando:

```bash
./bin/heimdalld start --home=./heimdalld_data2
```

E lanciamo il rest-server con il seguente comando:

```bash
./bin/heimdalld rest-server --home=./heimdalld_data2 --laddr=tcp://0.0.0.0:1318 --node=tcp://localhost:26659 --grpc-addr 0.0.0.0:3133
```

A questo punto il secondo nodo si connetterà al primo nodo, e sarà possibile vedere i blocchi prodotti dal secondo nodo nel primo nodo, per verificarne la giusta connessione è possibile controllare il log del nodo principale e lo stato della net al seguente endpoint: [http://localhost:26657/net_info](http://localhost:26657/net_info).

## Configurazione erigon

```bash
./bin/erigon --datadir=./erigon_data/data/erigon --chain=bor-devnet --private.api.addr=localhost:9090 --http.api=eth,erigon,web3,net,debug,trace,txpool,parity,admin --http.corsdomain="*" --bor.heimdall=http://localhost:1317
```

## Configurazione bor

Configuriamo il file [genesis.json](./erigon_data/genesis.json) con i dati dei/del validatori/e heimdall e con i chain_id scelti. Ecco qui un esempio:

```json
{
 "config": {
  "chainId": 2999, // chain_id scelto
  "homesteadBlock": 0,
  "eip150Block": 0,
  "eip150Hash": "0x0000000000000000000000000000000000000000000000000000000000000000",
  "eip155Block": 0,
  "eip158Block": 0,
  "byzantiumBlock": 0,
  "constantinopleBlock": 0,
  "petersburgBlock": 0,
  "istanbulBlock": 0,
  "muirGlacierBlock": 0,
  "berlinBlock": 0,
  "londonBlock": 0,
  "shanghaiBlock": 0,
  "cancunBlock": 0,
  "bor": {
   "jaipurBlock": 0,
   "delhiBlock": 0,
   "indoreBlock": 0,
   "period": {
    "0": 2
   },
   "producerDelay": {
    "0": 4
   },
   "sprint": {
    "0": 16
   },
   "backupMultiplier": {
    "0": 2
   },
   "validatorContract": "0x0000000000000000000000000000000000001000",
   "stateReceiverContract": "0x0000000000000000000000000000000000001001"
  }
 },
 "nonce": "0x0",
 "timestamp": "0x5ce28211",
 "extraData": "",
 "gasLimit": "0x989680",
 "difficulty": "0x1",
 "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
 "coinbase": "0x0000000000000000000000000000000000000000",
 "alloc": {
  "0000000000000000000000000000000000001000": {
   "balance": "0x0",
   "code": "0x<data>" // copiare da amoy
  },
  "0000000000000000000000000000000000001001": {
   "balance": "0x0",
   "code": "0x<data>" // copiare da amoy
  },
  "0000000000000000000000000000000000001010": {
   "balance": "0x204fcd4f31349d83b6e00000",
   "code": "0x<data>" // copiare da amoy
  },
  // validatore 1 heimdall
  "048d975e40d9d9e8931b9ec38f404b8e36be3218": {
   "balance": "0x3635c9adc5dea00000" // 1000 ether
  },
  // validatore 1 heimdall
  "f5e55a3e66d028c59c12185e2e51cdafe2c53baf": {
   "balance": "0x3635c9adc5dea00000" // 1000 ether
  }
 },
 "number": "0x0",
 "gasUsed": "0x0",
 "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000"
}
```

A questo punto importiamo le chiavi private dei validatori heimdall in bor, per farlo eseguiamo il seguente comando:

```bash
./bin/bor account import -datadir ./erigon_data/datadir_1 scripts/out/privatekey.txt
```

Creiamo il file con la password della chiave utilizzata e salviamolo in `erigon_data/password.txt`.

Esecuzione di bor sul primo heimdall con il comando:

```bash
./bin/bor server -chain ./erigon_data/genesis.json --mine \
  --datadir ./erigon_data/datadir_1 \
  --miner.gaslimit "30000000" \
  --miner.etherbase="0x048d975e40d9d9e8931b9ec38f404b8e36be3218" \
  --unlock "0x048d975e40d9d9e8931b9ec38f404b8e36be3218" \
  --allow-insecure-unlock \
  --bor.withoutheimdall=false \
  --bor.heimdall "http://localhost:1317" \
  --bor.heimdallgRPC "tcp://localhost:6060" \
  --password ./erigon_data/password.txt
```
