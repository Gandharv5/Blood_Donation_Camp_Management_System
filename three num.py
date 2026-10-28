#biggest of three num

a=int(input("Enter the num1"))
b=int(input("Enter the num2"))
c=int(input("Enter the num3"))

if(a>b and a>c):
    print("a is biggest:")
elif(b>a and b>c):
    print("b is biggest:")
elif(c>a and c>b):
    print("c is biggest:")
else:
    print("they are equals:")
