v = 1000
def func_name():
    print(f"Value of v in func_name() level is : {v}")
    print("I am inside func_name()")

def add(a,b, c=10):
    print(f"Value of v in add() level is : {v}")
    return a+b+c

def greet(username, prepend="Hello", append='Welcome to session'):
    return prepend + ' '+ username + ' ' + append

def add(*args):
    total = 0
    print(type(args))
    for num in args:
        total += num
    
    return total

if __name__ == '__main__':
    print(greet('Vishwas',append='Welcome to python Session'))
    print(add(2,3,4,5))
    print(add(10,20))