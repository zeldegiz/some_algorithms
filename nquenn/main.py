import random
import quenn

n=int(input("Enter the size of the board: "))

while True:
  lst=[]
  a=[]
  for i in range(1,n*n+1):
    a.append(i)
  while(len(a)!=0):
    r=random.choice(a)
    lst.append(r)
    z=quenn.quenn(r,n)
    for j in z:
      if(j in a):
        a.remove(j)
  if(len(lst)==n):
    print(lst)
    






