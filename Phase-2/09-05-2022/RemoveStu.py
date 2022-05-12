# Write a program to remove student details in dictionary.


stu = {
    101: ["Charvy Jain","Female","MSCS","Pass"],
    102: ["Sita","Female","MPCS","Fail"],
    103: ["Aditya","Male","MECS","Pass"],
    104: ["Karthik","Male","CS","Pass"]
}

x = int(input("Enter Student's Number to delete:"))
stu.pop(x)
print(stu)
