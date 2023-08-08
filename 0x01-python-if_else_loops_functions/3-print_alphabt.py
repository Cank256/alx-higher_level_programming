#!/usr/bin/python3
for i in range(26):
    if i == 4 or i == 16:  # Skip 'e' (ASCII value 101) and 'q' (ASCII value 113)
        continue
    print(chr(97 + i), end='')
