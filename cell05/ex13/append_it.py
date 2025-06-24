#!/usr/bin/env python3

# • Create a program called append_it.py.
# • This program should be executable.
# • The program will display each parameter passed as an argument, one by one, by
# appending it with "ism".
# • If the parameter already ends with "ism", it will be skipped and not displayed. If
# there are no parameters, it should display "none" followed by a newline.
# ?> ./append_it.py | cat -e
# none$
# ?> ./append_it.py "parallel" "egoism" "human" | cat -e
# parallelism$
# humanism$
# ?>

import sys

if len(sys.argv) - 1 < 1:
    print("none")
    exit()

parameters = sys.argv[1:]
for param in parameters:
    if param.endswith("ism"):
        continue
    print(f"{param}ism")

