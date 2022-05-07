# Prepare dictionary for student with the fields sno,name,gender,group,result.

stu = {
    101: ["Charvy Jain","Female","MSCS","Pass"],
    102: ["Sita","Female","MPCS","Fail"],
    103: ["Aditya","Male","MECS","Pass"],
    104: ["Karthik","Male","CS","Pass"]
}

x = int(input("Enter Student's Number:"))
print("Name:", stu[x][0])
print("Gender:", stu[x][1])
print("Group:", stu[x][2])
print("Result:", stu[x][3])
