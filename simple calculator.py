a=int(input("Enter first operand: "))
b=int(input("Enter second operand: "))
c=input('''
Enter operator
+ for addition
- for subtraction
* for multiplication
/ for division
''')
if(c=='+'):
    print(a, "+", b, "=", a + b)
elif(c=='-'):
    print(a, "-", b, "=", a - b)
elif(c=='*'):
    print(a, "*", b, "=", a * b)
elif(c=='/'):
    print(a, "/", b, "=", a / b)
else:
    print("Invalid operator")