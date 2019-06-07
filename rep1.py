n1=int(input())
n2=input().split()
m=[]
n=''
for i in n2:
    if n2.count(i)>1 and i not in m:
        m.append(i)
if len(m)>0:
    for i in range(len(m)-1):
        n+=m[i]+" "
    print(n+m[-1])
else:
    print("unique")
