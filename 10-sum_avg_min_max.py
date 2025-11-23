#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Script to Calculate Sum, avg, min, max for n numbers entered in a single line

numbers = list(map(int,input('Enter the numbers seperated by spaces: ').split()))
print(f"The Sum of Numbers is:{sum(numbers)}")
print(f"The Average of Numbers is:{sum(numbers)/len(numbers)}")
print(f"The Maximum of Numbers is:{max(numbers)}")
print(f"The Minimum of Numbers is:{min(numbers)}")


