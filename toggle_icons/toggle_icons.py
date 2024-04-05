from ctypes import *

def toggle():
    DLL = "./IconSwitch.dll"
    lib = CDLL(DLL)
    print(lib.IconSwitch())
