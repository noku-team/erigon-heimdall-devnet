# Configurazione di una chain locale Polygon

## Configurazione Heimdall validator node

### Installazione

Clonare la release più recente da [Github](https://github.com/maticnetwork/heimdall/releases), e installare heimdall seguendone il README.

### Configurazione first node

Inizializzare il primo nodo nella directory dei dati con il seguente comando:

```bash
./bin/heimdalld init --chain-id=heimdall-erigon-assertoor --chain=local --home=./heimdalld_data
```

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
./bin/heimdalld init --chain-id=heimdall-erigon-assertoor --chain=local --home=./heimdalld_data2
```

Copiare il file [genesis.json](./heimdalld_data/config/genesis.json) dalla directory `heimdalld_data/config/` alla directory `heimdalld_data2/config/`.
Modificare il file [config.toml](./heimdalld_data2/config/config.toml) nella directory `heimdalld_data2/config/` cambiando il valore della chiave `seeds` con l'id (che troviamo a [questo](http://localhost:26657/status?) endpoint) e l'indirizzo ip del nodo principale, es:

```toml
seeds = "f1b1c1b1d1b1e1b1f1b1g1b1@127.0.0.1:26656"
```

Modifichiamo inoltre le porte di servizio (p2p e rpc), es:

```toml
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
