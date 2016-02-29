# C_code generator v: 0.0.1 alpha
# Author: Byron Lambrou
import os,sys
import subprocess
import glob
from os import path

#f = open('gen.c', 'w')
#orig_stdout = sys.stdout
#sys.stdout = f

otherf = open('helloworld.by', 'r')

def parser(input):
    if input[0] == 'vg':
        return"int {0} = {1};".format(input[1],input[2])
    if input[0] == 'print':
        return "printf(\"{0}\\n\");".format(input[1])
    else:
        return "//ERROR"

print ("#include <stdio.h>\n")
print ("main(){")

for line in otherf:
    line = line.replace("\n", "")
    print(parser(line.split(" ")))
print("}")
