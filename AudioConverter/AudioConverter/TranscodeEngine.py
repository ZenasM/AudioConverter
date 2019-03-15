# Transcode Engine module

supportedTypes = [ ".flac", ".mp3" ]

def Transcode(self, fromAudioFile, toAudioFile):
    if not isinstance([fromAudioFile.fileType, toAudioFile.fileType], supportedTypes):
        raise TypeError("Attempting to transcode from or to an unsupported type!")
