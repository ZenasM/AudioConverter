# FileConversion module
import os
import subprocess
import concurrent.futures
import FileOperations
from Programs.FlacProgram import FlacProgram
from Programs.LameProgram import LameProgram

def TranscodeFlacToMp3(file, **keyword_parameters):
    outputFile = file[:-5] + ".mp3"
    if "output" in keyword_parameters:
        outputFile = keyword_parameters["output"]
    FileOperations.EnsurePath(os.path.dirname(outputFile))
    # Need confirmation from user.

    rawData = DecodeFlacFile(file)
    EncodeMp3(file, rawData, output=outputFile)

def DecodeFlacFile(file):
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    tagsResult = executor.submit(FileOperations.RetrieveIdTags, file)
    dataResult = executor.submit(DecodeFlacData, file)
    tags = tagsResult.result()
    data = dataResult.result()
    return [ data, tags ]

def DecodeFlacData(file):
    flacArgs = FlacProgram().SetDefault(file).GetArgList()
    flacProcess = subprocess.Popen(flacArgs, stdout=subprocess.PIPE,)
    decodedData = flacProcess.communicate()[0]   # Returns tuple (stdout, stderr). We only care about the raw data from stdout.
    print("Decoding " + file + " complete.")
    return decodedData

def DecodeMpeg(file):
    pass

def EncodeFlac(rawData):
    pass

def EncodeMp3(file, rawData, **keyword_parameters):
    outputFile = file[:-5] + ".mp3"
    if "output" in keyword_parameters:
        outputFile = keyword_parameters["output"]

    fileData = rawData[0]
    metaData = rawData[1]
    lameArgs = LameProgram().SetDefault(metaData, "-", outputFile).GetArgList()
    lameProcess = subprocess.Popen(lameArgs, stdin=subprocess.PIPE)
    lameProcess.communicate(input=fileData)
    print("MP3 Conversion for " + file + " complete.")

