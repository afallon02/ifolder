from sys import platform
import importlib
from pathlib import Path
import os
import subprocess
import logging

home = str(Path.home())
ifolder = "ifolder"

def create_folder(foldername=ifolder):
    if os.path.isdir(f"{home}/{foldername}"):
        return True
    else:
        try:
            logging.info("Folder not present, creating now")
            os.mkdir(f"{home}/{foldername}")
            return True
        except OSError:
            logging.info("FATAL ERROR: Failed to create ifolder")
            return False
        else:
            logging.info("FATAL ERROR: Failed to create ifolder")
            return False

def first_time_setup():
    logging.info("Checking for AWS Credential")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Configuring...")

    logging.info("Starting file sync")
    if create_folder():
        logging.info("Folder exists")
        sync = importlib.import_module("sync")
        sync.start_daemon(f"{home}/{ifolder}")
    else:
        logging.info("Something went wrong! UwU!")

