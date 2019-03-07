from Programs.FlacProgram import FlacProgram
import FileOperations
import time
import multiprocessing
import FileConversion
import asyncio

# What about dynamic folders for artists/albums?
# Dependency check. Check for lame/flac?
# Continuous Run. Run a... throttled loop on a folder. 
# Aggregate artist names.
# Cover photos?

async def main():
    #config = FileOperations.InitVariables()
    #allFiles = FileOperations.getAllElementsInFolder(config["currentPath"])

    #for f in allFiles:
    #    print(f)

    #testVar = FlacProgram()
    #testVar.GetDefault()
    #print(testVar.GetArgList())

    mypath = r"C:\Users\Zenas\Desktop\Flacs"
    f = FileOperations.getAllFlacsInFolder(mypath)

    # Processes V2
    start = time.time()
    allProcess = []
    for file in f:
        p = multiprocessing.Process(target=FileConversion.ConvertFlacToMp3, args=(file,))
        allProcess.append(p)
        p.start()

    for pr in allProcess:
        pr.join()
    end = time.time()
    print("Processes V2 Total Time: " + str(end - start))

if __name__ == '__main__':
        asyncio.run(main())