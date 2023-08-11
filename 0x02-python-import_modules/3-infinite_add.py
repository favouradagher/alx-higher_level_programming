#!/usr/bin/python3

import sys

def main():
    # Get all arguments as integers and sum them up
    total_sum = sum(int(arg) for arg in sys.argv[1:])

    # Print the total sum
    print(total_sum)

if __name__ == "__main__":
    main()

