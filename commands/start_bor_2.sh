#!/bin/bash

docker run -d \
  -v $(pwd)/erigon_data:/data/bor \
  -p 3133:3131 \
  -p 8546:8545 \
  -p 30304:30303 \
  bor-dev-local \
  server -chain /data/bor/genesis.json \
    --datadir /data/bor/datadir_2 \
    --bor.heimdall=http://host.docker.internal:1318 \
    --mine \
    --miner.etherbase="0xf5e55a3e66d028c59c12185e2e51cdafe2c53baf" \
    --allow-insecure-unlock \
    --bor.withoutheimdall=false \
    --bor.heimdallgRPC "host.docker.internal:3134" \
    --bor.logs true \
    --password /data/bor/password.txt \
    --port 30303 \
    --http --http.addr "localhost" --http.port "8546" \
    --http.api "eth,net,web3,txpool,debug,bor" \
    --http.corsdomain "*" --http.vhosts "*" \
    --bootnodes "enode://d25526ab1a2e372fd136cae3fb678deea069639436d34ca0cbb2f80629d43bfd3c2f8fdd5c4940380b18e771199bdf577bfd984e85df816e9c00dbd25e7839ec@host.docker.internal:30303"

exit 0
