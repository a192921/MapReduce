import os
import os.path
import time



def FileSpilt(sourceFile,targetFolder):
    if not os.path.isfile(sourceFile):
        print(sourceFile,'does not exits.')
        return
    if not os.path.isdir(targetFolder):
        os.mkdir(targetFolder)
    tempData = []
    number = 1000
    fileNum = 1
    with open(sourceFile,'r',encoding="utf-8",errors='ignore') as srcFile:
        dataLine = srcFile.readline().strip()
        while dataLine:
            for i in range(number):
                tempData.append(dataLine)
                dataLine = srcFile.readline()
                if not dataLine:
                    break
            desFile = os.path.join(targetFolder,str(fileNum)+'.txt')
            with open(desFile,'a+',encoding="utf-8",errors="ignore") as f:
                f.writelines(tempData)
            tempData = []
            fileNum = fileNum + 1



if  __name__ == "__main__":
    sourceFile = "./test.txt"
    targetFolder = 'test'
    FileSpilt(sourceFile,targetFolder)

