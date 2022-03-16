 

 # write a program to find the lists of odd and even numbers from given list. 

  



 n = int(input()) 

 list1 = [] 

 for i in range(n): 

   x = int(input()) 

   list1.append(x) 

 print("Given List:",list1) 

  

 n=len(list1) 

 o=[] 

 e=[] 

 for i in list1: 

     if i%2==0: 

         e.append(i) 

     else: 

         o.append(i) 

 print(o, e)
