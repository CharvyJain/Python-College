# Write a program for sum of factorial series.

n = int(input("Enter number:"))
sum = 0
for i in range(1, n+1):
  f = f*i
  sum = sum+f
print(sum)
   
