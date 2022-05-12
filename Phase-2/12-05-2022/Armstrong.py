# Write a program to print given number is Armstrong number or not using method.

def arm(n):
    num=n
    r=0
    while n>0:
        rem=n%10
        r=r+rem*rem*rem
        n=n//10
    if num==r:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")
n=int(input())
arm(n)
