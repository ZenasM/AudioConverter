class Program(object):
    def GetArgList(self):
        argList = [self.programName]
        for attr in dir(self):
            currentAttrName = attr.replace("_" + type(self).__name__, "")
            currentAttrValue = getattr(self, attr)
            if not callable(currentAttrValue) and not attr.startswith("__") and not currentAttrName == "programName":
                if currentAttrValue == True:
                    argList.append(currentAttrName.replace("_", "-"))
                elif currentAttrValue == False or currentAttrValue == "":
                    pass
                else:
                    if "_WITHNAME" in currentAttrName:  # Variables with _WITHNAME need to have both varname and value as arguments
                        argList.append(currentAttrName.replace("_WITHNAME", "").replace("_", "-"))
                    argList.append(currentAttrValue)
        return argList
