# FileOperations module
import os
import json

def InitVariables():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + '\config.json', 'r') as f:
        config = json.load(f)
    return config

def getAllElementsInFolder(path):
    allFiles = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in [f for f in filenames]:
            allFiles.append(os.path.join(dirpath, filename))
    return allFiles

def getAllFlacsInFolder(path):
    allFiles = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in [f for f in filenames]:
            if filename.endswith(".flac"):
                allFiles.append(os.path.join(dirpath, filename))
    return allFiles
