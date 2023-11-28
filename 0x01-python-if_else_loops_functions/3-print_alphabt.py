#!/usr/bin/python3
# prints all ASCII lowercase letters
# excluding q and e

for i in range(97, 123):
    if (i == 101) or (i == 113):
        continue
    print("{}".format(chr(i)), end="")
