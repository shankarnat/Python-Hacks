#List Files in a Directory passed to the command, if no dir is mentioned then current directory is listed
import sys
import os

dirname = sys.argv
if len(dirname) ==  1 :
    list_files = os.listdir()
elif len(dirname) ==  2 :
    list_files = os.listdir(dirname)
else:
    print("The input is wrong")
    sys.exit()
for filenam in list_files:
    print(filenam)
