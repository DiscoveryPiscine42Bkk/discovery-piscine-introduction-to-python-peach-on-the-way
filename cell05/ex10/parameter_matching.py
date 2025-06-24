#!/usr/bin/env python3

# • Create a program called parameter_matching.py.
# • This program should be executable.
# • If a parameter is passed as an argument to the program, it should prompt the user
# to enter a word.
# • If the word entered by the user is the same as the parameter passed, the program
# should display "Good job!". Otherwise, it should display "Nope, sorry..." followed
# by a newline.
# • If the number of parameters passed to the program is different from 1, it should
# display "none" followed by a newline.
# ?> ./parameter_matching.py
# none
# ?> ./parameter_matching.py "Hello"
# What was the parameter? Bonjour
# Nope, sorry...
# ?> ./parameter_matching.py "Hello"
# What was the parameter? Hello
# Good job!
# ?>

import sys

if len(sys.argv) - 1 != 1:
    print("none")
    exit()

param = sys.argv[1]
param_check = input("What was the parameter? ")
if param_check == param:
    print("Good job!")
else:
    print("Nope, sorry...")
