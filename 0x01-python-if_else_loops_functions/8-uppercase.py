#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
        print(char, end="")
    print()

# Test cases
if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")

