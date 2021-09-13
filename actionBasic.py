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
    data = shell("bash /home/pi/api/tool/getPacket.sh")
    print(data)

PacketStatus()