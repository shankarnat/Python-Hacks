#Copies the input file to output files
#if input file in current directory - full dir path is not required
#if output file full dir path not mentioned - would be copied to current dirname

import shutil
import os
import sys

cwd = os.getcwd()
inputfile = sys.argv[1]
outputfile = sys.argv[2]
inpdir = ""
opdir = ""

#Handle for Directory structure
if "/" not in inputfile:
    inpdir = cwd + "/"
if "/" not in outputfile:
    opdir = cwd + "/"

shutil.copy2(inpdir+inputfile, opdir+outputfile)
