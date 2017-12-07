import os
import sys

cwd = os.getcwd()

print(cwd)
op = sys.argv[1]
os.remove(op)
