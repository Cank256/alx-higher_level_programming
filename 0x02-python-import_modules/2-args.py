#!/usr/bin/python3
import sys

def main():
    argv = sys.argv[1:]  # Excluding the script name itself
    num_args = len(argv)

    if num_args == 1:
        print(f"{num_args} argument:")
    else:
        if num_args == 0:
            print(f"{num_args} arguments.")
        else: 
            print(f"{num_args} arguments")

    for index, arg in enumerate(argv, start=1):
        print(f"{index}: {arg}")

if __name__ == "__main__":
    main()
