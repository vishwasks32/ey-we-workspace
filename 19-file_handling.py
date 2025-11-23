try:
    with open(r"C:\Users\VishwasKSingh\Workspace\ey-we-workspace\14-number_guess.py","r") as fh:
        contents = fh.readlines()
        print(contents)
except FileNotFoundError:
    print('File Not Found')
