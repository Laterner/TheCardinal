import HotKeys
import subprocess

from TheCardinalsUI import *


if __name__ == "__main__":
    import sys
    TheWatcher = None #subprocess.Popen("TheWatcher.exe")

    HotKeys.reg_hotkeys()
    
    app = QApplication(sys.argv)
    # if app.exit:
    #     subprocess.Popen("notepad.exe")
    window = TheCardinalMainWindow()
    # window.show()
    sys.exit(app.exec())