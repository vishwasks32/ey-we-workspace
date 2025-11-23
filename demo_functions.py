v = 1000
def func_name():
    print(f"Value of v in func_name() level is : {v}")
    print("I am inside func_name()")

def add(a,b, c=10):
    print(f"Value of v in add() level is : {v}")
    return a+b+c

def greet(username, prepend="Hello", append='Welcome to session'):
    return prepend + ' '+ username + ' ' + append

if __name__ == '__main__':
    print(greet('Vishwas',append='Welcome to python Session'))