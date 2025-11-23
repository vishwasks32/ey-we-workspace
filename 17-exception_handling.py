def add(a,b):
    return a+b

def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Cannot divide by Zero")
        
if __name__ == '__main__':
    print(add(2,3))
    print(div(6,2))
    print(div(9,0))