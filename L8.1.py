                                # OBJECT ORIENTED PROGRAMMING SYSTEM


# OOP in Python :

# To map with real world scenarios,we started using objects in code.This is called object oriented programming.


# Class & Object in Python :

# Class is a blueprint for creating objects.

# Example :
class Student:
    name="Karan"
s1=Student()
print(s1.name)

s2=Student()
print(s2.name)

# Example 2:
class Car:
    color="Black"
    brand="Toyota"
    model="Fortuner"
c1=Car()
print(c1.color)
print(c1.brand)
print(c1.model)


                                    # __init__Function :


# Constructor :

# All classes have a function called __init__(),which always executed when the object is being initiated.

# Example 1 :
class Student:
    name="Karan"
    def __init__(self):
        print(self)
        print("adding new students in Database..")

s3=Student()
print(s3)

# Example 2 :
class Student:
    # default constructor
    def __init__(self):
        pass

    # parameterized constructor
    def __init__(self,fname,marks): # The self parameter is a reference to the current instance of the class,and is used to access variables that belongs to the class.
        self.name=fname
        self.marks=marks
        print("Adding new students information in the database..")

s1=Student("Zahir",95)
print(s1.name)
print(s1.marks)

s2=Student("Rahul",90)
print(s2.name,s2.marks)


# Class & Instance Attributes :

# Example 1 :
class Student:
    college_name="Adamas University"
    def __init__(self,fname,marks):
        self.name=fname
        self.marks=marks
        print("Adding new students information in the database..")

s1=Student("Zahir",95)
print(s1.name)
print(s1.marks)

s2=Student("Rahul",90)
print(s2.name,s2.marks)
print(s2.college_name) # We can write instance attribute as class.attribute or object.attribute
print(Student.college_name)

# Example 2 :
class Student:
    college_name="Adamas University"
    name="Anonymous"  # Class attribute
    def __init__(self,name,marks):
        self.name=name    # Object attribute. Object attribute > Class attribute
        self.marks=marks
        print("Adding new students information in the database..")

s1=Student("Zahir",95)
print(s1.name)