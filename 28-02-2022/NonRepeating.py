# write a program to find the odd occurences in a given list

n = int(input())
list1 = []
for i in range(n):
  x = int(input())
  list1.append(x)
print("Given List:",list1)

l  = []
for i in list1:
    if list1.count(i)==1:
        l.append(i)
print(l)
