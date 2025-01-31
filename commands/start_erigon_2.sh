#!/bin/bash
./bin/erigon --datadir ./erigon_data/datadir_2 \
	--chain=bor-devnet --networkid=2999 \
	--http --private.api.addr=localhost:9091 \
	--http.api=eth,erigon,web3,net,debug,trace,txpool,parity,admin \
	--http.corsdomain="*" --bor.heimdall=http://localhost:1318 \
	--mine --miner.etherbase=0xf5e55a3e66d028c59c12185e2e51cdafe2c53baf \
	--bootnodes "enode://80178fe2b2b990cb780489ef0a4535a740348f180112a7ae83af5493fd5ccb2b546924490dd4368f3b53c8d3b128c54f38e00645af1e7d220d637da2929ad908@127.0.0.1:30306" \
	--torrent.port 42070
