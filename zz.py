#sanjay

n=int(input())
a=list(map(int,input().split()[:n]))
x=max(a)
x1,y=0,0
for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        if(abs(a[i]+a[j])<x):
            x1,y=a[i],a[j]
            x=abs(x1+y)
print(x1,y)
