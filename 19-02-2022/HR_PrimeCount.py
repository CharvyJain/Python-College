# https://www.hackerrank.com/contests/supercoder-or-pseudocoder/challenges/q-2

def myprime(n):
  for i in range(2,n):
    if n%i==0:
      return False
    return True
  
t = int(input())
for i in range(t):
  n = input().split(' ')
  s = int(n[0])
  e = int(n[1])
  c=0
  for i in range(s+1, e):
    if myprime(i):
      c=c+1
  print(c)
