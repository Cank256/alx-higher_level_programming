#!/usr/bin/python3
for i in range(25, -1, -1):
    c = chr(122 - i) if i % 2 == 0 else chr(90 - (i - 1))
    print("{}".format(c), end="")
