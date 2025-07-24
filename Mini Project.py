# 1) Guess the Number :

"""import random
target = random.randint(1,100)
while True:
    userChoice = input("Guess the target or Quit(Q): ")
    if(userChoice == "Q"):
        break
    
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess..!!")
        break
    elif(userChoice < target):
        print("Your number is too small..Take a bigger guess..!!")
    else:
        print("Your number is too big..Take a smaller guess..!!")
        
print("-----Game Over-----")"""


# 2) Random Password Generator :

import random
import string

pas_len =  12
charValues = string.ascii_letters + string.digits + string.punctuation

password=""
for i in range(pas_len):
    password += random.choice(charValues)
    
print("Your random password is :",password)

            # OR
            
# Using List Comprehension :

import random
import string

pass_len=8
CharValues = string.ascii_letters + string.digits + string.punctuation

res = "".join([random.choice(CharValues) for i in range(pass_len)])
print("Your random password is :",res)