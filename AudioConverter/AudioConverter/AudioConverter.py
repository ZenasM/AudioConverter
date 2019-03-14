from Programs.FlacProgram import FlacProgram
import FileOperations
import time
import multiprocessing
import FileConversion

# What about dynamic folders for artists/albums?
# Dependency check. Check for lame/flac?
# Continuous Run. Run a... throttled loop on a folder. 
# Aggregate artist names.
# Cover photos?

def main():
    config = FileOperations.InitVariables()
    flacFiles = FileOperations.GetAllFlacsInFolder(config["currentPath"])

    # Processes V2
    start = time.time()
    allProcess = []
    for file in flacFiles:
        p = multiprocessing.Process(target=FileConversion.TranscodeFlacToMp3, args=(file,))
        allProcess.append(p)
        p.start()

    for pr in allProcess:
        pr.join()
    end = time.time()
    print("Processes V2 Total Time: " + str(end - start))

if __name__ == '__main__':
    main()