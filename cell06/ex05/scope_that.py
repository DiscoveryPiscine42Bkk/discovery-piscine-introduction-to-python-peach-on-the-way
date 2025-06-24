#!/usr/bin/env python3

# • Create a program called scope_that.py that does not take any parameters.
# • This program must be executable.
# • Inside the program, create a method called add_one that takes a parameter and
# adds 1 to the parameter passed to the method.
# • Initialize a variable in the body of the program, display it, and then call the method
# that adds 1.
# • Display your variable again in the body of the program.
# • What do you observe?

def add_one(param):
    param + 1

variable = 5
print(variable)
add_one(variable)
print(variable)

# variable do not change!
