#! /bin/bash

cd /home/pi/config/_build/prod/rel/gateway_config/
./bin/gateway_config start 
sleep 3
./bin/gateway_config advertise on
