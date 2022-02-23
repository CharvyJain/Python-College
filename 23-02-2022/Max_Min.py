# write a program to find maximum and minimum from list

list1 = []
n = int(input())
for i in range(n):
  x = int(input())
  list1.append(x)
print("Given List:",list1)
max = list1[0]
for i in range(1,n):
  if max<list1[i]:
    max = list1[i]
min = list1[0]
for i in range(1,n):
  if min>list1[i]:
    min = list1[i]
print("Maximum:", max)
print("Minimum:", min)
