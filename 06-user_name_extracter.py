#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Script to extract user name from email id
# Eg: vishwas@cloudthat.com
# username: vishwas

inp_str = input("Enter the email Id: ")
user_name = inp_str[:inp_str.find('@')]
print(f"Extracted User name: {user_name}")