#!/usr/bin/env python3

# • Create a program called string_are_arrays.py that takes a string as a parameter.
# • This program should be executable.
# • When executed, the program should display "z" for each occurrence of the character
# "z" in the string passed as a parameter, followed by a newline.
# • If the number of parameters is different from 1, or if there are no "z" characters in
# the string, it should display "none" followed by a newline.
# ?> ./string_are_arrays.py | cat -e
# none$
# ?> ./string_are_arrays.py "The character Z is not found in this string" | cat -e
# none$
# ?> ./string_are_arrays.py "The character z is found in this string" | cat -e
# z$
# ?> ./string_are_arrays.py "Zaz visits the zoo with Zazie" | cat -e
# zzz$
# ?>

import sys

if len(sys.argv) - 1 != 1:
    print("none")
    exit()

param = sys.argv[1]
count = param.count("z")
if count == 0:
    print("none")
    exit()
print("z" * count)

