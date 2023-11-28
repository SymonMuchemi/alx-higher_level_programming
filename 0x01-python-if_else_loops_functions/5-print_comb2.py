#!/usr/bin/python3
# print all numbers from 0 to 99
# prefix all nunmbers less than 10 with a zero

for i in range(0, 100):
    if i < 99:
        print("{}".format(str(i).zfill(2)), end=", ")
    else:
        print("{}".format(i))
