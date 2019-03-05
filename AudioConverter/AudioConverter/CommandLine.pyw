class CommandLine(object):
    
    programType = ""
    decode = ""
    stdin = ""
    stdout = ""
    silent = ""
    list = ""
    blockType = ""


    def GetArguments(self, type):
        args = self.GetDefault(type)
        return args

    def GetDefault(self, type):
        if type == 'flac':
            SetDefaultFlac(self)
        #return self.


    def SetDefaultFlac(self):
        self.programType = "flac"
        self.decode = True
        self.stdout = True
        self.silent = True

    #def ToArgList(self):
