import HotKeys
import subprocess

from TheCardinalsUI import *


if __name__ == "__main__":
    import sys
    # TheWatcher = subprocess.Popen("py ./TheWatcher.exe")

    HotKeys.reg_hotkeys()
    
    app = QApplication(sys.argv)
    # if app.exec:
    #     subprocess.Popen("notepad.exe")
    window = TheCardinalMainWindow()
    # window.show()
    sys.exit(app.exec())