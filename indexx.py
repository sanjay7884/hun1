n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range (n):
  if(a[i]==i):
    b.append(str(a[i]))
if(len(b)==0):
  print(-1)
else:
  print(" ".join(b))
