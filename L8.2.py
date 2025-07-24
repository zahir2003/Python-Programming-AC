 # METHODS :
                    
# Methods are functions that belongs to the objects.

# Example 1 :
"""class Student:
    college_name="Adamas University"
    name="Anonymous"  # Class attribute
    def __init__(self,name,marks):
        self.name=name  
        self.marks=marks
    
    def welcome(self): # Methods
        print("Welcome Students ,",self.name)
        
    def get_marks(self): # Methods
        #return self.marks
        print(self.marks)
        
s1=Student("Zahir",95)
#print(s1.name)
s1.welcome() 
#print(s1.get_marks())
s1.get_marks()

# Practice Question :

# Q.1) Create student class that takes name & marks of 3 subjects as arguments in constructor.Then create a method to print their average.
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Hii",self.name,"your average score is :",sum/3)
        
s1 = Student("Tony Stark",[98,96,97])
s1.get_avg()
s1.name="Ironman"
s1.get_avg()"""


# Static Methods

# Methods that don't use the self parameter(work at class level).

# Example 1 :
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    @staticmethod  # decorator // decorators are used for to convert a normal method to static method .
    def hello():
        print("Hello everyone")
        
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Hii",self.name,"your average score is :",sum/3)
        
s1 = Student("Tony Stark",[98,96,97])
s1.hello()
s1.get_avg()


# IMPORTANT CONCEPTS IN OOP :

# 1) Abstraction : Hiding the implementation details of a class and only showing the essential fetaures to the user.

# Example 1 :
class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
        
    def start(self):
        self.clutch=True
        self.acc=True
        print("Car started...")
        
c1=Car()
c1.start()

# 2) Encapsulation : Wrapping data and functions into a single unit(object).

# Example 1 : 
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Hii",self.name,"your average score is :",sum/3)
        
s1 = Student("Tony Stark",[98,96,97])
s1.get_avg()


# Practice Question :

# Q.1) Create Account class with 2 attributes - balance & account no. Create methods for debit,credit & printing the balance.

class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
        
    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"is debited from your account")
       # print("Total balance :",self.get_bal())
        
    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"is credited to your account")
       # print("Total balance :",self.get_bal())
        
    def get_bal(self):
        #return self.balance
        print("Now your total balance is :",self.balance)
        
a1=Account(10000,1234)
a1.debit(3000)
a1.credit(4000)
a1.get_bal()
a1.credit(50000)
a1.debit(5000)
a1.get_bal()