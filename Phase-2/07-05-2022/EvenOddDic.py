# Write a program to store no for odd keys and yes for even numbers and display them, ex:{1:no,2:yes,3:no,4:yes}

n = int(input())
l = []
d = {}
for i in range(1,n):
    x = int(input())
    l.append(x)

for i in l:
    if i%2==0:
        d[i] = "Yes"
    else:
        d[i] = "No"
print(d)
