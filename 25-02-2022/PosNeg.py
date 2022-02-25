# write a program to print positive numbers first and negative numbers next.

n = int(input())
list1 = []
for i in range(n):
  x = int(input())
  list1.append(x)
print("Given List:",list1)

pos = []
neg = []
for i in list1:
  if i > 0:
    pos.append(i)
  else:
    neg.append(i)
print(pos,neg)
