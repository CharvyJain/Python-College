# Write a program to print reverse of elements.

list1 = []
n = int(input())
for i in range(n):
  x = int(input())
  list1.append(x)
print("Given List:",list1)
list2 = []
for i in range(n-1, -1, -1):
  list2.append(list1[i])
print("Reversed List:", list2)
