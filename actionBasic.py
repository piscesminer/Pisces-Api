# coding:utf-8
import os
import json
import RPi.GPIO as GPIO
import time

def shell(action):
    out = os.popen(action)
    info = out.read()
    return info;

def PacketStatus():
    status = shell("sudo bash /home/pi/api/tool/getPacket.sh").split("\n")[0]
    return status

def PacketOn():
    status = PacketStatus();
    if(status):
        return "running:"+status
    else:
        shell("sudo bash /home/pi/api/tool/onPacket.sh")
        return "succes"

def PacketOff():
    status = PacketStatus();
    if(status):
        shell("sudo kill "+status)
        return("stop "+status)
    else:
        return "not running" 

def PacketRestart():
    status = PacketStatus();
    if(status):
        shell("sudo kill "+status)
        time.sleep(0.3);
        PacketRestart();
    else:
        PacketOn();
        return "not running" 

def ApiStatus():
    status = shell("sudo netstat -anp|grep 8001|awk '{printf $7}'|cut -d/ -f1")
    return status

def ApiOff():
    status = apiStatus();
    if(status):
        shell("sudo kill "+status)
        return("stop "+status)
    else:
        return "not running" 
        

def KafkaStatus():
    status = shell("sudo netstat -anp|grep 8002|awk '{printf $7}'|cut -d/ -f1")
    return status

def KafkaOn():
    status = KafkaStatus();
    if(status):
        return "running:"+status
    else:
        shell("sudo node /home/pi/kafka/kafka.js > /home/pi/log/kafka.log &")
        return "succes"
def KafkaOff():
    status = KafkaStatus();
    if(status):
        shell("sudo kill "+status)
        return("stop "+status)
    else:
        return "not running" 

def KafkaRestart():
    status = PacketStatus();
    if(status):
        shell("sudo kill "+status)
        time.sleep(0.3);
        KafkaRestart();
    else:
        KafkaOn();
        return "not running" 

def MinerStatus():
    status = shell("sudo docker inspect --format '{{.Name}} {{.State.Running}}' miner ");
    return status

def MinerOn():
    shell("sudo docker start miner ");
    return true

def MinerOff():
    return shell("sudo docker stop miner");

def MinerRestart():
    return shell("sudo docker restart miner")

def ConfigStatus():
    status = shell("sudo /home/pi/config/_build/prod/rel/gateway_config/bin/gateway_config ping").split("\n")[0]
    if(status == "pong"):
        return "runing"
    else:  
        return status

def ConfigOn():
    status = ConfigStatus();
    if(status=="runing"):
        return "running:"+status
    else:
        shell("sudo /home/pi/config/_build/prod/rel/gateway_config/bin/gateway_config start")
        return "succes"

def ConfigOff():
    status = KafkaStatus();
    if(status=="runing"):
        shell("sudo /home/pi/config/_build/prod/rel/gateway_config/bin/gateway_config stop")
        return("stop "+status)
    else:
        return "not running" 

def ConfigRestart():
    status = ConfigStatus();
    if(status=="runing"):
        ConfigOff()
        time.sleep(0.3);
        ConfigRestart();
    else:
        ConfigOn();
        return "not running" 


def AdvertiseStatus():
    status = shell("sudo /home/pi/config/_build/prod/rel/gateway_config/bin/gateway_config advertise status").split("\n")[0]
    return status

def AdvertiseOn():
    status = AdvertiseStatus();
    if(status=="off"):
        return "running:"+status
    else:
        shell("sudo /home/pi/config/_build/prod/rel/gateway_config/bin/gateway_config advertise on")
        return "succes"

def AdvertiseOff():
    status = AdvertiseStatus();
    if(status=="on"):
        shell("sudo /home/pi/config/_build/prod/rel/gateway_config/bin/gateway_config off")
        return("stop "+status)
    else:
        return "not running" 

def AdvertiseRestart():
    status = AdvertiseStatus();
    if(status=="off"):
        AdvertiseOff()
        time.sleep(0.3);
        AdvertiseRestart();
    else:
        AdvertiseOn();
        return "not running" 



# print(AdvertiseStatus())