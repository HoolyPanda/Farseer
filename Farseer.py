import os
import knocker
import time

class Farseer:
    def __init__(self):
        while True:
            pids = open("./farseerConfig", 'r').readlines()
            for rPid in pids:
                rPid = rPid.replace('\n', '')
                pid = ''
                for char in rPid:
                    if char != ' ':
                        pid += char
                    else:
                        break
                pid = pid.replace('\n', '')
                path = '/proc/' + pid
                if os.path.exists(path):
                    print("")
                else:
                    buddy = knocker.Knocker()
                    buddy.SendMsg("PID: " + rPid + " is not OK", peerId = 0)
            time.sleep(3600)

        # print(a)

f = Farseer()