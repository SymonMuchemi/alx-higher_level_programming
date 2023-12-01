#!/usr/bin/python3
# This program prints the arguments passed to it
if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1
    if argc == 0:
        print("{:d} arguments.".format(argc))
    elif argc > 1:
        print("{:d} arguments:".format(argc))
        for i in range(1, argc + 1):
            print("{:d}: {}".format(i, argv[i]))
    else:
        argc = 1
        print("{:d} argument:".format(argc))
        print("{:d}: {}".format(argc, argv[1]))
