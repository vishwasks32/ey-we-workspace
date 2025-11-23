#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Count the number of times a character occurs in a given string
# Eg: 's' in 'Vishwas' -> 2

inp_char = input('Enter the character to search: ')
inp_str = input('Enter the String to be searched in: ')
count = 0
# for idx in range(len(inp_str)):
#     if inp_char == inp_str[idx]:
#         count += 1

for char in inp_str:
    if inp_char == char:
        count += 1

print(f'{inp_char} is found {count} times ')