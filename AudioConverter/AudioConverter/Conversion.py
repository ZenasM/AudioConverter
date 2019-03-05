import subprocess
# Conversion module

def FlacDecode(file):
    flacArgs = ["flac", "--decode", "--stdout", "--silent", file]
    flacProcess = subprocess.Popen(flacArgs, stdout=subprocess.PIPE,)
    decodedData = flacProcess.communicate()[0]   # Returns tuple (stdout, stderr). We only care about the raw data from stdout.
    print("Decoding " + file + " complete.")
    return decodedData

def ConvertMp3(file, rawData):
    lameArgs = ["lame", "--silent", "-V0", "-", file[:-5] + ".mp3"]
    lameProcess = subprocess.Popen(lameArgs, stdin=subprocess.PIPE)
    lameProcess.communicate(input=rawData)
    print("MP3 Conversion for " + file + " complete.")

def ConvertFlacToMp3(file):
    rawData = FlacDecode(file)
    ConvertMp3(file, rawData)

    #def ConverToFlac(inputPath, outputPath):
    #    command = ["flac", ""]
    #    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #    stdout, stderr = process.communicate()

    #def ConverToMp3V0(inputPath, outputPath):
    #    command = ["lame", "-V0", inputPath, outputPath]
    #    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #    stdout, stderr = process.communicate()



