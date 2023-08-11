#!/usr/bin/python3
import hidden_4


def main():
    names = [name for name in dir(hidden_4) if not name.startswith("__")]
    for name in sorted(names):
        print(name)


if __name__ == "__main__":
    main()
