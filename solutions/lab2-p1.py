#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Event Attendee Management System ( If, For)

names_list = ["Alice", "Bob", "Charlie", "David", "Eve", "Fiona"]
for i in range(6):
    inp_name = input('Enter the name of student: ')
    if inp_name.capitalize() in names_list:
        names_list.remove(inp_name)
        print(f"{inp_name} attendance marked")
    else:
        print(f"{inp_name} student not present")

remaining_students = " ".join(names_list)
print(f"Remaining students are: {remaining_students}")