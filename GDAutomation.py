import os
import shutil

def addNewFiles(dirName):
    global localPath, serverPath
    localSubPath = os.path.join(localPath,dirName)
    serverSubPath = os.path.join(serverPath, dirName)
    localFiles = os.listdir(localSubPath)
    serverFiles = os.listdir(serverSubPath)
    
    for file in localFiles:
        localSubFile = localSubPath + "\\" + file
        #check if the same file is directory
        if file in serverFiles:
            if (os.path.isdir(localSubFile)):
                addNewFiles(dirName + "\\" + file)
        #add localFile to serverFile
        else: 
            shutil.copyfile(localSubFile, serverSubPath)
    
    for file in serverFiles:
        serverSubFile = serverSubPath + "\\" + file
        if (file in localFiles):
            shutil.copyfile(serverSubFile, localSubPath)
            
    
def main():
    global localPath, serverPath
    localPath = "D:\\"
    serverPath = "C:Users\\Stephen\\Google Drive"
    folderName = "School"
    
    local = localPath + "\\" + folderName
    server = serverPath + "\\" + folderName
    
    addNewFiles(folderName)
    #file mover from local to server
    #file mover from server to local
    

if __name__=="__main__" : main()