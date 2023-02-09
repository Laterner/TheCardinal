from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler

import keyboard

folder_track = 'D:/Home/Downloads'

class Handler(FileSystemEventHandler):
    def __init__(self) -> None:
        self.pictures = ["jpg","png","jpeg","ico","gif","svg"]

        self.pictures_folder_dest = f'D:\Home\Jean\Pictures'
        self.videos_folder_dest = f'D:\Home\Jean\Videos'
        self.torrents_folder_dest = f'D:\Home\Jean\Downloads\Torrents'

    def on_modified(self, event):
        for filename in os.listdir(folder_track):
            extension = filename.split(".")
            if len(extension) > 1 and (extension[len(extension) - 1].lower() in self.pictures):
                file = folder_track + "/" +filename
                new_path = self.pictures_folder_dest + "/" + filename
                os.rename(file, new_path)

            elif len(extension) > 1 and (extension[len(extension) - 1].lower() == "torrent"):
                file = folder_track + "/" +filename
                new_path = self.torrents_folder_dest + "/" + filename
                os.rename(file, new_path)


handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()

def stopWork():
    os.system("taskkill /F /IM TheWatcher.exe")
    

keyboard.add_hotkey("end", lambda: stopWork())

try:
    while(True):
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()