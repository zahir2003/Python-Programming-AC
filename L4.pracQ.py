# Question 1 :

# Store following word meanings in a python dictionary:
# table:"a piece of furniture","list of facts & figure"
# cat:"a small animal"

A={
    "table":["a piece of furniture","list of facts & figure"],
    # or "table":("a piece of furniture","list of facts & figure"),
    "cat":"a small animal"
}
print(A)
print(len(A))
print(type(A))

# Question 2 :

# You are given a list of subjects for students.Assume one classroom is required for 1 subject.How many classrooms are needed by all students.
# "python","java","C++","python","javascript","java","python","java","C++","C".

Subjects={"python","java","C++","python","javascript","java","python","java","C++","C"}
print(len(Subjects))

# Question 3 :

# WAP to enter marks of 3 subjects from the user and store them in a dictionary.Start with an empty dictionary & add one by one.Use subject name & marks as value.

Students={

}
a=input("Enter 1st subject name : ")
b=float(input("Enter 1st subject marks : "))
c=input("Enter 2nd subject name : ")
d=float(input("Enter 2nd subject marks : "))
e=input("Enter 3rd subject name : ")
f=float(input("Enter 3rd subject marks : "))
Students.update({a:b})
Students.update({c:d})
Students.update({e:f})
print(Students)

# Question 4 :

# Figure out a way to store 9 & 9.0 as separate values in the set.(You can take help of built-in data types)

A=set()
A.add(9)
A.add("9.0")
print(A)

# or
A=set()
A.add(("int",9))
A.add(("float",9.0))
print(A)