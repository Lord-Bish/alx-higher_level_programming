#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    num = len(sys.argv) - 1
    for i in range(1, num + 1):
        result += int(sys.argv[i])
    print("{:d}".format(result))
