# write a program to count duplicates in a list.

n = int(input())
li = []
for i in range(n):
  li.append(int(input())) 
print("Given list:", li)

dup = []
for i in li:
    if i not in dup:
        dup.append(i)
print(dup)

dup.sort(reverse=True)
print(dup[2])
