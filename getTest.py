# coding:utf-8
import os
import router
import json
import api

def shell(action):
    out = os.popen(action)
    info = out.read()
    return info;

def testBle():
    info =shell("hcitool dev")
    raw = info.split("Devices:")
    dev = raw[1].split("\n")
    if(len(dev)>3):
        hci1 = dev[1].split("\t")[2]
        hci0 = dev[2].split("\t")[2]
        return json.dumps({"hci0":hci0,"hci1":hci1})
    else:
        return router.server_error();

def testEcc():
    info =shell("docker exec provision gateway_mfr ecc test")
    raw = info.split("|")
    serial_num = raw[5]
    zone_locked_config = raw[8]
    zone_locked_data = raw[11]
    slot_config =raw[14]
    key_config = raw[17]
    miner_key = raw[20]
    #return serial_num+zone_locked_config+zone_locked_data+slot_config+key_config+miner_key
    ret = {"serial_num":serial_num,"zone_locked_config":zone_locked_config,"zone_locked_data":zone_locked_data,"slot_config":slot_config,"key_config":key_config,"miner_key":miner_key}
    return json.dumps(ret)

def provisionEcc():
    info =shell("docker exec provision gateway_mfr ecc provision")
    raw = info.split("|")
    serial_num = raw[5]
    zone_locked_config = raw[8]
    zone_locked_data = raw[11]
    slot_config =raw[14]
    key_config = raw[17]
    miner_key = raw[20]
    #return serial_num+zone_locked_config+zone_locked_data+slot_config+key_config+miner_key
    return json.dumps({"serial_num":serial_num,"zone_locked_config":zone_locked_config,"zone_locked_data":zone_locked_data,"slot_config":slot_config,"key_config":key_config,"miner_key":miner_key})


def onboardingEcc():
    info =shell("docker exec provision gateway_mfr ecc onboarding")
    if (len(info)<50):
        #ecc sleep
        onboardingEcc()
    else:
        return json.dumps({"onboarding_key":info})

if __name__ == '__main__':
    print(testBle())
