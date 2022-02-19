# write a program to count prime upto given number.

def isprime(n):
  for i in range(2,n):
    if(n%i==0):
      return False
  return True
  
n = int(input("Enter number:"))
count = 0
for i in range(2,n+1):
    if isprime(i):
      count = count+1
print(count)
