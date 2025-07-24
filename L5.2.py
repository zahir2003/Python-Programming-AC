                         # BREAK & CONTINUE

# Break : Used to terminate the loop when encountered.
i=0
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1
print("End of programming")

# Continue : Terminates execution in the current iteration & continues execution of the loop with the next iteration.

# Example 1 :
i=0
while i<=5:
    if(i==3):
        i += 1
        continue # skip
    print(i)
    i+=1
print("End of programming")

# Example 2 : For print the odd number
i=1
while i<=10:
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1
print("End of programming")

# Example 3 : For print the even number
i=1
while i<=10:
    if(i%2!=0):
        i+=1
        continue
    print(i)
    i+=1
print("End of programming")