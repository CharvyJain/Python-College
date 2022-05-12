# Write a program to retrieve email id with the name using dictionary.

n = int(input())
dic = {}
for i in range(n):
  x = input("Enter details:").split()
  dic[x[0]] = x[1]
while True:
   try:
      name = input("Enter the name:")
      if name in dic:
         print("Name:",name,"Email:",dic[name],sep=' ')
      else: print("Not Found")
   except:
       break
  
