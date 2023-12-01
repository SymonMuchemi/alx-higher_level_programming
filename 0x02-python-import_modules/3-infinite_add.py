#!/usr/bin/python3
# This program adds all the passed arguments

if __name__ == "__main__":
    from sys import argv
    sum = 0
    argc = len(argv)
    if argc == 1:
        print("{:d}".format(argc - 1))
    else:
        for i in range(1, argc):
            sum += int(argv[i])
        print("{:d}".format(sum))
