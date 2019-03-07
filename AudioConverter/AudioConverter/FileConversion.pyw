# FileConversion module
import subprocess
import re
import multiprocessing
from Programs.FlacProgram import FlacProgram
from Programs.MetaFlacProgram import MetaFlacProgram
from Programs.LameProgram import LameProgram

def DecodeFlac(file):
    tagDict = RetrieveIdTags(file)
    flacArgs = FlacProgram().SetDefault(file).GetArgList()
    flacProcess = subprocess.Popen(flacArgs, stdout=subprocess.PIPE,)
    decodedData = flacProcess.communicate()[0]   # Returns tuple (stdout, stderr). We only care about the raw data from stdout.
    print("Decoding " + file + " complete.")

    return [ decodedData, tagDict ]

def DecodeMp3(file):
    pass

def ConvertFlac(rawData):
    pass

def ConvertMp3(file, rawData):
    fileData = rawData[0]
    metaData = rawData[1]
    lameArgs = LameProgram().SetDefault(metaData, "-", file[:-5] + ".mp3").GetArgList()
    lameProcess = subprocess.Popen(lameArgs, stdin=subprocess.PIPE, shell=True)
    lameProcess.communicate(input=fileData)
    print("MP3 Conversion for " + file + " complete.")

def ConvertFlacToMp3(file):
    rawData = DecodeFlac(file)
    ConvertMp3(file, rawData)

def RetrieveIdTags(file):
    metaFlacArgs = MetaFlacProgram().SetDefault(file).GetArgList()
    metaFlacProcess = subprocess.Popen(metaFlacArgs, stdout=subprocess.PIPE,)
    tagData = metaFlacProcess.communicate()[0]

    tagDict = {
        'TITLE': '',
        'ARTIST': '',
        'ALBUM': '',
        'YEAR': '',
        'DATE': '',
        'COMMENT': '',
        'TRACKNUMBER': '',
        'TRACKTOTAL': '',
        'GENRE': ''
    }

    pattern = r'\s+comment\[\d+\]:\s+(\w+)=(.*)\r\n'
    for name, value in re.findall(pattern, tagData.decode()):
        tagDict[name.upper()] = value

    print(file + " tags retrieved.")
    return tagDict

