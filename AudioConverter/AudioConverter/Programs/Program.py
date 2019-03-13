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
                    if "_WITHNAME" in currentAttrName:  # Variables with _WITHNAME need to have both varname and value as arguments
                        argList.append(currentAttrName.replace("_WITHNAME", "").replace("_", "-"))
                    if isinstance(currentAttrValue, collections.Mapping):
                        for k, v in currentAttrValue.items():
                            argList.append(k + '=' + v)
                    else:
                        argList.append(currentAttrValue)
        return argList
