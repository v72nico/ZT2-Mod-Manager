import glob2

path = 'C:\\Program Files (x86)\\Microsoft Games\\Zoo Tycoon 2\\'
modfiles = glob2.glob(path+'*.Z2F')
path2 = 'C:\\Program Files (x86)\\Microsoft Games\\Zoo Tycoon 2\\ModsNotinUse\\'
truemodfiles = glob2.glob(path2+'*.Z2F')
totalfiles = modfiles + truemodfiles
activelen = len(modfiles)

def getFileOnly(modfileone):
    lastThing = 0
    FileName = ""
    for i,ele in enumerate(modfileone):
        if modfileone[len(modfileone) - i - 1] == '\\':
            lastThing = len(modfileone) - i - 1
            break
    for i,ele in enumerate(modfileone):
        for j in range(lastThing + 1, len(modfileone)):
            if i ==  j:
                FileName += modfileone[i]
    return FileName
    
filesOnly = []
for direc in totalfiles:
    filesOnly.append(getFileOnly(direc))

print(filesOnly)