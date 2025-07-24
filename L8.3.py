# del keyword : Used to delete object properties or object itself.

# Example 1 :
"""class Student:
    def __init__(self,name):
        self.name=name
        
s1=Student("Zahir")
print(s1)
del s1
#print(s1)

# Example 2 :
class Student:
    def __init__(self,name1):
        self.name=name1
        
s2=Student("Zahir")
print(s2.name)
del s2.name1
print(s2.name1)


# Private(like) attributes & methods : (Conceptual Implementation in Python)
# Private attributes & methods are meant to be used only within the class and are not accessible from outside the class.

# Example 1 :
class Account:
    def __init__(self,acc_no,acc_pass):
        self.a=acc_no
        self.__b=acc_pass # Whenever we want to private the method or attribute just add the __ (double underscore) before the method or attribute and this private method or attribute are only accessible by inside the class not outside the class.
        
    def reset_pass(self):
        print(self.__b)
        
acc1=Account("12345","abcde")
print(acc1.a)
print(acc1.reset_pass())
#print(acc1.__b)

# Example 2 :
class Person:
    __name="Anonymous"
    
p1=Person()
#print(p1.__name)

# Example 3 :
class Person1:
    def __hello():
        print("Hello world")
        
p2=Person1()
#print(p2.__hello())

# Example 4 :
class Person3:
    def __hello1(self):
        print("Hello world")
        
    def welcome(self):
        self.__hello1()
        
p3=Person3()
print(p3.welcome())"""


                                           # INHERITANCE : 

# When one class(child/derived) derives the properties & methods of another class(parent/base class).

# Example 1 :
class Car:
    color="Black"
    @staticmethod
    def start():
        print("Car started..")
        
    @staticmethod
    def stop():
        print("Car stopped..")
        
class Toyotacar(Car):
    def __init__(self,name):
        self.name=name
        
c1=Toyotacar("Fortuner")
c2=Toyotacar("Suppra")

print(c1.name)
print(c2.name)
print(c2.color)
print(c1.start())
print(c2.stop())

# Types of Inheritance :

# 1) Single Inheritance : One single Base/Parent class and one single Child/Derived class.

# Example 1 :
class Car:
    color="Black"
    @staticmethod
    def start():
        print("Car started..")
        
    @staticmethod
    def stop():
        print("Car stopped..")
        
class Toyotacar(Car):
    def __init__(self,name):
        self.name=name
        
c1=Toyotacar("Fortuner")
c2=Toyotacar("Suppra")

print(c1.name)
print(c2.name)
print(c2.color)
print(c1.start())
print(c2.stop())


# 2) Multilevel Inheritance : Base class --> Child class --> Child class.  // 1st Child class is directly access the Base class.2nd Child class is directly access the 1st child class and indirectly access the base class.
 
# Example 1 :
class Car:
    @staticmethod
    def start():
        print("Car started..")
        
    @staticmethod
    def stop():
        print("Car stopped..")
        
class Toyotacar(Car):
    def __init__(self,brand):
       self.brand=brand
        
class Fortuner(Toyotacar):
    def __init__(self,type):
        self.type=type
        
c1=Fortuner("Diesel")
c1.start()
print(c1.type)
c2=Toyotacar("Suppra")
print(c2.brand)
c2.stop()


# 3) Multiple Inheritance : 2 or more than 2 Parent/Base class and one Child/Derived class.

# Example 1:
class A:
    varA = "Welcome to class A"
    
class B:
    varB = "Welcome to class B"
    
class C(A,B):
    varC="Welcome to class c"
    
c1=C()
print(c1.varC)
print(c1.varB)
print(c1.varA)
    
    
# Super Method : super() method is used to access methods of the parent class.

# Example 1 :
class Car:
    def __init__(self,type):
        self.type=type
        
    @staticmethod
    def start():
        print("Car started..")
        
    @staticmethod
    def stop():
        print("Car stopped..")
        
class Toyotacar(Car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
        super().start()
        
c1=Toyotacar("Fortuner","Diesel")
print(c1.name)
print(c1.type)
c1.stop()


# Class method : A class method is bound to the class & receives the class as an implicit first argument. 
# NOTE : static method can't access or modify class state & generally for utility.

# Example 1 :  // Using class method
class Person:
    name="Anonymous"
    
    @classmethod  # decorator
    def Cha_name(cls,name):
       cls.name=name
        
p1=Person()
p1.Cha_name("Sk Mahiduzzaman")
print(p1.name)
print(Person.name)

# Example 2 : // Normal technique
"""class Person:
    name="Anonymous"
    
    def Cha_name(self,name):
       # self.name=name
        Person.name=name
        
p1=Person()
p1.Cha_name("Sk Mahiduzzaman")
print(p1.name)
print(Person.name)

# Example 3 : // Normal technique
class Person:
    name="Anonymous"
    
    def Cha_name(self,name):
       self.__class__.name="Zahir"
        
p1=Person()
p1.Cha_name("Sk Mahiduzzaman")
print(p1.name)
print(Person.name)"""


# Property : We use @property decorator on any method in the class to use the method as a property.

# Example 1 : // Using Property decorator
class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"
        
stu1=Student(98,97,96)
print(stu1.percentage)

stu1.phy=86
print(stu1.phy)
print(stu1.percentage)

# Example 2 : // Using normal technique
class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        self.percentage=str((self.phy+self.chem+self.math)/3)+"%"
        
    def calcPercentage(self):
        self.percentage=str((self.phy+self.chem+self.math)/3)+"%"
        
stu1=Student(98,97,96)
print(stu1.percentage)

stu1.phy=86
print(stu1.phy)
stu1.calcPercentage()
print(stu1.percentage)