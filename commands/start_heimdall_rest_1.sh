#!/bin/bash
heimdalld rest-server --home ./heimdalld_data --laddr=tcp://0.0.0.0:1317 --node=tcp://localhost:26657 --grpc-addr=localhost:3132
exit 0