# This program prints the arguments passed to it
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    if argc == 1:
        print("{:d} arguments.".format(argc - 1))
    elif argc > 2:
        print("{:d}: arguments:".format(argc))
        for i in range(1, argc):
            print("{:d}: {}".format(i, sys.argv[i]))
    else:
        argc = 1
        print("{:d} argument:".format(argc))
        print("{:d}: {}".format(argc, sys.argv[1]))
