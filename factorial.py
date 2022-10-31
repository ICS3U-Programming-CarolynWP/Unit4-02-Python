# !/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/10/31
# Takes the user input of a positive number and displays
# The factorial.


def main():

    # Title
    print("Product of Numbers: Factorials")

    # Variables for the counter and product
    counter = 1
    product = 1

    # User input for the integer
    integer_input = input("Please enter a positive number: ")

    # Try Catch to make sure the input is an integer
    try:
        input_as_integer = int(integer_input)

    # Exception which tells the user to enter an integer
    except Exception:
        print("Please enter an integer!")

    else:
        # IF statement to make sure the input is positive
        if input_as_integer < 0:
            print("Please enter a positive integer")
        else:
            # "Do While" Loop to calculate the product
            while True:
                product = product * counter
                print("{} x ".format(counter))
                counter = counter + 1
                if counter > input_as_integer:
                    break
            # Answer
            print("The product of all numbers is {}".format(product))


if __name__ == "__main__":
    main()
