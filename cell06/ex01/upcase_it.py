#!/usr/bin/env python3

# • Create a program upcase_it.py (again!)
# • This program must be executable.
# • You must define a method in this program. This method is called upcase_it.
# • The upcase_it method takes a string as an argument. It should return the string
# in uppercase.
# • Test the method by calling it in your program. In the example below, we test it
# with "hello":
# ?> cat upcase_it.py
# # Your method definition
# print(upcase_it("hello"))
# ?> ./upcase_it.py
# HELLO
# ?>

def upcase_it(str):
    return str.upper()

print(upcase_it("hello"))
