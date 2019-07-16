#sanjay
n=int(input())
a=list(map(int,input().split()))
x=max(a)
for i in range(len(a)):
    for j in range(len(a)):
        if((a[i]+a[j]<x)):
            x1=a[i]
            x2=a[j]
            x=abs(x1+x2)
print(x1,x2)  
