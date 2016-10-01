#!/usr/bin/python 
#coding: utf-8
#Chinese Char Count
from sys import *

notcc = ' \n!"\'#$%&()*+,-./:;<=>?@[\\]^_`{|}~'
n = 0

def usage():
    print "usage: " + argv[0] + " <filename>"
    exit(-1)

if len(argv) < 2:
    usage()

try:
    for line in open(argv[1]):
        n += len(line.decode("utf-8"))
        for c in line:
            if c in notcc:
                n -= 1
    print n
except IOError:
    usage()
