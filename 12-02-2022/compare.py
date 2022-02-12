a = int(input("Enter 1st NUmber:"))
b = int(input("Enter 2nd NUmber:"))
        
if a == b:
    print("Numbers are equal")
elif a >= b:
    print(a,"is greater than",b)
elif b >= a:
    print(a,"is smaller than",b)
else:
    print("Numbers are not equal")
