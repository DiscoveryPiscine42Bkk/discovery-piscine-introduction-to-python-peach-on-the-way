#!/usr/bin/env python3

# • Create a program called count_it.py.
# • This program should be executable.
# • The program will display "parameters:" followed by the number of parameters
# passed as arguments, followed by a newline. Then, for each parameter, it will
# display the parameter itself and its length, followed by a newline.
# • If there are no parameters, it should display "none" followed by a newline.
# ?> ./count_it.py | cat -e
# none$
# ?> ./count_it.py "Game" "of" "Thrones" | cat -e
# parameters: 3$
# Game: 4$
# of: 2$
# Thrones: 7$
# ?>

import sys
if len(sys.argv) - 1 < 1:
    print("none")
    exit()

parameters = sys.argv[1:]
print("parameters:", len(parameters))
for param in parameters:
    print(f"{param}: {len(param)}")
