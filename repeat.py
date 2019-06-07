n1=int(input())
m=[]
s=[]
for i in range (n1):
  k=int(input())
  m.append(k)
for i in range(n1-1):
  for j in range(i+1,n1-1):
      if m[i]==m[j]:
        s.append(m[i])
s.sort()
print (s)
