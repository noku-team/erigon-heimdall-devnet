#!/bin/bash

./bin/bor server -chain ./erigon_data/genesis.json \
	--datadir ./erigon_data/datadir_2 \
	--bor.heimdall=http://localhost:1318 \
	--mine \
  --miner.gaslimit "30000000" \
	--miner.etherbase="0xf5e55a3e66d028c59c12185e2e51cdafe2c53baf" \
  --allow-insecure-unlock \
  --bor.withoutheimdall=false \
  --bor.heimdallgRPC "localhost:3134" \
  --password ./erigon_data/password.txt \
  --port 30304 \
  --grpc.addr :3133 \
	--http --http.addr "localhost" --http.port "8546" \
	--http.api "eth,net,web3,txpool,debug,bor" \
	--http.corsdomain "*" --http.vhosts "*" \
  --bootnodes "enode://d25526ab1a2e372fd136cae3fb678deea069639436d34ca0cbb2f80629d43bfd3c2f8fdd5c4940380b18e771199bdf577bfd984e85df816e9c00dbd25e7839ec@127.0.0.1:30303"

exit 0
