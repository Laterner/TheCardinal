from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler

folder_track = 'C:/Users/vany0/Downloads'

class Handler(FileSystemEventHandler):
    def __init__(self) -> None:
        self.pictures = ['jpg','png','jpeg','ico','gif','svg']

        self.pictures_folder_dest = 'C:/Users/vany0/Pictures/Donwloaded'
        self.videos_folder_dest = 'C:/Users/vany0/Videos'
        self.torrents_folder_dest = 'C:/Users/vany0/Downloads/Torrents'

    def on_modified(self, event):
        for filename in os.listdir(folder_track):
            extension = filename.split('.')
            if len(extension) > 1 and (extension[len(extension) - 1].lower() in self.pictures):
                file = folder_track + '/' + filename
                new_path = self.pictures_folder_dest + '/' + filename
                os.rename(file, new_path)

            elif len(extension) > 1 and (extension[len(extension) - 1].lower() == 'torrent'):
                file = folder_track + '/' + filename
                new_path = self.torrents_folder_dest + '/' + filename
                os.rename(file, new_path)


handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()

def stopWork():
    os.system('taskkill /F /IM TheWatcher.exe')

try:
    while(True):
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()