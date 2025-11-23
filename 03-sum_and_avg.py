#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Sum and average of 10 Numbers taken from the user

total = 0
numbers = ""
for i in range(10):
    num = float(input("Enter the Number: "))
    if i==0:
        numbers += str(num)
    else:
        numbers = numbers + "," + str(num)
    
    total += num

print(f"The Sum of [{numbers}] Numbers is: {total}")
print(f"Average of [{numbers}] Numbers is: {total/10}")