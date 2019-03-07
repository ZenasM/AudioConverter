from .Program import Program

class LameProgram(Program):
    programName             = "lame"
    quality                 = ""
    __silent                = False
    __decode                = False    
    __tt_WITHNAME           = ""        # Title
    __ta_WITHNAME           = ""        # Artist
    __tl_WITHNAME           = ""        # Album
    __ty_WITHNAME           = ""        # Year
    __tc_WITHNAME           = ""        # Comment
    __tn_WITHNAME           = ""        # Track
    __tg_WITHNAME           = ""        # Genre
    __ti_WITHNAME           = ""        # Album Art
    __priority_WITHNAME     = ""        # Windows specific
    ___input                = ""
    ___output               = ""


    def SetDefault(self, tagDict, input, output):
        self.quality = "-V0"
        self.__silent = True
        self.__tt_WITHNAME = tagDict["TITLE"]      
        self.__ta_WITHNAME = tagDict["ARTIST"]     
        self.__tl_WITHNAME = tagDict["ALBUM"]      
        self.__ty_WITHNAME = tagDict["YEAR"]       
        self.__tc_WITHNAME = tagDict["COMMENT"]    
        self.__tn_WITHNAME = tagDict["TRACKNUMBER"]
        self.__tg_WITHNAME = tagDict["GENRE"]      
        #__ti = tagDict[""]
        self.__priority_WITHNAME = "4"
        self.___input = input
        self.___output = output
        return self