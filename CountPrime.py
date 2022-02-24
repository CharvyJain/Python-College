# write a program to find count of prime numbers in given list.

n = int(input())
list1 = []
for i in range(n):
  x = int(input())
  list1.append(x)
print("Given List:",list1)

def isprime(num1):
    for i in range(2,num1):
        if num1%i ==0:
          return False
    return True    

c=0
for num in list1:
    if isprime(num):
        c=c+1
print(c)

        
