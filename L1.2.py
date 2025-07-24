                                      # CONDITIONAL OPERATOR

# 1st Example

"""light=input("Light is : ")
if(light == "red"):
    print("Stop")
elif(light == "green"):
    print("Go")
elif(light == "yellow"):
    print("Look")
else:
    print("Light is broken")

# 2nd Example

marks=int(input("Marks : "))
if(marks>100):
    print("Please enter a valid marks!!")
elif(marks>=90 and marks<=100):
    print("A")
elif(marks>=80 and marks<90):
    print("B")
elif(marks>=70 and marks<80):
    print("C")
else:
    print("D")

# 3rd Example

A=int(input("A : "))
G=input("M/F : ")
if((A==1 or A==2)and G=="M"):
    print("Fee is 100")
elif((A==3 or A==4)and G=="F"):
    print("Fee is 200")
elif(A==5 and G=="M"):
    print("Fee is 300")
else:
    print("No fee will be required")

                                     # SINGLE LINE IF/TERNARY OPERATOR

# 1st Example

food=input("Food : ")
eat="Yes" if food=="cake" else "no"
print(eat)

# 2nd Example

food=input("food : ")
print("Sweet") if food=="cake" or food=="jalebi" else print("No Sweet")"""

                                      # CLEVER IF/TERNARY OPERATOR

# 1st Example

age=int(input("age: "))
vote=("Yes" , "No") [age < 18]
print(vote)

# 2nd Example

sal=float(input("Salary : "))
tax=sal*(0.2,0.1) [sal < 50000]
print(tax)