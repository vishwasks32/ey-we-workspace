#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Given a string count the frequency of characters

inp_str = input("Enter the string: ")
char_counts = {}
for char in inp_str:
    # Check if the character exists in the dictionary
    # if it Exists
    # Increase the count
    # if not set to 1
    # char_counts[char] = char_counts.get(char,0)+ 1
    if char in char_counts.keys():
        char_counts[char] += 1
    else:
        char_counts[char] = 1


print(f"Frequency of characters: {char_counts}")