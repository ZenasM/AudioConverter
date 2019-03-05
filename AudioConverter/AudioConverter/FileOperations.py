import os
# FileOperations module

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
