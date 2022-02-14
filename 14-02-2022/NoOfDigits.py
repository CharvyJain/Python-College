# Find number of digits in a given number

n = int(input("Enter Number:"))
count = 0
while n > 0:
     rem = n%10
     count+=1
     n = n//10
print(count)
     
