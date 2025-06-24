#!/usr/bin/env python3

# • Create a program called free_range.py that takes two parameters.
# • These two parameters will be two numbers.
# • This program should be executable.
# • You must construct an array containing all the values between these two numbers
# using a range. Then, you will display the array using the print function.
# • If the number of parameters is different from 2, you should display ’none’ followed
# by a newline.
# ?> ./free_range.py | cat -e
# none$
# ?> ./free_range.py 10 14 | cat -e
# [10, 11, 12, 13, 14]$
# ?>

import sys

if len(sys.argv) - 1 != 2:
    print("none")
    exit()

start = int(sys.argv[1])
end = int(sys.argv[2])
print([x for x in range(start, end + 1)])
