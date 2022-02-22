n = int(input())
ascii = 97
for i in range(1,n+1):
  for j in range(1,n+1):
    print(chr(ascii), end=" ")
    ascii+=1
  print("\n")

  
 '''
 OUTPUT ::
 4
a b c d 

e f g h 

i j k l 

m n o p 
'''
      
