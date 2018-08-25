from os.path import isdir
from os import listdir

def Reduce(sourceFolder,targetFile):
    if not isdir(sourceFolder):
        print(sourceFolder,'does not exits.')
        return
    result = {}
    allFiles = [sourceFolder+'\\'+f for f in listdir(sourceFolder) if f.endswith('_map.txt')]
    for f in allFiles:
        with open(f,'r') as fp:
            for line in fp:
                line = line.strip()
                if not line:
                    continue
                key,value = line.split(':')
                result[key] = result.get(key,0)+int(value)
    with open(targetFile,'w',encoding='utf-8') as fp:
        for k,v in result.items():
            fp.write(k + ':' + str(v) + '\n')

if __name__ == '__main__':
    Reduce('test','test\\result.txt')