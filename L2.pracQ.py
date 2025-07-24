# Question 1

a=input("Enter your first name : ")
b=input("Enter your last name : ")
print("Your first name length is :",len(a))

# Question 2

b="Rosella is made with the help of sugar and it is sweet and soft"
print("The occurrence of 's' in the string is :",b.count("s"))

# Question 3

a=int(input("Enter a number : "))
if(a%2==0):
    print("The number is even")
else:
    print("The number is odd")

# Question 4

a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
c=int(input("Enter third number : "))
if(a>b and a>c):
    print("A is greatest")
elif(b>a and b>c):
    print("B is greatest")
else:
    print("C is greatest")

# Question 5

a=int(input("Enter a number : "))
if(a%7==0):
    print("The number is multiple of 7")
else:
    print("The number is not multiple of 7")

# Question 6

a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
c=int(input("Enter a number : "))
d=int(input("Enter a number : "))
if(a>b and a>c and a>d):
    print("A is greatest")
elif(b>c and b>a and b>d):
    print("B is greatest")
elif(c>a and c>b and c>d):
    print("C is greatest")
else:
    print("D is greatest")