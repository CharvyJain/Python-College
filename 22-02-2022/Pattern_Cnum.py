n = int(input())
for i in range(1, n+1):
   for j in range(1, i + 1):
     print(j, end = "")
   print()
  
    # Loop to print the lower half 
    # diamond pattern 
for i in range(n+1,0,-1):
    for j in range(1,i-1):
       print(j, end = "")
    print()
    
   '''
   OUTPUT ::
   
    6 
1
12
123
1234
12345
123456
12345
1234
123
12
1

   '''
