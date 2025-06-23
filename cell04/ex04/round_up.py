#!/usr/bin/env python3

# • Create a program called round_up.py.
# • This program should be executable.
# • Your script will ask the user for a number.
# • You should then display the entered number rounded up.
# ?> ./round_up.py
# Give me a number: 41.42
# 42
# ?>
# ?> ./round_up.py
# Give me a number: 42
# 42
# ?>
# ?> ./round_up.py
# Give me a number: 0.001
# 1
# ?>

import math

number = float(input("Give me a number: "))
print(math.ceil(number))
