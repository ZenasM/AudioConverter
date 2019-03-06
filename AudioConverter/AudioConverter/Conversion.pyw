# Conversion module
import subprocess
import re
from .Programs.FlacProgram import FlacProgram
from .Programs.MetaFlacProgram import MetaFlacProgram
from .Programs.LameProgram import LameProgram


def FlacDecode(file):
    tagDict = GetTags(file)
    flacArgs = FlacProgram().GetDefault(file) #["flac", "--decode", "--stdout", "--silent", file]
    flacProcess = subprocess.Popen(flacArgs, stdout=subprocess.PIPE,)
    decodedData = flacProcess.communicate()[0]   # Returns tuple (stdout, stderr). We only care about the raw data from stdout.
    print("Decoding " + file + " complete.")
    return [ decodedData, tagDict ]

def ConvertMp3(file, rawData):
    fileData = rawData[0]
    tagData = rawData[1]
    lameArgs = LameProgram().GetDefault("-", file[:-5] + ".mp3") #["lame", "--silent", "-V0", "-", file[:-5] + ".mp3"]
    lameProcess = subprocess.Popen(lameArgs, stdin=subprocess.PIPE)
    lameProcess.communicate(input=fileData)
    print("MP3 Conversion for " + file + " complete.")

def ConvertFlacToMp3(file):
    rawData = FlacDecode(file)
    ConvertMp3(file, rawData)

def GetTags(file):
    metaFlacArgs = MetaFlacProgram().GetDefault(file) #["metaflac", "--list", "--block-type=VORBIS_COMMENT", file]
    metaFlacProcess = subprocess.Popen(metaFlacArgs, stdout=subprocess.PIPE,)
    tagData = metaFlacProcess.communicate()[0]

    tagDict = {
        'TITLE': '',
        'ARTIST': '',
        'ALBUM': '',
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

    #def ConverToFlac(inputPath, outputPath):
    #    command = ["flac", ""]
    #    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #    stdout, stderr = process.communicate()

    #def ConverToMp3V0(inputPath, outputPath):
    #    command = ["lame", "-V0", inputPath, outputPath]
    #    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #    stdout, stderr = process.communicate()



