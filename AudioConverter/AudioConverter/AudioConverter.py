from Programs.FlacProgram import FlacProgram

# What about dynamic folders for artists/albums?
# Dependency check. Check for lame/flac?
# Continuous Run. Run a... throttled loop on a folder. 
# Aggregate artist names.
# Cover photos?

def main():
    #config = FileOperations.InitVariables()
    #allFiles = FileOperations.getAllElementsInFolder(config["currentPath"])

    #for f in allFiles:
    #    print(f)

    testVar = FlacProgram()
    testVar.GetDefault()
    print(testVar.GetArgList())

if __name__ == '__main__':
        main()