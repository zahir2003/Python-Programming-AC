                                   # FILE I/O IN PYTHON

# Python can be used to perform operations on a file.(Read & write data)

# Types of all files :
# 1) Text Files : .txt,.docx,.log etc.
# 2) Binary Files : .mp4,.mov,.png,.jpeg etc.

# OPEN,READ & CLOSE FILE :

# We have to open a file before reading or writing.
# f=open("file_name","mode")  //mode : 1) r : read mode, 2) w : write mode

# Reading a file :

# Example 1 :
f=open("demo.txt","r")
data=f.read() # reads entire file.
#data=f.read(5) # It's read only the first 5 character.
data1=f.readline() # reads one line at a time.
data2=f.readline()
data3=f.readline()
print(data)
print(data1)
print(data2)
print(data3)
print(type(data))
f.close()

# Writing to a file :

# Example 1 : // w : write.
f=open("demo.txt","w") # w : overwrites the entire file.
f.write("I want to learn javascript tomorrow.123")
f.close()

# Example 2 : // a : append.
f=open("demo.txt","a") # a : adds to the file.
f.write("\nThen i will move for css")
f.close()

# Example 3 : When we haven't such any file in folder that mention in open() but if we use "w" or "a" .It,s automatically creates a file with that particular name which is present in the open().
f=open("sample.txt","w")
f.close()

f=open("Sample2.txt","a")
f.close()

# Example 4 : // r+ : read & write both.
f=open("demo.txt","r+") # r+ is used for both read and write and here whatever the string we write that overwrites and it started at the beginning of the string.
f.write("abc")
f.close()

# Example 5 : // w+ : read & write both.
f=open("demo.txt","w+") # w+ is also used for both read and write but here previous data will be deleted and then whatever we write the new data will be stored.
print(f.read())
f.write("Abc")
f.close()

# Example 6: // a+ : read & write both.
f=open("demo.txt","a+") # a+ is also used for both read and write but here the data will not be deleted and will not be overwrites and the new data stored just after the previous data.
print(f.read())
f.write("Def")
f.close()

# r+ : read+overwrites (curser will be present at the starting of the string) ,no truncate.  // truncate=delete
# w+ : read+overwrites ,truncate.
# a+ : read+overwrites (curser will be present at the ending of the string) ,no truncate.

# With Syntax :
# When we are using "with" keyword we need not to close the file ,it 's automatically closed after perform some specific task.

# Example 1 :
with open("demo.txt","r") as f:
    data=f.read()
    print(data)

# Example 2 :
with open("demo.txt","w") as f:
    f.write("New data")

# Deleting a file :

# Using the os module.
# Module(like a code library) is a file written by another programmer that generally has a function we can use.

# Example 1 :
import os
os.remove("Sample2.txt")