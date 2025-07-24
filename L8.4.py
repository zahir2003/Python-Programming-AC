# POLYMORPHISM : Operator Overloading

# When the same operator is allowed to have different meaning according to the context.

# Example 1 :
print(1+2)  #3
print(type(1))
print("Sk"+"Mahiduzzaman") # concatenate
print(type("Sk"))
print([1,2,3]+[4,5,6]) # merge
print(type([1,2,3]))

# Example 2 :
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
        
num=Complex(1,4)
num.showNumber()
num2=Complex(8,5)
num2.showNumber()
print("Thank you..")

# Operators & Dunder functions :

# 1) a+b  // addition  a.__add__(b) :

# Example 1 : # Using Normal function
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
        
    def add(self,num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)
        
num=Complex(1,4)
num.showNumber()
num2=Complex(8,5)
num2.showNumber()
num3=num.add(num2)
#num3=num+num2
num3.showNumber()
print("Thank you..")

# Example 2 : # Using Dunder function
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
        
    def __add__(self,num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)
        
num=Complex(1,4)
num.showNumber()
num2=Complex(8,5)
num2.showNumber()
#num3=num.add(num2)
num3=num+num2
num3.showNumber()
print("Thank you..")

# 2) a-b // substraction  a.__sub__(b) :

# Example 1 : # Using Dunder function
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
        
    def __sub__(self,num2):
        newReal=self.real-num2.real
        newImg=self.img-num2.img
        return Complex(newReal,newImg)
        
num=Complex(1,4)
num.showNumber()
num2=Complex(8,5)
num2.showNumber()
#num3=num.add(num2)
num3=num-num2
num3.showNumber()
print("Thank you..")

# 3) a*b // multiplication  a.__mul__(b)
# 4) a/b  // division  a.__truediv__(b)
# 5) a%b // modulo division  a.__mod__(b)


# Practice Questions : 

# Q.1) (i) Define a circle class to create a circle with radius r using the constructoer.(ii) Define an Area() method of the class which calculates the area of the circle. (iii) Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

class Circle:
    def __init__(self,radius):
        self.radius=radius
        
    def Area(self):
        return 3.14*self.radius**2
    
    def Perimeter(self):
        return 2*3.14*self.radius
    
c=Circle(12)
print("Area is :",c.Area())
print("Perimeter is :",c.Perimeter())
print("Completed")

# Q.2) (i) Define a Employee class with attributes role,department & salary.This class also has showDwtails() method. (ii) Create an Engineer class with that inherits properties from Employee & has additional attributes : name & age.

class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary
        
    def showDetails(self):
        print("Role is :",self.role)
        print("Department is :",self.department)
        print("Salary is :",self.salary)
        
class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Software Engineer","Development",90000)
        
    def show(self):
        print("Name is :",self.name)
        print("Age is :",self.age)
        
e=Engineer("Sk Mahiduzzaman",21)
e.show()
e.showDetails()

# Q.3) Create a class called Order which stores item & its price. Use Dunder function __gt__() to convey that : order1 > order2 if price of order1 > price of order2.

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
        
    def __gt__(self,odr):
        return self.price > odr.price
    
o1=Order("Chips",20)
o2=Order("Tea",15)
print(o1 > o2) # True