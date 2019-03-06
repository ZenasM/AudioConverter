from .Program import Program

class MetaFlacProgram(Program):
    programName         = "metaflac"
    __list              = ""
    __block_type        = ""
    ___file             = ""

    def GetDefault(self, file):
        self.__list = "__list"
        self.__block_type = "--block-type=VORBIS_COMMENT"
        self.___file = file
        return self.GetArgList()


    #def GetArgList(self):
    #    argList = [self.programName]
    #    for attr in dir(self):
    #        if not callable(getattr(self, attr)) and not attr.startswith("__") and not attr == "programName":
    #            if getattr(self, attr):
    #                argList.append("--" + attr.replace("_", "-"))
    #    return argList
