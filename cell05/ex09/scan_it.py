#!/usr/bin/env python3

# • Create a program called scan_it.py.
# • This program should take two parameters.
# • The first parameter is a keyword to search for in a string.
# • The second parameter is the string to be searched.
# • This program should be executable.
# • When executed, the program should display the number of times the keyword ap-
# pears in the string.
# • If the number of parameters is different from 2 or if the first string does not appear
# in the second, it should display none followed by a newline.
# ?> ./scan_it.py | cat -e
# none$
# ?> ./scan_it.py "the" | cat -e
# none$
# ?> ./scan_it.py "the" "the quick brown fox jumps over the lazy dog" | cat -e
# 2$
# ?>

import sys
import re

if len(sys.argv) - 1 != 2:
    print("none")
    exit()

keyword = sys.argv[1]
string = sys.argv[2]
result = re.findall(keyword, string)
if result:
    print(len(result))
else:
    print("none")
