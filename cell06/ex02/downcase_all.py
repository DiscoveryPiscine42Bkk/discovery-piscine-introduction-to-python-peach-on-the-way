#!/usr/bin/env python3

# • Create a program downcase_all.py.
# • This program must be executable.
# • You must define a method in this program. This method is called downcase_it.
# • The downcase_it method takes a string as an argument. It should return the string
# in lowercase.
# • Apply this method, and display its return value, on the program’s parameters.
# • If there are no parameters, display "none" followed by a line break.
# ?> ./downcase_all.py
# none
# ?> ./downcase_all.py "HELLO WORLD" "I understood Arrays well!"
# hello world
# i understood arrays well!
# ?>

import sys

def downcase_it(str):
    return str.lower()

if len(sys.argv) - 1 < 1:
    print("none")
    exit()

parameters = sys.argv[1:]

for param in parameters:
    print(downcase_it(param))
