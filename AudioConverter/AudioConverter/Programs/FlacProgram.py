from .Program import Program

class FlacProgram(Program):
    programName             = "flac"
    __decode                = False
    __stdout                = False
    __silent                = False
    __force                 = False
    __compression_level_0   = False
    __compression_level_1   = False
    __compression_level_2   = False
    __compression_level_3   = False
    __compression_level_4   = False
    __compression_level_5   = False
    __compression_level_6   = False
    __compression_level_7   = False
    __compression_level_8   = False
    __tag                   = {}
    ___file                 = ""

    def SetDecodeDefault(self, file):
        self.__decode = True
        self.__stdout = True
        self.__silent = True
        self.___file = file
        return self

    def SetEncodeDefault(self, file):
        self.__stdout = True
        self.__silent = True
        self.___file = file
        return self