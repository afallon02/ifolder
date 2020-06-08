from sys import platform
import importlib
from pathlib import Path
import os
import subprocess

home = str(Path.home())
ifolder = "ifolder"

def create_folder(foldername=ifolder):
    if os.path.isdir(f"{home}/{foldername}"):
        return True
    else:
        try:
            print("Folder not present, creating now")
            os.mkdir(f"{home}/{foldername}")
            return True
        except OSError:
            print("FATAL ERROR: Failed to create ifolder")
            return False
        else:
            print("FATAL ERROR: Failed to create ifolder")
            return False

def first_time_setup():
    print("Checking for AWS Credential")

if __name__ == "__main__":
    print("Configuring...")

    print("Starting file sync")
    if create_folder():
        print("Folder exists")
        sync = importlib.import_module("sync")
        sync.start_daemon(f"{home}/{ifolder}")
    else:
        print("Something went wrong! UwU!")

