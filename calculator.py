a=int(input("enter a : "))
b= int(input("enter b : "))
operation=(input("Enter any operator(+,-,/,*): "))
if(operation == "+"):
    print(a+b)
if(operation == "-"):
    print(a-b)
if(operation == "*"):
    print(a*b)
if(operation == "/"):
    print(a/b)
else:
    print("INVALID OPERATOR")