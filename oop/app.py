# class and object
class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def show(self):
        print(self.name,self.age)

p1=Person("rahul",22)
p2=Person("sita",20)
p1.show()
p2.show()


# inheritance
class Student(Person):
    def __init__(self,n,a,r):
        super().__init__(n,a)
        self.roll=r
    def show(self):
        print(self.name,self.age,self.roll)

s1=Student("rohit",21,101)
s1.show()


# multilevel inheritance
class A:
    def x(self):
        print("A")

class B(A):
    def y(self):
        print("B")

class C(B):
    def z(self):
        print("C")

c1=C()
c1.x()
c1.y()
c1.z()


# multiple inheritance
class Father:
    def house(self):
        print("house")

class Mother:
    def gold(self):
        print("gold")

class Child(Father,Mother):
    def bike(self):
        print("bike")

ch=Child()
ch.house()
ch.gold()
ch.bike()


# polymorphism
class Animal:
    def sound(self):
        print("sound")

class Dog(Animal):
    def sound(self):
        print("bark")

class Cat(Animal):
    def sound(self):
        print("meow")

d=Dog()
c=Cat()
d.sound()
c.sound()


# encapsulation
class Bank:
    def __init__(self):
        self.__bal=0
    def set(self,x):
        self.__bal=x
    def get(self):
        return self.__bal

b=Bank()
b.set(5000)
print(b.get())


# abstraction
from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self,s):
        self.s=s
    def area(self):
        print(self.s*self.s)

sq=Square(5)
sq.area()


# constructor
class Mobile:
    def __init__(self,b,r):
        self.brand=b
        self.rate=r

m1=Mobile("samsung",12000)
m2=Mobile("realme",9000)
print(m1.brand,m1.rate)
print(m2.brand,m2.rate)


# destructor
class Test:
    def __del__(self):
        print("destroy")

t1=Test()
del t1


# static variable
class Car:
    tyres=4
    def __init__(self,n):
        self.name=n

c1=Car("swift")
c2=Car("alto")
print(Car.tyres)


# static method
class Math:
    @staticmethod
    def add(a,b):
        print(a+b)

Math.add(5,6)


# instance method
class User:
    def login(self):
        print("login user")

u=User()
u.login()


# class method
class College:
    cname="abc"
    @classmethod
    def ch(cls):
        print(cls.cname)

College.ch()


# getter setter
class Employee:
    def __init__(self):
        self.__sal=0
    def set(self,x):
        self.__sal=x
    def get(self):
        return self.__sal

e=Employee()
e.set(25000)
print(e.get())


# composition
class Engine:
    def start(self):
        print("engine start")

class Bike:
    def __init__(self):
        self.eng=Engine()
    def ride(self):
        self.eng.start()
        print("bike ride")

b=Bike()
b.ride()


# aggregation
class Dept:
    def __init__(self,n):
        self.name=n

class Clg:
    def __init__(self,d):
        self.dept=d

d1=Dept("CS")
c1=Clg(d1)
print(c1.dept.name)


# duck typing
class Laptop:
    def work(self):
        print("coding")

class Human:
    def work(self):
        print("typing")

def call(x):
    x.work()

call(Laptop())
call(Human())


# operator overloading
class Point:
    def __init__(self,a):
        self.a=a
    def __add__(self,o):
        return self.a+o.a

p1=Point(5)
p2=Point(10)
print(p1+p2)


# method overriding
class Phone:
    def call(self):
        print("normal call")

class SmartPhone(Phone):
    def call(self):
        print("video call")

s=SmartPhone()
s.call()


# enum
from enum import Enum

class Role(Enum):
    ADMIN=1
    USER=2
    GUEST=3

print(Role.ADMIN)
print(Role.USER)

# another examples

from enum import Enum

class Status(Enum):
    OK=1
    FAIL=2
    WAIT=3

print(Status.OK)
print(Status.FAIL)




# real life student system
class Student2:
    def __init__(self,n,m):
        self.name=n
        self.marks=m
    def result(self):
        print(self.name,self.marks)

st1=Student2("aman",78)
st2=Student2("prafulla",88)
st1.result()
st2.result()


# real life banking
class Account:
    def __init__(self,n):
        self.name=n
        self.bal=0
    def deposit(self,x):
        self.bal+=x
    def show(self):
        print(self.name,self.bal)

ac=Account("prafulla")
ac.deposit(10000)
ac.show()


# real life shopping
class Product:
    def __init__(self,n,p):
        self.name=n
        self.price=p

class Cart:
    def __init__(self):
        self.items=[]
    def add(self,p):
        self.items.append(p)
    def show(self):
        for i in self.items:
            print(i.name,i.price)

p1=Product("mobile",12000)
p2=Product("laptop",55000)
ct=Cart()
ct.add(p1)
ct.add(p2)
ct.show()



# multiple real mixed
class A1:
    def f(self):
        print("A1")

class B1:
    def f(self):
        print("B1")

class C1(A1,B1):
    pass

C1().f()




# override error style
class P:
    def run(self):
        print("run")

class Q(P):
    pass

Q().run()



# silly cart
class Product:
    def __init__(self,n):
        self.n=n

class Cart:
    def __init__(self):
        self.a=[]
    def add(self,x):
        self.a.append(x)
    def show(self):
        for i in self.a:
            print(i.n)

ct=Cart()
ct.add(Product("apple"))
ct.add(Product("mango"))
ct.show()