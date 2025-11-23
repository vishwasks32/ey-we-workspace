v = 1000
def func_name():
    print(f"Value of v in func_name() level is : {v}")
    print("I am inside func_name()")

def add(a,b):
    print(f"Value of v in add() level is : {v}")
    return a+b


if __name__ == '__main__':
    k = add(2,3)