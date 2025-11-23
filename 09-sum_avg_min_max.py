#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Script to Calculate Sum, avg, min, max for n numbers until user enters -999

numbers = []
while True:
    num = int(input('Enter the number(-999 to quit): '))
    if num == -999:
        break

    numbers.append(num)

print(f"The Sum of Numbers is:{sum(numbers)}")
print(f"The Average of Numbers is:{sum(numbers)/len(numbers)}")
print(f"The Maximum of Numbers is:{max(numbers)}")
print(f"The Minimum of Numbers is:{min(numbers)}")


