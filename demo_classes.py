class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__balance = 1000

    def print_age(self):
        print(self.age)


p1 = Person('Vishwas', 25)

print(p1.name)
print(p1.age)
p1.print_age()
p2 = Person('Singh', 45)
print(p2.name)
print(p2.age)
p2.print_age()
p1.print_age()
p1.salary = 250000

print(p1.salary)
print(p1.__balance)