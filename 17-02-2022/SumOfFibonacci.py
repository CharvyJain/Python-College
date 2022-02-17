# Write a program to print sum of Fibonaaci Series upto given range.

n = int(input("Enter Range:"))
a = -1
b = 1
sum = 0
for i in range (1, n+1):
  c = a+b
  sum = sum+c
  a = b
  b = c
print(sum)
