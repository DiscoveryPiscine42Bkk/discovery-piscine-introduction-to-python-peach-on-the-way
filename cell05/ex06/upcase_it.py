#!/usr/bin/env python3

# • Create a program called upcase_it.py that takes a string as a parameter.
# • This program should be executable.
# • The program should display the string in uppercase, followed by a newline.
# • If the number of parameters is different from 1, display "none" followed by a newline.
# ?> ./upcase_it.py | cat -e
# none$
# ?> ./upcase_it.py "initiation" | cat -e
# INITIATION$
# ?> ./upcase_it.py 'This exercise is quite easy!' | cat -e
# THIS EXERCISE IS QUITE EASY!$
# ?>

import sys

if len(sys.argv) - 1 != 1:
    print("none")
    exit()

print(sys.argv[1].upper())
