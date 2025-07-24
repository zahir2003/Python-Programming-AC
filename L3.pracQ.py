# Question 1 :
# WAP to ask the user to enter names of their 3 favorite movies & store them in a list

#Process 1 : insert()
list=[]
list1=input("Enter 1st movie name : ")
list2=input("Enter 2nd movie name : ")
list3=input("Enter 3rd movie name : ")
list.insert(0,list1)
list.insert(1,list2)
list.insert(2,list3)

print("Name of the movies are :",list)

           # or
# Process 2 : insert()
list=[]
list.insert(0,input("Enter 1st movie : "))
list.insert(1,input("Enter 2nd movie : "))
list.insert(2,input("Enter 3rd movie : "))
print("The movies are : ",list)

          # Or
# Process 1 : append()
list=[]
list1=input("Enter 1st movie name : ")
list.append(list1)
list2=input("Enter 2nd movie name : ")
list.append(list2)
list3=input("Enter 3rd movie name : ")
list.append(list3)
print("The movies are :",list)

         # Or
# Process 2 : append()
list=[]
list.append(input("Enter 1st movie name : "))
list.append(input("Enter 2nd movie name : "))
list.append(input("Enter 3rd movie name : "))
print("The movies are :",list)

# Question 2 :
# WAP to check if a list contains a palindrome of elements.(Hint:use copy() method)

list=[3,2,2,3]
list1=list.copy()
list1.reverse()
if(list1==list):
    print("Palindrome")
else:
    print("Not palindrome")

# Question 3 :
# WAP to count the number of student with the "A" grade in the following tuple : ["C","D","A","A","B","B","A"]

list=("C","D","A","A","B","B","A")
print(list.count("A"))

# Question 4 :
# Store the ["C","D","A","A","B","B","A"] values in the list & sort them from "A" to "D".

# Process 1 : For user input
list=[]
list.append(input("Enter the 1st character :"))
list.append(input("Enter the 2nd character :"))
list.append(input("Enter the 3rd character :"))
list.append(input("Enter the 4th character :"))
list.append(input("Enter the 5th character :"))
list.append(input("Enter the 6th character :"))
list.append(input("Enter the 7th character :"))
print("The characters are :",list)
list.sort()
print("The sorting character are ",list)

# Process 2 : For given the value
list=["C","D","A","A","B","B","A"]
print("The characters are :",list)
list.sort()
print("The sorting characters are :",list)