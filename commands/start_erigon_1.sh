#!/bin/bash
./bin/erigon --datadir ./erigon_data/datadir_1 \
	--chain=bor-devnet --networkid=2999 \
	--http --private.api.addr=localhost:9090 \
	--http.api=eth,erigon,web3,net,debug,trace,txpool,parity,admin \
	--http.corsdomain="*" --bor.heimdall=http://localhost:1317 \
	--mine --miner.etherbase=0x048d975e40d9d9e8931b9ec38f404b8e36be3218 \
	--torrent.port 42069
