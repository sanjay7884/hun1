#sanjay   


n1=int(input())
a=input().split()
for i in range(n1):
    if(i%2==0):
        if(int(a[i])%2==1):
            print(a[i],end=' ')
    else:
        if(int(a[i])%2==0):
            print(a[i],end=' ')
