# coding:utf-8
import os
import router
import json
import api
import RPi.GPIO as GPIO

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

##E2相关接口
def e2init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27,GPIO.OUT)
    return GPIO.output(27,GPIO.LOW)

def e2write(data):

    basecmd = "i2cset -f -y 1 0x50 "

def e2read():
    basecmd = "i2cget -f -y 1 0x50 "
    length = 14;
    data = [];
    for i in range(length):
        address = e2decode(i);
        cmd = shell(basecmd+address);
        ret = cmd.split("\n")[0]
        data.append(ret);
    ret = ""
    for result in data:
        ret = ret+bytes(int(result,16))
    ret = json.dumps({'minerSn':ret,'raw':data})
    return ret

def e2decode(data):
    add = 2-len(bytes(data));
    for i in range(add):
        data = "0"+bytes(data);
    return "0x"+bytes(data);

if __name__ == '__main__':
    print(e2read())
