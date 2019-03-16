import os
import FileConversion
from .AudioFile import AudioFile

class MpegFile(AudioFile):
    def __init__(self, filePath=""):
        if not len(filePath) == 0:
            super(MpegFile, self).__init__(filePath)
            self.rawAudioData = self.Decode(filePath)
            self.metaData = self.RetrieveIdTags(filePath)

    def RetrieveIdTags(self, file):
        pass

    def EncodeMp3(rawData, metaData, output):
        outputFile = file[:-5] + ".mp3"
        if "output" in keyword_parameters:
            outputFile = keyword_parameters["output"]

        lameArgs = LameProgram().SetEncodeDefault(metaData, "-", outputFile).GetArgList()
        lameProcess = subprocess.Popen(lameArgs, stdin=subprocess.PIPE)
        lameProcess.communicate(input=rawData)
        print("MP3 Conversion for " + file + " complete.")


    def Decode(self, file):
        pass