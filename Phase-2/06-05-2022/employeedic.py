# Prepare dictionary for employee with the fields empno,empname,empdesig,empdoj,empsal,city.

emp = {
    101: ["Charvy Jain","Developer","10-05-2005",50000,"Secunderabad"],
    102: ["Sita","Manager","09-06-2007",30000, "Hyderabad"],
    103: ["Aditya","Tester","30-01-2006",45000,"Chennai"],
    104: ["Karthik","Sales","06-12-2015",20000, "Kolkata"]
}

x = int(input("Enter Employee's Number:"))
print("Emp Name:", emp[x][0])
print("Emp Designation:", emp[x][1])
print("Emp DOJ:", emp[x][2])
print("Emp Salary:", emp[x][3])
print("City:", emp[x][4])

