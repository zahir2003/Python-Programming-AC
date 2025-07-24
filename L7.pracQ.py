# Practice Questions :

# Q.1) Create a new file "practice.txt" using python.Add the following data in it:
# 1) Hi everyone
#    we are learning File I/O
#    using Java.
# 2) I like programming in Java.

"""f=open("practice.txt","w")
f.write("Hi everyone\nwe are learning File I/O\nusing Java.")
f.write("\nI like programming in Java.")
f.close()


# Q.2) WAF that replaces all occurrences of "Java" with "Python" in above file.
def Replace():
    with open("practice.txt","r") as f:
        data=f.read()
    new_data=data.replace("Java","Python")
    print(new_data)

    with open("practice.txt","w") as f:
        f.write(new_data)
Replace()


# Q.3) Search if the word "learning" exists in the file or not.

def check_word():
    word="learning"
    with open("practice.txt","r") as f:
        data=f.read()
        if(word in data):
            print("Found")
        else:
            print("Not found")
check_word()


# Q.4) WAF to find in which line of the file does the word "programming" occur first.
#      Print -1 if word not found.

def check_line():
    word="programming"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1
    return -1
print(check_line())"""


# Q.5) From a file containing numbers separated by comma,print the count of even numbers.

count=0
with open("Practice2.txt","r") as f:
    data=f.read()
    nums=data.split(",") # split() is used for splitting the string.
    for val in nums:
        if(int(val)%2==0):
            count+=1
print(count)