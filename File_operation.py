import os
import pathlib
from DraculaPlugin import *



def File_operation(path,filetype,function):
    if "." not in filetype:
        filetype="."+filetype
    # DraculaLinStamp()
    SavePath=pathlib.Path(path).absolute()
    arr = os.listdir(SavePath)
    for objectFile in arr:
        if os.path.isdir(objectFile):
            print("DIR>> :"+str(SavePath.joinpath(objectFile)))
            File_operation(SavePath.joinpath(objectFile),filetype,function)
        elif filetype in objectFile:
            print(objectFile)
            function(SavePath.joinpath(objectFile))
        # else :
            # print(objectFile)
    # print("All is done!! Finally")
    

def gaga(filepath):
    #適用小檔案
    contents=""
    with open(filepath, 'r+') as f:
        contents=f.read()
        # print(contents)
        if ("mother" in contents and "father" in contents):
            contents=contents.replace("father","")
            contents=contents.replace("mother","mother\nfather")
    print("replace"+contents)
    with open(filepath, 'w+') as a:
        a.write(contents)
    print(contents)

# DraculaLinStamp()
SavePath=pathlib.Path(__file__).parent.absolute()
print(SavePath)
File_operation(SavePath,"txt",gaga)
os.system("pause")

