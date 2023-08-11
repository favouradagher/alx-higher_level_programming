#!/usr/bin/python3

# Import functions from calculator_1.py
from calculator_1 import add, sub, mul, div

    # Assign values to variables a and b
a = 10
b = 5

    # Call each of the imported functions and store the result
addition_result = add(a, b)
subtraction_result = sub(a, b)
multiplication_result = mul(a, b)
division_result = div(a, b)

    # Print the formatted outputs
if __name__=="__main__":
    print("{} + {} = {}".format(a, b, addition_result))
    print("{} - {} = {}".format(a, b, subtraction_result))
    print("{} * {} = {}".format(a, b, multiplication_result))
    print("{} / {} = {}".format(a, b, division_result))



