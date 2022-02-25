# write a program to remove all zero from given llist adn count the non zero number.

n = int(input())
list1 = []
for i in range(n):
  x = int(input())
  list1.append(x)
print("Given List:",list1)
list2 = []
c=0
for i in list1:
  if i != 0:
    list2.append(i)
    c = c+1
print(list2)
print("Count:",c)
