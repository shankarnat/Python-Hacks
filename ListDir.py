#Copies a file in mac from one place and replicates at another place

import sys
import os

dirname = sys.argv[1]

list_files = os.listdir(dirname)
for filenam in list_files:
    print(filenam)
