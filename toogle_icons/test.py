from ctypes import *
DLL = "C:/Users/vany0/source/repos/toggle_icons_dll/Debug/DLLTest.dll"
lib = CDLL(DLL)

exit()
# lib = cdll.LoadLibrary(f"C:\Windows\System32\msvcrt.dll")   
# lib.printf(b"From dll with love!\n")    # вывод строки через стандартную printf

# lib_2 = CDLL(f"C:\Windows\System32\msvcrt.dll") # подключаем библиотеку msvcrt.dll

# var_a = 31
# lib_2.printf(b"Print int_a = %d\n", var_a)  # вывод переменной int