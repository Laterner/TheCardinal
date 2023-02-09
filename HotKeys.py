import os, rotatescreen, keyboard

def test(_TheWatcher):
    _TheWatcher.kill()
    print("close")
    
def rotate_screen_left():
    pass

def console():
    os.system("start wt")
    # os.startfile("cmd.exe")
    # subprocess.run(['cmd', '/k cd C:/Home'], shell=True, check=True)

def closeExp():
    os.system("taskkill -f -im explorer.exe")

def startExp():
    os.system("start explorer.exe")

def ToggleIcon():
    os.system("start explorer.exe")

def Screen_rotation(temp):
    screen = rotatescreen.get_primary_display()
    if temp == "up":
        screen.set_landscape()
    elif temp == "right":
        screen.set_portrait_flipped()
    elif temp == "down":
        screen.set_landscape_flipped()
    elif temp == "left":
        screen.set_portrait()


def reg_hotkeys():
    keyboard.add_hotkey("ctrl+alt+t", lambda: console())
    # keyboard.add_hotkey("win+a", lambda: HotKeys.ToggleIcon())
    keyboard.add_hotkey('ctrl+alt+up', lambda: Screen_rotation("up"))
    keyboard.add_hotkey('ctrl+alt+down', lambda: Screen_rotation("down"))
    keyboard.add_hotkey('ctrl+alt+left', lambda: Screen_rotation("left"))
    keyboard.add_hotkey('ctrl+alt+right', lambda: Screen_rotation("right"))
    keyboard.add_abbreviation("@emy", "ivantrofimov2001@yandex.ru")