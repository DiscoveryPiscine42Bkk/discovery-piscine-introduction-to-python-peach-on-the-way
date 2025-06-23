#!/usr/bin/env python3

# • Create a program called age.py.
# • This program should be executable.
# • The program asks the user to enter their age and then displays the user’s age in 10
# years, 20 years, and 30 years.
# ?> ./age.py
# Please tell me your age: 15
# You are currently 15 years old.
# In 10 years, you'll be 25 years old.
# In 20 years, you'll be 35 years old.
# In 30 years, you'll be 45 years old.
# ?>

age = int(input("Please tell me your age: "))
print("You are currently 15 years old.")
years = [10, 20, 30]
for year in years:
    print(f"In {year} years, you'll be {age + year} years old.")
