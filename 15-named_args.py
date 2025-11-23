def user_profile_display(*args,**kwargs):
    for i in args:
        print(i)

    print("|property|Value|")
    for k,v in kwargs.items():
        print(f"|{k}|{v}|")

if __name__ == '__main__':
    user_profile_display("Vishwas","Singh")
    print("-"*10)
    user_profile_display(name="Vishwas",age="25",salary="25000")
    print("-"*10)
    user_profile_display("Sireesha","Arjun","Lakshmi",name="Vishwas",age="25",salary="25000",location="City")
