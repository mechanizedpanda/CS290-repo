from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
import shutil

folder_to_track = "C:/Users/wsnid/Downloads"
image_formats = ["jpg", "png", "jpeg", "gif", "webp", "tiff"]
audio_formats = ["mp3", "wav"]
video_formats = ["mp4", "avi", "webm", "mov"]
docs_formats = ["ai", "ait", "rtf", "txt", "doc", "docx", "pdf"]
executables = ["exe"]
zip_folders = ["zip"]

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):

        for filename in os.listdir(folder_to_track):
            extension = (filename.split(".")[-1]).lower()
            src = folder_to_track + '/' + filename

            if extension in image_formats:
                folder_destination = "C:/Users/wsnid/Pictures"
                new_destination = folder_destination + '/' + filename
                shutil.move(src, new_destination)

            elif extension in audio_formats:
                folder_destination = "C:/Users/wsnid/Music"
                new_destination = folder_destination + '/' + filename
                shutil.move(src, new_destination)

            elif extension in video_formats:
                folder_destination = "C:/Users/wsnid/Videos"
                new_destination = folder_destination + '/' + filename
                shutil.move(src, new_destination)

            elif extension in docs_formats:
                folder_destination = "C:/Users/wsnid/Documents"
                new_destination = folder_destination + '/' + filename
                shutil.move(src, new_destination)

            elif extension in zip_folders:
                folder_destination = "C:/Users/wsnid/Zip Folders"
                new_destination = folder_destination + '/' + filename
                shutil.move(src, new_destination)

            elif extension in executables:
                folder_destination = "C:/Users/wsnid/.exe's"
                new_destination = folder_destination + '/' + filename
                shutil.move(src, new_destination)

            else:
                folder_destination = "C:/Users/wsnid/Miscellaneous"
                new_destination = folder_destination + '/' + filename
                shutil.move(src, new_destination)


event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
