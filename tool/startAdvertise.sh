#! /bin/bash
/home/pi/config/_build/prod/rel/gateway_config/bin/gateway_config start 
sleep 1
/home/pi/config/_build/prod/rel/gateway_config/bin/gateway_config ping
sleep 1
/home/pi/config/_build/prod/rel/gateway_config/bin/gateway_config advertise on
