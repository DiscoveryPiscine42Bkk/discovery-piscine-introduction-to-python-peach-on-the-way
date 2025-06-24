#!/usr/bin/env python3

# • Create a program methods_everywhere.py that takes parameters.
# • This program must be executable.
# • You must create two different methods in this program:
# • The method shrink takes a string as a parameter and displays the first eight
# characters of that string.
# • The method enlarge takes a string as a parameter and appends ’Z’ characters to
# make it a total of eight characters. Then, it displays the resulting string.
# • For each argument of the program: if the argument has more than eight characters,
# call the shrink method on it; if the argument has less than eight characters, call
# the enlarge method on it; and if the argument has exactly eight characters, display
# it directly followed by a new line.
# • If the number of parameters is less than 1, display ’none’ followed by a new line.
# ?> ./methods_everywhere.py | cat -e
# none$
# ?> ./methods_everywhere.py 'lol' 'physically' 'backpack' | cat -e
# lolZZZZZ$
# physical$
# backpack$
# ?>

import sys

if len(sys.argv) - 1 < 1:
    print("none")
    exit()

def shrink(str):
    return str[:8]

def enlarge(str):
    count = 8 - len(str)
    return str + "Z" * count

parameters = sys.argv[1:]

for param in parameters:
    param_len = len(param)
    if param_len > 8:
        print(shrink(param))
    elif param_len < 8:
        print(enlarge(param))
    else:
        print(param)
