#sanjay
n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)):
    for j in range(len(a)):
        if((a[i]+a[j]==0)):
           print(a[i],a[j])
    break
