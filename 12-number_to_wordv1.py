#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Script to convert given number to words
# 0 - 9 in words
# 0 - Zero
# 1 - One

num_words = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
user_inp = input("Enter a number between 0 to 9: ")
if not user_inp.isdigit() or int(user_inp) >= 10:
    print("Enter a valid digit")
else:
    user_inp = int(user_inp)
    print(f"{user_inp} in words is: {num_words[user_inp]}")