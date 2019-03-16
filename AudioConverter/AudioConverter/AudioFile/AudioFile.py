import os
import FileConversion

class AudioFile(object):
    filePath = ""
    fileName = ""
    fileType = ""
    rawAudioData = ""
    metaData = ""

    def __init__(self, filePath):
        self.filePath = filePath
        self.fileName, self.fileType = os.path.splitext(os.path.basename(filePath))

    def RetrieveIdTags(self):
        pass
