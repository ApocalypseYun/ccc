#!/usr/bin/python 
#coding: utf-8
#Chinese Char Count
from sys import *

notcc = ' \n!"\'#$%&()*+,-./:;<=>?@[\\]^_`{|}~'
chars = 0
words = 0
lines = 0
def usage():
    print "usage: " + argv[0] + " <filename>"
    exit(-1)

if __name__ == '__main__':
    if len(argv) < 2:
        usage()
    
    try:
        for line in open(argv[1]):
            chars += len(line.decode("utf-8"))
            lines += 1
            
            for c in line:
                if c in notcc:
                    chars -= 1

        print "chars: " + str(chars) + ', lines: ' + str(lines)
    
    except IOError:
        usage()
        
# 待开发
# 1.通过管道通信 实现字符统计 
#   e.g. cat flag.txt | cwc.py 
#   out: chars: xx, lines; yy
