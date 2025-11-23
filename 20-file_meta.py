#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Get information from a particular file provided by the user
# Number of Words, Number of Lines, Number of Characters
# Log it to a file

def extract_count_of_words(input_text):
    return len(input_text.split())

def summary_writer(op_file,**kwargs):
    try:
        with open(op_file, "+a") as fh:
            for k,v in kwargs.items():
                fh.write(f"{k}:{v}")
    except FileExistsError:
        print("File Exists")

if __name__ == '__main__':
    fname = input("Enter the file name: ")
    count_of_lines = 0
    count_of_words = 0
    try:
        with open(fname,"r") as fh:
            lines = fh.readlines()
            count_of_lines = len(lines)
            for line in lines:
                count_of_words += extract_count_of_words(line)
        
        summary_writer("summary.log",count_of_lines=count_of_lines,count_of_words=count_of_words)
    except FileNotFoundError:
        print("File is not found")