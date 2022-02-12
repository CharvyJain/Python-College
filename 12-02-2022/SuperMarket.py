# Write a program to prepare supermarket bill.

fruits = 35
veggies = 40
flour = 100
milk = 50
drinks = 25

cname = input("Enter Customer Name:")
cpnum = int(input("Enter Customer Number:"))
fru = int(input("Enter the Kgs of Fruits:")) 
veg = int(input("Enter the Kgs of Vegetables:")) 
flo = int(input("Enter the Kgs of Flour:")) 
mil = int(input("Enter no. of packets of Milk:")) 
dri = int(input("Enter no. of cans of Drinks:"))

total = (fruits*fru) + (veggies*veg) + (flour*flo) + (mil*milk) + (dri*drinks)
if total>5000:
  dis = total*10/100
  tax = total*10/100
elif total>3000:
  dis = total*8/100
  tax = total*10/100
elif total>2000:
  dis = total*5/100
  tax = total*18/100
elif total>1000:
  dis = total*3/100
  tax = total*10/100
else:
  tax = 0
  dis = 0

amount = total - (dis+tax)  
print("Total Amount to be paid:", amount)  
