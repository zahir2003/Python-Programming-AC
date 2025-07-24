# Concatenation

a="My name is "
b="Zahir"
print(a+b)
print(len(a))

#Indexing

a="I am Zahir"
b=a[3]
print(b)

# Slicing

a="Adamas University"
print(a[0:6])
print(a[7:17])
print(a[7:len(a)])
print(a[7:]) # 7 to End
print(a[:17]) # First to 17

# Slicing(Negative Index)

a="apple"
print(a[-5:-2])
print(a[-3:-1])

# String Method

# Method 1 : String.endswith()

a="I sm pursuing B.tech from Adamas University"
print(a.endswith("ity"))
print(a.endswith("ty"))
print(a.endswith("y"))
print(a.endswith("sit"))

# Method 2 : String.capitalize()

b="zahir"
print(b.capitalize())
print(b)

# Method 3 : String.replace("old","new")
# Example 1
a="Adamas University"
print(a.replace("a","o"))

# Example 2
b="Sk"
print(b.replace("Sk","Sk Mahiduzzaman"))

# Method 3 : String.find()
# Example 1
a="youtube"
print(a.find("u"))
print(a.find("q")) # If the input value is not present in the string then it's return -1 so, it's totally invalid

#Example 2
a="I am from Burdwan"
print(a.find("from"))

# Method 4 : String.count()

a="I am studying python from youtube"
print(a.count("u")) # Count the given input value from the string

# Nesting if  :

age=int(input("Enter your age : "))
if(age>=18):
    if(age>=80):
        print("Can not drive")
    else:
        print("Can drive")
else:
    print("Can not drive")