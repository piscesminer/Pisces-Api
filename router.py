# coding:utf-8

import os
import sys
import json
import socket
import api
import info
import getIp
import getCpu
import getMiner
import getTest

'''
🍺路由系统，根据路由系统进行跳转
'''
def router(client,method,path,parame):
    if(path == "/"):
        api.responsing(client,index());
    elif(path == "/api"):
        api.responsing(client,index());
        ##🍺设备硬件信息
    elif(path == "/api/hotspot/info"):
        api.responsing(client,hotspot_info());
    elif(path == "/api/hotspot/eth0"):
        api.responsing(client,hotspot_eth0());
    elif(path == "/api/hotspot/wlan0"):
        api.responsing(client,hotspot_wlan0());
    elif(path == "/api/hotspot/cpuinfo"):
        api.responsing(client,hotspot_cpuinfo());
        ##🍺设备Miner信息
    elif(path == "/api/miner/keys"):
        api.responsing(client,miner_keys());
        ##🍺测试相关debug接口
    elif(path == "/api/test/shell"):
        api.responsing(client,getTest.shell(parame[0][1]));
    elif(path == "/api/test/ble"):
        api.responsing(client,getTest.testBle());
    elif(path == "/api/test/ecc"):
        api.responsing(client,getTest.testEcc());
    elif(path == "/api/test/ecc/provision"):
        api.responsing(client,getTest.provisionEcc());
    elif(path == "/api/test/ecc/onboarding"):
        api.responsing(client,getTest.onboardingEcc());
        ##🍺测试接口
    elif(path == "/parame"):
        api.responsing(client,json.dumps(parame));
    else : 
        api.responsing(client,not_found());


'''
🍺路由相关controller接口集
'''
#🔥接口服务器一切正常
def index():
    ret = {'code':200,'data':"Server Alive  :-)"}
    back =json.dumps(ret)
    return back

#🔥404路径
def not_found():
    ret = {'code':404,'data':"Nothing Found Here  :-("}
    back =json.dumps(ret)
    return back

#🔥服务器错误
def server_error():
     return json.dumps({'code':500,'data':"Result Error :-("})

#🔥获取设备信息
def hotspot_info ():
    return info.getInfo();

#🔥获取设备eth0 信息
def hotspot_eth0 ():
    return getIp.networkInfo("eth0");

#🔥获取设备wlan0 信息
def hotspot_wlan0 ():
    return getIp.networkInfo("wlan0");

#🔥获取设备cpuinfo 信息
def hotspot_cpuinfo ():
    return getCpu.getHardware();

#🔥获取Miner onboading 信息
def miner_keys ():
    return getMiner.print_keys();