from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import time
import importlib

aws = importlib.import_module("aws")

def start_daemon(path):
    # Handler
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True # TODO: This probably breaks some filesystems
    ev_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    ev_handler.on_created = on_created
    ev_handler.on_deleted = on_deleted
    ev_handler.on_modified = on_modified
    ev_handler.on_moved = on_moved


    # Observer
    go_recursively = True
    observer = Observer()
    observer.schedule(ev_handler, path, recursive=go_recursively)

    observer.start()
    try:
        while True:
            time.sleep(5)
    except:
        print("Stopping observer")

def on_created(event):
    print(event)
    aws.sync(event.src_path)
    
def on_deleted(event):
    print(event)

def on_modified(event):
    print(event)

def on_moved(event):
    print(event)
