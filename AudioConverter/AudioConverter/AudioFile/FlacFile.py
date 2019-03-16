import os
import subprocess
import re
import FileConversion
import ID3Tag
import concurrent.futures
from .AudioFile import AudioFile
from fuzzywuzzy import process, fuzz
from Programs.MetaFlacProgram import MetaFlacProgram
from Programs.FlacProgram import FlacProgram


class FlacFile(AudioFile):
    def __init__(self, filePath=""):
        if not len(filePath) == 0:
            super(FlacFile, self).__init__(filePath)
            #self.rawAudioData = self.Decode(filePath)
            #self.metaData = self.RetrieveIdTags(filePath)

    def RetrieveIdTags(self, file):
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

    def Encode(self):
        if len(rawAudioData) == 0:
            self.rawAudioData = self.Decode(self.filePath)
        if len(metaData) == 0:
            self.metaData = self.RetrieveIdTags(self.filePath)

    def Decode(self, file):
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
        tagsResult = executor.submit(self.RetrieveIdTags, file)
        dataResult = executor.submit(self.DecodeFlacData, file)
        tags = tagsResult.result()
        data = dataResult.result()
        return [ data, tags ]
    
    def DecodeFlacData(self, file):
        flacArgs = FlacProgram().SetDecodeDefault(file).GetArgList()
        flacProcess = subprocess.Popen(flacArgs, stdout=subprocess.PIPE,)
        decodedData = flacProcess.communicate()[0]   # Returns tuple (stdout, stderr). We only care about the raw data from stdout.
        print("Decoding " + file + " complete.")
        return decodedData
