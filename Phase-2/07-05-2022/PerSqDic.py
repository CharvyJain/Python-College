# Write a program to store yes for perfact square keys and no for other from 1 to 1000,ex:{1:yes,2:no,3:no,4:yes}

def is_perfect_square(n):
    x = n // 2
    y = set([x])
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in y: return False
        y.add(x)
    return True
    
n = int(input())
l = []
d = {}
for i in range(1,n):
    x = int(input())
    l.append(x)

for i in l:
    if is_perfect_square(i):
        d[i] = "Yes"
    else:
        d[i] = "No"
print(d)
