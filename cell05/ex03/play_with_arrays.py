#!/usr/bin/env python3

# • Take the previous program and modify it to remove duplicates from the output.
# Note that you should not explicitly remove values from your arrays.
# • For example, if your original array is [2, 8, 9, 48, 8, 22, -12, 2], the expected output
# would be:
# ?> ./play_with_arrays.py | cat -e
# [2, 8, 9, 48, 8, 22, -12, 2]$
# {24, 10, 11, 50}$
# ?>

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
print("Original array:", original_array)
print("New set:", set([x + 2 for x in original_array if x > 5]))
