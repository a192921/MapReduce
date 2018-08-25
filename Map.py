import os
import re
import threading
import time

def Map(sourceFile):
    if not os.path.exists(sourceFile):
        print(sourceFile,'does not exits.')
        return
    pattern = re.compile(r'\d{4}/\d{1,2}/\d{1,2}')
    #pattern =re.compile(r'[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}')
    result = {}
    with open(sourceFile,'r') as srcFile:
        for dataLine in srcFile:
            r = pattern.findall(dataLine)
            if r:
                result[r[0]] = result.get(r[0],0+1)
    desFile = sourceFile[0:-4] + '_map.txt'
    with open(desFile,'a+',encoding="utf-8",errors="ignore") as fp:
        for k,v in result.items():
            fp.write(k+':'+str(v)+'\n')


if __name__ == '__main__':
    desFolder = './test'
    files = os.listdir(desFolder)
    def Main(i):
        Map(desFolder + '\\' + files[i])
    fileNumber = len(files)
    for i in range(fileNumber):
        t = threading.Thread(target=Main,args=(i,))
        t.start()