#!/usr/bin/env python3

# • Create a program called parameters.py.
# • This program should be executable.
# • The program will display the number of parameters passed to it, followed by a
# newline.
# ?> ./parameters.py
# Number of parameters: 0.
# ?> ./parameters.py "initiation"
# Number of parameters: 1.
# ?> ./parameters.py "this" "is" "crazy" "there's" "everywhere!"
# Number of parameters: 5.
# ?>

import sys

print("Number of parameters:", len(sys.argv) - 1)
