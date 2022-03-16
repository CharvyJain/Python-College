# write a program to remove duplicates from given list. 

list1=input()

l=list(list1)

res=[]

for i in l:

    if i not in res:

        res.append(i)

print(res)
