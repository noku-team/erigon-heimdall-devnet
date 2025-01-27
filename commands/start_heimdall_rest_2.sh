#!/bin/bash
heimdalld rest-server --home ./heimdalld_data2 --laddr=tcp://0.0.0.0:1318 --node=tcp://localhost:26659 --grpc-addr=localhost:3134
exit 0