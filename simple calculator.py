a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = input("eoperation u want:? -,+,*,/,//,%,**")

if c == "-":
    print(a-b)
elif c == "//":
    print(a//b)
elif c == "%":
     print(a%b)
elif c == "**":
     print(a**b)
elif c =="+":
    print(a+b)
elif c == "*":
    print(a*b)
elif c == "/":
    if b == 0:
        print("undefined")
    else:
        print(a/b)
else:
    print("you have enter wrong operator")
