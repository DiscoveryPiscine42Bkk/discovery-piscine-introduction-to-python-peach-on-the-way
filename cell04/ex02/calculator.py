#!/usr/bin/env python3

#  Create a program called calculator.py.
# • This program should be executable.
# • Your script will ask the user for two numbers.
# • You must store these numbers as numerical values in two variables.
# • You should then display the result of their addition, subtraction, division, and multiplication.
# ?> ./calculator.py
# Give me the first number: 10
# Give me the second number: 2
# Thank you!
# 10 + 2 = 12
# 10 - 2 = 8
# 10 / 2 = 5
# 10 * 2 = 20
# ?>

first_number = int(input("Give me the first number: "))
second_number = int(input("Give me the second number: "))
print("Thank you!")
print(f"{first_number} + {second_number} = {first_number + second_number}")
print(f"{first_number} - {second_number} = {first_number - second_number}")
print(f"{first_number} / {second_number} = {first_number / second_number}")
print(f"{first_number} * {second_number} = {first_number * second_number}")
