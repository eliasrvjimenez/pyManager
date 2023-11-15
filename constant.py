import time
import datetime
import logging
import watchdog
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
import json
import FileOrganizer as organize
import DirectoryCheck as check

class Watcher(FileSystemEventHandler):
    
    files_moved = 0 
    
    def on_created(self, event):
        self.files_moved = self.files_moved + organize.run_sort()
        return self.files_moved
    
    def on_any_event(self, event):
        return LoggingEventHandler().on_any_event(event)

if __name__ == "__main__":
    f = open(check.get_settings(), 'r')
    settings = json.load(f)
    f.close()
    

    watcher = watchdog.events.FileSystemEventHandler.on_created
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    path = settings["fileOrganizer"]["Downloads"]
    event_handler = Watcher()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    start_time = datetime.datetime.now()
    timer_start_time = time.time()
    print("pyManager Started at: %s " % start_time )
    organize.run_sort()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
            observer.stop()
            timer_end_time = round((time.time() - timer_start_time))
            print("\nRan for %s seconds" % timer_end_time)
            print("Files Moved: %s" % Watcher.files_moved)
    observer.join()
    