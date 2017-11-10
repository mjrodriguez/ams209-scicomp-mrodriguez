def writeFiles(N):
    for i in range(1,N+1):
        fileName = 'junk_'+str(i)+'.txt'
        f = open(fileName,'w')
        f.write('This is '+fileName)
        f.close()
        
def readFiles(N):
    for i in range(1,N+1):
        fileName = 'junk_'+str(i)+'.txt'
        f = open(fileName,'r')
        fread = f.read()
        print fread
        f.close()
        est
def removeFiles():
    import os
    os.system('rm junk*.txt')
    print os.listdir(os.getcwd())
    # for i in range(1,N+1):
    #     fileName = 'junk_'+str(i)+'.txt'
    #     os.remove(fileName)
        
####################################################
# ^ Function implemenations above
###################################################

if __name__ == "__main__":
    writeFiles(5)
    readFiles(5)
    
    removeFiles()