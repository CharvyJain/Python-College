# Write a program to print sum of even and odd numbers.

n = int(input("Enter Range:"))
eSum = 0
oSum = 0
for i in range(1, n+1):
    if i%2 == 0:
        eSum = eSum+i
    else:
        oSum = oSum+i
print("Sum of Even numbers upto",n,":",eSum)
print("Sum of Odd numbers upto",n,":",oSum)
        
