#!/bin/bash

./bin/bor server -chain ./erigon_data/genesis.json \
	--datadir ./erigon_data/datadir_1 \
	--bor.heimdall=http://localhost:1317 \
	--mine \
	--miner.etherbase="0x048d975e40d9d9e8931b9ec38f404b8e36be3218" \
  --allow-insecure-unlock \
  --bor.withoutheimdall=false \
  --bor.heimdallgRPC "localhost:3132" \
  --bor.logs true \
  --password ./erigon_data/password.txt \
  --port 30303 \
	--http --http.addr "localhost" --http.port "8545" \
	--http.api "eth,net,web3,txpool,debug,bor" \
	--http.corsdomain "*" --http.vhosts "*"

exit 0
