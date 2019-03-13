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
        self.__tt_WITHNAME = tagDict["TITLE"]      
        self.__ta_WITHNAME = tagDict["ARTIST"]     
        self.__tl_WITHNAME = tagDict["ALBUM"]      
        self.__ty_WITHNAME = tagDict["YEAR"]       
        self.__tc_WITHNAME = tagDict["COMMENT"]    
        self.__tn_WITHNAME = tagDict["TRACKNUMBER"]
        self.__tg_WITHNAME = tagDict["GENRE"]      
        #self.__tv_WITHNAME = { "TXXX": "Testing=123" }

        # TEST CODE
        
        for k, v in tagDict.items():
            key = process.extractOne(k, ID3Tag.matchingStrings, scorer=fuzz.ratio) # Tuple of (key, ratio)
            # Fuzzy matching doesn't take into account string length. Track and Tracktotal match...
            if key[1] > 80:
                self.__tv_WITHNAME[ID3Tag.matchingDict[key[0]]] = v
            else:
                if not isinstance(self.__tv_WITHNAME["TXXX"], list):
                    self.__tv_WITHNAME["TXXX"] = []
                self.__tv_WITHNAME["TXXX"].append(k + "=" + v)

        # TEST CODE
        #__ti = tagDict[""]
        self.__priority_WITHNAME = "4"
        self.___input = input
        self.___output = output
        return self