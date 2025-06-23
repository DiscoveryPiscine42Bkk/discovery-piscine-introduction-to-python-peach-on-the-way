#!/usr/bin/env python3

# • Create a program called aff_first_param.py.
# • This program should be executable.
# • The program displays the first string parameter passed, followed by a newline.
# • If there are no parameters, display "none" followed by a newline.
# ?> ./aff_first_param.py | cat -e
# none$
# ?> ./aff_first_param.py "Code Ninja" "Numerique" "42" | cat -e
# Code Ninja$
# ?>

import sys

if len(sys.argv) - 1 < 1:
    print("none")
    exit()

print(sys.argv[1])
