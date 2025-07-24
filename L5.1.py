                                         # LOOPS IN PYTHON

# Loops are used to repeat instructions.

# 1) While loop :
count=1
while count<=5:
    print("Hello",count)
    count += 1

print(count)

i=5
while i>=1:
    print("Hello",i)
    i -= 1
print("Loop ended")

# Practice Question :

# Q.1)Print numbers from 1 to 100
i=1
while i<=100:
    print(i)
    i += 1
print("\nProgram ended !!")

# Q.2)Print numbers from 100 to 1
j=100
while j>=1:
    print("Hii",j)
    j-=1
print("Program ended")

# Q.3)Print the multiplication table of a number n.
i=1
n=int(input("Enter a number : "))
while i<=10 :
    print(n*i)
    i+=1
print("End")

# Q.4)Print the elements of the following lists using a list:[1,4,9,16,25,36,49,64,81,100],["Ironman","Thor","Spiderman"]
nums=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx < len(nums):
    print(nums[idx])
    idx+=1
print("End !!") 

heros=["Ironman","Thor","Spiderman"]
idx=0
while idx < len(heros):
    print(heros[idx])
    idx+=1

# Q.5)Search for a number x in this tuple using loop:[1,4,9,16,25,36,49,64,81,100]
nums=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter a element that present in the list (1,4,9,16,25,36,49,64,81,100) : "))
i=0
while i<len(nums):
    if(nums[i]==x):
        print("Found at index :",i)
        break
    else:
        print("Finding..")
    i+=1
print("End of programming..!!")

# For Loops :

# For loops are used for sequential traversal.For traversing list,string,tuples etc.
# Example 1 :
nums=[1,4,7,3,6,4]
for val in nums:
    print(val)

# Example 2 :
veg=["Potato","Onion","Ladyfinger","Carrot"]
for eat in veg:
    print(eat)

# Example 3 :
tup=(2,4,2,1,6,4,9,6,5)
for num in tup:
    print(num)

# Example : 4
str="Sk Mahiduzzaman"
for char in str:
    print(char)

# Example : 5
nums=[1,4,7,3,6,4]
for val in nums:
    print(val)
else:
    print("Program end")

# Example : 6
str="Sk Mahiduzzaman"
for char in str:
    if(char=='u'):
        print("U found")
        break
    print(char)
else:
    print("Program end")

# Q.1)Print the elements of the following list using a loop:[1,4,9,16,25,36,49,64,81,100] (Using for loop)
list=[1,4,9,16,25,36,49,64,81,100]
for num in list:
    print(num)
else:
    print("Program end")

# Q.2)Search for a number x in this tuple using loop:[1,4,9,16,25,36,49,64,81,100] (Using for loop)
list=(1,4,9,16,25,36,49,64,81,100)
a=int(input("Enter a number present in the list (1,4,9,16,25,36,49,64,81,100) : "))
idx=0
for num in list:
    if(num==a):
        print("Element found at index :",idx)
        break
    idx+=1