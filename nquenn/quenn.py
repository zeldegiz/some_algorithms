def quenn(x,n):
  import math
  v=math.ceil(x/n)
  h=x-(v-1)*n
  r=[]
  i=x
  while(i%n!=1 and i-(n+1)>=1):
    i=i-(n+1)
    r.append(i)
  i=x
  while(i%n!=0 and i+(n+1)<=n*n):
    i=i+(n+1)
    r.append(i)
  i=x
  while(i%n!=1 and i+(n-1)<=n*n):
    i=i+(n-1)
    r.append(i)
  i=x
  while(i%n!=0 and i-(n-1)>=1):
    i=i-(n-1)
    r.append(i)
  for i in range((v-1)*n+1,v*n+1):
    r.append(i)
  for i in range(n):
    r.append(i*n+h)
  z=[]
  for i in r:
    if(i not in z):
      z.append(i)
  return z
