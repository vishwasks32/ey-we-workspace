#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Script to swap first name & last name
# Eg: 'vishwas singh'
# singh vishwas

fullname = input("Enter the full name: ")
new_name = ""
# fullname.find(' ') != -1
if fullname.find(' ') == -1 or fullname.count(' ') != 1:
    print("Please enter the fullname with format 'first_name last_name'")
else:
    new_name = ' '.join(fullname.split()[::-1])

print(f"{new_name}")
