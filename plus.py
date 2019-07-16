#sanjay
n=int(input())
a=list(map(int,input().split()[:a1]))
for i in range(len(a)):
    for j in range(len(a)):
        for k in range(len(a)):
            if((a[i]+a[j]==a[k])and(i<j<k)):
                print(a[i],a[j],a[k])
