                                         # PASS STATEMENT :
# pass is a null statement that does nothing.It is based as a placeholder for future code.

# Example :
for i in range(5):
    pass
if i>5:
    pass

print("Python")

# Practice Questions :

# Q.1) WAP to find the sum of first n natural numbers.(Using while)
a=int(input("Enter a number : "))
sum=0
i=1
while i <= a:
    sum+=i
    i+=1
print("The sum of first",a,"natural number is : ",sum)

               # OR (for loop)
b=int (input("Enter a number : "))
sum=0
for i in range(1,b+1):
    sum+=i
print("The sum of first",b,"natural number is : ",sum)

# Q.2)WAP to find the factorial of first n natural numbers.(Using for)
a=int(input("Enter a number : "))
fact=1
i=1
while i <= a:
    fact*=i
    i+=1
print("The factorial is : ",fact)

                      #OR (for loop)
a=int(input("Enter a number : "))
fact=1
for i in range(1,a+1):
    fact*=i
print("The factorial of this number is :",fact)