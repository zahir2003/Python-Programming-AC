                                       # DICTIONARY IN PYTHON

# Dictionaries are used to store data values in key:value pairs
# They are unordered,mutable(changeable) & don't allow duplicate keys

# Example 1 :

info={
    "key" : "value",
    "name" :"Zahir",
    "age" :21,
    "marks" : 93.6,
    "Is_adult":True,
    "subjects":["C","Java","Python","C++"],
    "topics":("dictionary","set"),
    12 : 93.6
}
print(type(info))
print(info["name"])
print(info["age"])
print(info["subjects"])
print(info[12])
info["name"]="Sk"
info["Surname"]="Mahiduzzaman"
print(info["age"],info["marks"])
print(info)

# Example 2 : Null Dictionary

null_dict={}
null_dict["Vill"]="Patna"
print(null_dict)

# Nested Dictionary :

student={
    "name":"Sk Mahiduzzaman",
    "Subjects":{
        "C++":93,
        "Java":94,
        "Python":95
    }
}
print(student["Subjects"]["C++"])
print(student)

# Dictionary Methods : 

# Method 1 : Dictionary name.keys()  // returns all keys

# Example 1 :
info={
    "key" : "value",
    "name" :"Zahir",
    "age" :21,
    "marks" : 93.6,
    "Is_adult":True,
    "subjects":["C","Java","Python","C++"],
    "topics":("dictionary","set"),
    12 : 93.6
}
print(info.keys())
print(len(info))
print(list(info.keys()))   # For typecasting , we can change it in several format like float,int etc.
print(len(list(info.keys())))

# Example 2 :
student={
    "name":"Sk Mahiduzzaman",
    "Subjects":{
        "C++":93,
        "Java":94,
        "Python":95
    }
}
print(student.keys())
print(len(student))
print(list(student.keys()))  # For typecasting
print(len(list(student.keys())))

# Method 2 : Dictionary name.values()  // returns all values

# Example 1 :
info={
    "key" : "value",
    "name" :"Zahir",
    "age" :21,
    "marks" : 93.6,
    "Is_adult":True,
    "subjects":["C","Java","Python","C++"],
    "topics":("dictionary","set"),
    12 : 93.6
}
print(info.values())
print(list(info.values()))  # For typecasting

# Example 2 :
student={
    "name":"Sk Mahiduzzaman",
    "Subjects":{
        "C++":93,
        "Java":94,
        "Python":95
    }
}
print(student.values())
print(list(student.values()))  # For typecasting

# Method 3 : Dictionary name.items()  // returns all(keys,values) pairs as tuple

# Example 1 :
info={
    "key" : "value",
    "name" :"Zahir",
    "age" :21,
    "marks" : 93.6,
    "Is_adult":True,
    "subjects":["C","Java","Python","C++"],
    "topics":("dictionary","set"),
    12 : 93.6
}
print(info.items())
print(list(info.items()))  # For typecasting
pair=list(info.items())
print(pair[0])

# Method 3 : Dictionary name.get("key")  // returns all key according to value

# Example 1 :
info={
    "key" : "value",
    "name" :"Zahir",
    "age" :21,
    "marks" : 93.6,
    "Is_adult":True,
    "subjects":["C","Java","Python","C++"],
    "topics":("dictionary","set"),
    12 : 93.6
}
print(info["name"]) # If we a put a key and thats not present in the dictionary then we will get an error.
print(info.get("name")) # But in here we will get None.

# Method 4 : Dictionary name.update(newDict)  // Inserts the specified items to the dictionary

# Example 1 :
student={
    "name":"Sk Mahiduzzaman",
    "Subjects":{
        "C++":93,
        "Java":94,
        "Python":95
    }
}
student.update({"city":"kolkata","age":21})
print(student)


                                    #  SET IN PYTHON

# Set is the collection of the unordered items.
# Each element in the set must be unique & set is mutable but its elements are immutable.

# Example 1 :
collection={1,2,3,2,4,"Hello","world","world"}  # Duplicate value is getting ignored and print one value of the duplicate value.
print(collection)
print(type(collection))
print(len(collection))  # len() is also ignored the duplicate value.

# Example 2 : Empty set{}
collection=set()
print(collection)
print(type(collection))
print(len(collection))

# Set methods : 

# Method 1 : setname.add(element) // adds an element. // We can't add list on set.

collection=set()
collection.add(1)
collection.add(2)
collection.add("Zahir")
collection.add(4.8)
collection.add(2)
collection.add((4,6,2))
print(collection)

# Method 2 : setname.remove(element) // remove the element

# Example 1 :
collection={1,2,3,2,4,"Hello","world","world"}
collection.remove("world")
print(collection)
print(len(collection))

# Example 2 :
collection=set()
collection.add(1)
collection.add(2)
collection.add("Zahir")
collection.add(4.8)
collection.add(2)
collection.add((4,6,2))
print(collection)
print(len(collection))
collection.remove((4,6,2))
print(collection)
print(len(collection))

# Method 3 : setname.clear()  // Empties the list

collection=set()
collection.add(1)
collection.add(2)
collection.add("Zahir")
collection.add(4.8)
collection.add(2)
collection.add((4,6,2))
print(collection)
print(len(collection))
collection.clear()
print(collection)
print(len(collection))

# Method 4 : setname.pop()  // Removes the random value.

collection={"Hello","world","Zahir",1,6.6,"student"}
print(collection.pop())
print(collection.pop())
print(collection.pop())
print(collection.pop())

# Methods 5 : setname.union(another setname)  // Combines both set values and returns new.

set1={1,2,3}
set2={2,3,4}
print(set1.union(set2))
print(set1)
print(set2)

# Method 6 : setname.intersection(another setname)  // combines common values & returns new.

set1={1,2,3}
set2={2,3,4}
print(set1.intersection(set2))
print(set1)
print(set2)