#!/usr/bin/env python3

x = 0
while x <= 10:
    y = 0
    print("Table de ", x, ": ", end="", sep="")
    while y <= 10:
        print(x*y, end=" ", sep=" ")
        y += 1
    print()
    x += 1
