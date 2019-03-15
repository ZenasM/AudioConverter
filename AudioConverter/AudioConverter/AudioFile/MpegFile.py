import os
import FileConversion
from .AudioFile import AudioFile

class MpegFile(AudioFile):
    def __init__(self, filePath):
        super(MpegFile, self).__init__(filePath)
        self.audioData = FileConversion.DecodeMpeg(filePath)
        self.metaData = RetrieveIdTags(filePath)

    def RetrieveIdTags(self, file):
        pass
