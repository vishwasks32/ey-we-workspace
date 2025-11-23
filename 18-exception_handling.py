# try:
#     val = int(input("Enter a number: "))
# except ValueError:
#     print("It is not a valid number")
# else:
#     print(f"10 divided by {val} is {10/val}")

try:
    fh = open("example.txt", "r")
except FileNotFoundError:
    print("file is not found")
finally:
    if 'fh' in locals():
        fh.close()
        print("File Closed")