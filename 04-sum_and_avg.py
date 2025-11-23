#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Sum and average of Numbers taken from a user until the user enters -999
# not including -999

total = 0
numbers = ""
while True:
    num = int(input("Enter the number: "))
    if num == -999:
        break
    total += num


print(f"The Sum of [{numbers}] Numbers is: {total}")
print(f"Average of [{numbers}] Numbers is: {total/10}")