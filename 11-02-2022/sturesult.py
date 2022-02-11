# Write program to generate student result.

sno = int(input("Enter Student Number:"))
sname = input("Enter Student Name:")
sgroup = input("Enter Student group:")
s1 = int(input("Enter marks of Maths:"))
s2 = int(input("Enter marks of Statistics:"))
s3 = int(input("Enter marks of Computer Science:"))
s4 = int(input("Enter marks of Hindi:"))
s5 = int(input("Enter marks of English:"))
s6 = int(input("Enter marks of CRT:"))
total = s1+s2+s3+s4+s5+s6
avg = total/6

if s1>=35 and s2>=35 and s3>=35 and s4>=35 and s5>=35 and s6>=35:
  print("Pass")
  if avg>91:
    print("Grade:O")
  elif avg>81:
    print("Grade:A")
  elif avg>71:
    print("Grade:B")
  elif avg>61:
    print("Grade:C")
  elif avg>51:
    print("Grade:D")
else:
  print("Fail")
