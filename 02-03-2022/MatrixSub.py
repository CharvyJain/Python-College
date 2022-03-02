# Write program for suntraction of matrix.

r = int(input("Enter rows:"))
c = int(input("Enter columns:"))

A = []
for i in range(r):
    lis = []
    for j in range(c):
        lis.append(int(input()))
    A.append(lis)

for i in range(r):
	for j in range(c):
		print(A[i][j], end = " ")
	print()

r = int(input("Enter rows:"))
c = int(input("Enter columns:"))

B = []
for i in range(r):
    lis = []
    for j in range(c):
        lis.append(int(input()))
    B.append(lis)

for i in range(r):
	for j in range(c):
		print(B[i][j], end = " ")
	print()

result = [[0,0],
         [0,0,]]

for i in range(len(A)):
   for j in range(len(B[0])):
       result[i][j] = A[i][j] - B[i][j]

for r in result:
   print(r)
