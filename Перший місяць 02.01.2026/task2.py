import math
print("Noob calculator")
a = float(input("First number:  "))
b = float(input("Second number:  "))
x = input("Choose an action *,/,+,-:  ")

if x=="*":
    print(a*b)
elif x=="/":
    if b == 0:
        print("Wrong action")
    else:
            print(a/b)
elif x=="+":
    print(a+b)
elif x=="-":
    print(a-b)
else:
    print("something went wrong")