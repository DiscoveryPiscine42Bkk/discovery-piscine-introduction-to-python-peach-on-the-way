#!/usr/bin/env python3

# • Create a program called play_with_arrays.py.
# • This program should be executable.
# • First, define an array of numbers.
# • Then, iterate over this array and build a new array by adding 2 to each value of
# the original array.
# • You should have two arrays in your program: the original array and the new array
# you created.
# • Finally, display both arrays on the screen.
# • For example, if your original array is [2, 8, 9, 48, 8, 22, -12, 2], you should have the
# following output:
# ?> ./play_with_arrays.py
# Original array: [2, 8, 9, 48, 8, 22, -12, 2]
# New array: [4, 10, 11, 50, 10, 24, -10, 4]
# ?>

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
print("Original array:", original_array)
print("New array:", [x + 2 for x in original_array])
