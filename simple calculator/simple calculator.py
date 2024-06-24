# Design a simple calculator with basic arithmetic operations.
# Prompt the user to input two numbers and an operation choice.
# Perform the calculation and display the result.
a = eval(input("Enter 1st operand: "))
b = eval(input("Enter 2nd operand: "))
ch = input('''Enter 
+ for addition,
- for subtraction, 
* for multiplication,
/ for division:
''')
if (ch=="+"):
    print(a, "+", b, "=", a + b)
elif (ch=="-"):
    print(a, "-", b, "=", a - b)
elif (ch=="*"):
    print(a, "*", b, "=", a * b)
elif (ch=="/"):
    print(a, "/", b, "=", a / b)
else:
    print("Invalid Input")
