import FileOperations
# Import flac api

# Temp
testPath = r"C:\Users\Zenas\Desktop\Flacs"

# Define path and variables here.
fileInput = "fileInput"
fileOutputFlac = "fileOutput"
fileOutputMp3 = "fileOutputMp3"
continuousRun = None
cleanUp = None
# What about dynamic folders for artists/albums?

def initVariables():
    continuousRun = input("Run continuously? ")
    while continuousRun != "Y" and continuousRun != "N":
        print("Try that again.")
        continuousRun = input("Run continuously? ")

    cleanUp = input("Delete original after conversion? ")
    while cleanUp != "Y" and cleanUp != "N":
        print("Try that again.")
        cleanUp = input("Run continuously? ")

# Check for lame/flac?
# Run a... throttled loop on a folder.
# Aggregate artist names.
# Cover photos?

def main():
    allFiles = FileOperations.getAllElementsInFolder(testPath)
    for f in allFiles:
        print(f)

if __name__ == '__main__':
        main()