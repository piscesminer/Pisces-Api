import threading
from threading import Lock,Thread
import serial
from time import ctime,sleep
import json
import api
import router
time = 0; 


def reader():
    ret = [];
    ser = serial.Serial("/dev/serial0",9600)
    i=10
    while i>0:
        i=i-1;
        line = str(str(ser.readline())[2:])
        ret.append(line)
    if(len(ret)>5):
        return json.dumps(ret);
    else:
        return router.server_error();
    


if __name__ == '__main__':
    print(reader())
