import os
import subprocess
import re
import FileConversion
import ID3Tag
from .AudioFile import AudioFile
from fuzzywuzzy import process, fuzz
from Programs.MetaFlacProgram import MetaFlacProgram

class FlacFile(AudioFile):
    def __init__(self, filePath):
        super(FlacFile, self).__init__(filePath)
        self.audioData = FileConversion.DecodeFlacData(filePath)
        self.metaData = self.RetrieveIdTags(filePath)

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
