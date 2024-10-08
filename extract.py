import os
import shutil
def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            if(fullPath.endswith('.webp')):
                allFiles.append(fullPath)
                
    return allFiles

#dirname = '/2way' #Your Full Path of Projects Folder
#dest="/gif_extract/gif_data/"

base_dir = os.path.dirname(os.path.abspath(__file__))
dest = os.path.join(base_dir, "filtered_data/")
#alpha_dest = os.path.join(base_dir, "alphabet/")

data=getListOfFiles(dirname)
for i in range(len(data)):
    fname=dest+str(i)+".webp"
    shutil.copyfile(data[i], fname)
