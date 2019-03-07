from .Program import Program

class MetaFlacProgram(Program):
    programName         = "metaflac"
    __list              = False
    __block_type        = ""
    ___file             = ""

    def SetDefault(self, file):
        self.__list = True
        self.__block_type = "--block-type=VORBIS_COMMENT"
        self.___file = file
        return self