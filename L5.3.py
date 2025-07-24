# range()
# Range functions returns a sequence of numbers,starting from 0 by default,and increments by 1(by default),and stops before a specified number.
# range(start?,stop,step?)   // (?)=optional

# Example 1 :
seq=range(10)
for i in seq:
    print(i)
            #Or
for i in range(10):
    print(i)

# Example 2 :
for i in range(10):  # range(stop)
    print(i)

for i in range(2,10): #range(start,stop)
    print(i)

for i in range(2,10,2): #range(start,stop,step)
    print(i)

# Example 3 :

# Find all the even number between 1-100 using range function.
for i in range(2,101,2):
    print(i)

# Find all the odd number between 1-100 using range function.
for i in range(1,100,2):
    print(i)

# PRACTICE QUESTIONS :

# Q.1) Print numbers from 1 to 100.
for i in range(1,101):
    print(i)

# Q.2) Print numbers from 100 to 1.
for i in range(100,0,-1):
    print(i)

#  Q.3) Print the multiplication table of a number n.
n=int(input("Enter a number :"))
for i in range(11):
    print(n*i)