# write a program to count duplicates in a list.

n = int(input())
li = []
for i in range(n):
  li.append(int(input())) 
print("Given list:", li)

notDup = []
for i in li:
    if li.count(i)>1:
        if notDup.count(i) == 0:
            notDup.append(i)
print(notDup)
    
