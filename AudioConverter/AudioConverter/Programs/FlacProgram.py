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
    ___file                 = ""

    def GetDefault(self, file):
        self.decode = True
        self.stdout = True
        self.silent = True
        self.___file = file
        return self.GetArgList()

    #def GetArgList(self):
    #    argList = [self.programName]
    #    for attr in dir(self):
    #        if not callable(getattr(self, attr)) and not attr.startswith("__") and not attr == "programName":
    #            if getattr(self, attr):
    #                argList.append(attr.replace("_", "-"))
    #    return argList
