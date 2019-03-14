from .Program import Program
from fuzzywuzzy import process, fuzz
import ID3Tag

class LameProgram(Program):
    programName             = "lame"
    quality                 = ""
    __silent                = False
    __decode                = False    
    __tt_WITHNAME           = ""                # Title
    __ta_WITHNAME           = ""                # Artist
    __tl_WITHNAME           = ""                # Album
    __ty_WITHNAME           = ""                # Year
    __tc_WITHNAME           = ""                # Comment
    __tn_WITHNAME           = ""                # Track
    __tg_WITHNAME           = ""                # Genre
    __ti_WITHNAME           = ""                # Album Art
    __tv_WITHNAME           = { "TXXX": [] }    # Custom tags
    __priority_WITHNAME     = ""                # Windows specific
    ___input                = ""
    ___output               = ""

    def SetDefault(self, tagDict, input, output):
        self.quality = "-V0"
        self.__silent = True
        self.__tv_WITHNAME = tagDict
        self.__priority_WITHNAME = "4"
        self.___input = input
        self.___output = output
        return self