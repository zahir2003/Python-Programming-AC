                  # FUNCTIONS IN PYTHON
# Block of statement that perform a specific task.

# Example 1 :
def calculate(a,b):
    sum=a+b
    print(sum)
   # return sum

calculate(12,34)
calculate(4,6)

# Example 2 :
def cal_sum(n,m):
    print(m+n)
   # return m+n
#sum=cal_sum(15,20)
cal_sum(15,20)
#print(sum)

# Average of 3 numbers :
def cal_avg(a,b,c):
    sum=(a+b+c)/3
    print(sum)

cal_avg(4,5,6)

# Example 2 :
def cal_sum(c,d):
    sum=c+d
    return sum
c=int(input("Enter a number : "))
d=int(input("Enter a number : "))
result=cal_sum(c,d)
print("The sum is :",result)


# 1)BUILT-IN FUNCTIONS :
# print() , len() , type() , range()

# 2)USER-DEFINED FUNCTIONS :
# cal_sum() , cal_avg() , calculation()

# Default Parameters : Assigning a default to parameter,which is used when no argument is passed.
# Example 1 : 
def cal_multi(a=10,b=3):
    print(a*b)
    return a*b

cal_multi()

# Example 2 :
def cal_mul(a,b=5): # Default value is always in the last.
#def cal_mul(a=2,b): // Occurs error.
    print(a*b)
    return a*b
cal_mul(3)

# Practice Questions :

# Q.1)WAF to print the length of a list.(list is the parameter)
cities=["Delhi","Mumbai","Kolkata","Pune","Chandigarh","Noida"]
heroes=["Ironman","Thor","Hulk","Spiderman"]

def print_len(a):
    print(len(a))

print_len(cities)
print_len(heroes)

# Q.2)WAF to print the elements of a list in a single line.(list is the parameter)
cities=["Delhi","Mumbai","Kolkata","Pune","Chandigarh","Noida"]

def print_list(b):
    for item in b:
        print(item,end=" ")

print_list(cities)

# Q.3) WAF to find the factorial of n.(n is the parameter)
def fact(n):
    sum=1
    for i in range(1,n+1):
        sum*=i
    return sum

n=int(input("\nEnter a number : "))
print("The factorial of",n,"is :",fact(n))

# Q.4) WAF to convert USD to INR.
def convert(d):
    r=d*83
    return r
d=int(input("Enter USD amount : "))
a=convert(d)
print(d,"USD =",a,"INR")

# Q.5) WAF to check a number even or odd.
def even_odd(n):
    if(n%2==0):
        print("The number is even")
    else:
        print("The number is odd")
    return n
n=int(input("Enter a number : "))
even_odd(n)