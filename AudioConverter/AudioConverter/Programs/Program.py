class Program(object):
    def GetArgList(self):
        argList = [self.programName]
        for attr in dir(self):
            currentAttr = getattr(self, attr)
            if not callable(currentAttr) and not attr.startswith("__") and not attr == "programName":
                if currentAttr == True:
                    argList.append("--" + attr.replace("_", "-"))
                elif currentAttr == False or currentAttr == "":
                    pass
                else:
                    argList.append(currentAttr)
        return argList
