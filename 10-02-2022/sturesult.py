# Write program to generate student result whether pass or fail.

sno = int(input("Enter Student Number:"))
sname = input("Enter Student Name:")
sgroup = input("Enter Student group:")
s1 = int(input("Enter marks of Maths:"))
s2 = int(input("Enter marks of Statistics:"))
s3 = int(input("Enter marks of Computer Science:"))
s4 = int(input("Enter marks of Hindi:"))
s5 = int(input("Enter marks of English:"))
s6 = int(input("Enter marks of CRT:"))

if s1>=35 and s2>=35 and s3>=35 and s4>=35 and s5>=35 and s6>=35:
    print("Pass")
else:
    print("Fail")
