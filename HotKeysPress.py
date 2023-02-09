import keyboard
import HotKeys
import time
import os
from datetime import datetime

isStarted = True
def close():
    print("closing...")
    #raise SystemExit
    os.kill(os.getpid(), -1)

def writeToFile():
    DIR = "C:/logs/log.txt"
    
    with open(DIR, 'a+') as file:
        file.write(str(datetime.now()) + " | " + "EROR" +'\n')

def listener():
    try:
        while isStarted:
            time.sleep(1)
        return 0

    except:
        print("except")
        writeToFile()
        return -1

    finally:
        print("finally")
        listener()



keyboard.add_hotkey("ctrl+alt+t", lambda: HotKeys.console())
keyboard.add_hotkey("end", lambda: close())
listener()

