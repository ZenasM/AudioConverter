from .Program import Program

class LameProgram(Program):
    programName             = "lame"
    quality                 = ""
    __silent                = False
    __decode                = False    
    __tt                    = ""        # Title
    __ta                    = ""        # Artist
    __tl                    = ""        # Album
    __ty                    = ""        # Year
    __tc                    = ""        # Comment
    __tn                    = ""        # Track
    __tg                    = ""        # Genre
    __ti                    = ""        # Album Art
    __priority              = ""       # Windows specific
    ___input                = ""
    ___output               = ""

    def GetDefault(self, input, output):
        self.quality = "-V0"
        self.silent = True
        #self.__priority = "--priority4"
        self.___input = input
        self.___output = output
        return self.GetArgList()
