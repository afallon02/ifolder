from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import time
import importlib
import logging

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
        download()
        while True:
            time.sleep(5)
    except:
        logging.info("Stopping observer")

def download():
    aws.download()
        
def on_created(event):
    logging.info(event)
    aws.upload(event.src_path)
    
def on_deleted(event):
    logging.info(event)

def on_modified(event):
    logging.info(event)

def on_moved(event):
    logging.info(event)
