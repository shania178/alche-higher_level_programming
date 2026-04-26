#!/usr/bin/python3
import sys
argv = sys.argv
if __name__ == "__main__":
    argc = len(argv) - 1
    if argc == 0:
        print("{} arguments.".format(argc))
    elif argc == 1:
        print("{} argument:".format(argc))
    else:
        print("{} arguments:".format(argc))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
