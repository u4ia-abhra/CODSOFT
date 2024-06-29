import random
import string

n=int(input("Enter the length of the password: "))
password=[]
l=string.ascii_letters+string.digits+string.punctuation #Creating a choice of characters
for i in range(n):
    c=random.choice(l)
    password.append(c)
print("Password = ","".join(password))