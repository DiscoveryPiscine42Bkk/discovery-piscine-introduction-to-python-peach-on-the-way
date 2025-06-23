#!/usr/bin/env python3

# • Create a program called aff_rev_params.py.
# • This program should be executable.
# • When executed, the program should display all the strings passed as parameters,
# followed by a newline, in reverse order.
# • If there are fewer than two parameters, it should display none followed by a newline.
# ?> ./aff_rev_params.py | cat -e
# none$
# ?> ./aff_rev_params.py "coucou" | cat -e
# none$
# ?> ./aff_rev_params.py "Python" "piscine" "hello" | cat -e
# hello$
# piscine$
# Python$
# ?>

import sys

if len(sys.argv) - 1 < 2:
    print("none")
    exit()

array = sys.argv[1:]
array = reversed(array)
for a in array:
    print(a)
