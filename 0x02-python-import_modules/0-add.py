# 0-add.py
#!/usr/bin/python3

# Import the add function from add_0.py
from add_0 import add

def main():
    # Assign values to variables a and b
    a = 1
    b = 2

    # Call the add function and store the result
    result = add(a, b)

    # Print the formatted output
    print("{} + {} = {}".format(a, b, result))

if __name__ == "__main__":
    main()

