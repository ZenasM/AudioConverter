import collections
class Program(object):
    def GetArgList(self):
        argList = [self.programName]
        for attr in dir(self):
            currentAttrName = attr.replace("_" + type(self).__name__, "")
            currentAttrValue = getattr(self, attr)
            if not callable(currentAttrValue) and not attr.startswith("__") and not currentAttrName == "programName":
                if currentAttrValue == True:
                    argList.append(currentAttrName.replace("_", "-"))
                elif currentAttrValue == False or len(currentAttrValue) == 0:
                    pass
                else:
                    if not isinstance(currentAttrValue, (list, dict)):
                        if "_WITHNAME" in currentAttrName:  # Variables with _WITHNAME need to have both varname and value as arguments
                            argList.append(currentAttrName.replace("_WITHNAME", "").replace("_", "-"))
                        argList.append(currentAttrValue)
                    else:
                       commandTag = currentAttrName.replace("_WITHNAME", "").replace("_", "-")
                       self.HandleCollections(commandTag, "", currentAttrValue, argList)
        return argList

    def HandleCollections(self, commandTag, possibleAttrName, listOrDict, argList):
        if isinstance(listOrDict, dict):
            for k, v in listOrDict.items():
                if isinstance(v, (list, dict)):
                    self.HandleCollections(commandTag, k, v, argList)
                else:
                    self.AddArgument(commandTag, k + "=" + v, argList)

        elif isinstance(listOrDict, list):
            for v in listOrDict:
                if isinstance(v, (list, dict)):
                    self.HandleCollections(commandTag, "", v, argList)
                else:
                    self.AddArgument(commandTag, possibleAttrName + "=" + v, argList)

    def AddArgument(self, commandTag, commandValue, argList):
        argList.append(commandTag)
        argList.append(commandValue)

# --tv TXXX=CATALOGNUMBER=1234567890
# --tv TPE2=Artist 