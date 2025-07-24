                            # RECURSION
# When a function calls itself repeatedly.

# Example 1 : // Recursive function
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
n=int(input("Enter a number : "))
show(n)

# Example 2 : //Recursion Factorial // n!=(n-1)!*n
def fact(a):
    if(a==1 or a==0):
        return 1
    return fact(a-1)*a
    #print(fact(a))
a=int(input("Enter a number : "))
print(fact(a))

# Practice Questions :
# Q.1) Write a recursive function to calculate the sum of n natural numbers.
def natural_num(b):
    if(b==0):
        return 0
    return natural_num(b-1)+b
b=int(input("Enter a number : "))
print(natural_num(b))

# Q.2) Write a recursive function to print all elements in a list.(Hint :use list & index as parameter)
def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits=["Mango","Apple","Banana","Litchi","Guava","Orange"]
#idx=int(input("Enter index no : "))
print_list(fruits) #print_list(fruits,idx)