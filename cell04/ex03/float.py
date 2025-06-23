#!/usr/bin/env python3

# • Create a program called float.py.
# • This program should be executable.
# • Your script will ask the user for a number.
# • You should then display whether the entered number is a decimal or not.
# ?> ./float.py
# Give me a number: 42
# This number is an integer.
# ?>
# ?> ./float.py
# Give me a number: 42.00
# This number is an integer.
# ?>
# ?> ./float.py
# Give me a number: 42.42
# This number is a decimal.
# ?>

number = float(input("Give me a number: "))
if number.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")
