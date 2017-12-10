#List Files in a the current Directory
import os

list_files = os.listdir()
for filenam in list_files:
    print(filenam)

#This shows the hidden files too; we need to figure out how to hide them
#Also print the list files in a single line seperated by spaces. 
