#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Given a string print the left, right & center justified string version with a max sreen width of 80 Columns
# Vishwas
# Vishwas
#                                                         Vishwas
#                            Vishwas

MAX_COLUMNS = 80
inp_str = input("Enter the String to be justified: ")
# print(f"{inp_str}")
# right_jstring = '-'*(MAX_COLUMNS - len(inp_str))+ inp_str
# print(right_jstring)

print(f"{inp_str.ljust(80,"-")}")
print(f"{inp_str.rjust(80,"-")}")
#print(f"{inp_str.center(80,"-")}")
center_jsting = '-'*((MAX_COLUMNS //2 - len(inp_str)// 2)-1)+ inp_str+ '-'*(MAX_COLUMNS//2 - len(inp_str)// 2)
print(f"{center_jsting}")