# FileOperations module
import os
import json
import re
import subprocess
import ID3Tag
from fuzzywuzzy import process, fuzz
from Programs.MetaFlacProgram import MetaFlacProgram

def InitVariables():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + '\config.json', 'r') as f:
        config = json.load(f)
    return config

def GetAllElementsInFolder(path):
    allFiles = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in [f for f in filenames]:
            allFiles.append(os.path.join(dirpath, filename))
    return allFiles

def GetAllFlacsInFolder(path):
    allFiles = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in [f for f in filenames]:
            if filename.endswith(".flac"):
                allFiles.append(os.path.join(dirpath, filename))
    return allFiles

def EnsurePath(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

def RetrieveIdTags(file):
    metaFlacArgs = MetaFlacProgram().SetDefault(file).GetArgList()
    metaFlacProcess = subprocess.Popen(metaFlacArgs, stdout=subprocess.PIPE,)
    tagData = metaFlacProcess.communicate()[0]

    tagDict = { "TXXX": [] }
    pattern = r'\s+comment\[\d+\]:\s+(\w+)=(.*)\r\n'
    for name, value in re.findall(pattern, tagData.decode()):
        key = process.extractOne(name, ID3Tag.matchingStrings, scorer=fuzz.ratio) # Tuple of (key, ratio)
        if key[1] > 80:
            tagDict[ID3Tag.matchingDict[key[0]]] = value
        else:
            tagDict["TXXX"].append(name + "=" + value)

    print(file + " tags retrieved.")
    return tagDict
