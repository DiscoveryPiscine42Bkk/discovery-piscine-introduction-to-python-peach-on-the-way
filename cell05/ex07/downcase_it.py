#!/usr/bin/env python3

# • Create a program called downcase_it.py.
# • This program should be executable.
# • The program takes a string as a parameter.
# • It should display the string in lowercase, followed by a newline.
# • If the number of parameters is different from 1, it should display "none" followed
# by a newline.
# ?> ./downcase_it.py | cat -e
# none$
# ?> ./downcase_it.py "LUCIOLE" | cat -e
# luciole$
# ?> ./downcase_it.py 'This exercise is quite easy!' | cat -e
# this exercise is quite easy!$
# ?>

import sys

if len(sys.argv) - 1 != 1:
    print("none")
    exit()

print(sys.argv[1].lower())
