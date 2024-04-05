from ctypes import *


DLL = "./IconSwitch.dll"
lib = CDLL(DLL)
print(lib.IconSwitch())
