# List

# Example 1
"""marks=[95.4,98.2,87.5,89.4]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[3])

# Example 2
students=["Zahir",5,21,98.4,"West Bengal"]
print(students)
print(len(students))
print(type(students))
print(students[0])
students[0]="Rahul"
print(students)

# List Slicing

mark=[86,87,98,56,76,93]
print(mark[0:6])
print(mark[0:])
print(mark[:6])

# List Slicing (Negative Index)

A=[87,88,98,65,46]
print(A[-3:-1])

# List Methods

# Method 1 : list.append()
b=[3,6,2,8]
b.append(4)
print(b)

# Method 2 : list.sort() // Sorting in ascending order
list=[2,5,1,3]
list.sort()
print(list.sort())
print(list)

# list name.sort(reverse=True)  // Sorting in descending order
list=['a','e','s','m','r','y']
list.sort()
print(list.sort(reverse=True))
print(list)

# Method 3 : list name.reverse()  // Reverse the entire list
list=['a','e','s','m','r','y']
list.reverse()
print(list)

# Method 4 : list name.insert()  // Insert element at index
list=[2,5,6,3]
list.insert(2,8)
print(list)

# Method 5 : list name.remove()  // Removes first occurrence of element
list=[2,5,6,8,6]
list.remove(6)
print(list)

# Method 6 : list name.pop(index no)  // Remove element from particular index
list=[9,6,7,2,5]
list.pop(2)
print(list)

                                      # TUPLES IN PYTHON #

# A built-in data type that lets us create immutable sequences of values.
# We can use tuple as list but instead of using square bracket,we can use parenthesis.
# We can not insert,update and delete values in tuple.

A=(3,4,1,4)
print(type(A))

# Example 1 : Empty Tuple
A=()
print(type(A))
print(A)

# Example 2 : Single Tuple  // Here we have to use coma(,) for Single Tuple otherwise compiler doesn't understand whether it is int,string,float or tuple.
A=(1,)
print(type(A))
print(A[0]) 

# Example 3 : Multiple Tuple  // In Multiple Tuple coma(,) is optional.
A=(4,7,3,6)
print(A[0])
print(A[3])

# Tuple Slice

A=(4,8,6,2,5)
print(A[0:2])"""

# Tuple Methods : 

# Method 1 : tuple name.index(element)  // For finding the index no of the particular element
A=(4,8,6,2,5)
print(A.index(8))

# Method 2 : tuple name.count(element)  // For finding the number of uses of a particular element in tuple
A=(2,5,4,3,2,5,7,2)
print(A.count(2))