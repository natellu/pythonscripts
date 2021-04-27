import sys
import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
from ffmpy import FFmpeg

WatchingExtensionsList = [".flac"]
watchingfolder = "C:\\Users\\natellu\\Documents\\programmierung\\pythonscripts\\flacs\\"
outputfolder = "C:\\Users\\natellu\\Documents\\programmierung\\pythonscripts\\mp3\\"

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        print(f'event: {event}')
       
        if event.is_directory:
            print("is directory")
            return

        filename, file_extension = os.path.splitext(event.src_path)
        if file_extension not in WatchingExtensionsList:
            print("not in extention list")
            return

        file_size = -1
        while file_size != os.path.getsize(event.src_path):
            file_size = os.path.getsize(event.src_path)
            time.sleep(1)

        print("done copying")

        ff = FFmpeg(
            inputs={event.src_path: None},
            outputs={'folder\\output.mp3': "-c:a libmp3lame -b:a 320k"}
        )
       
        ff.run()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = watchingfolder
    """ event_handler = LoggingEventHandler() """
    event_handler = Handler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    print("Watching " + path)

    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
