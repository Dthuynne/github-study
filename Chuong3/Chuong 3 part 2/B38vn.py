'''a=str(input())
n=int(input())
i=1
while i>=1 and i<=n and n>=1 and n<=20:
    print(((a) + (' '))*(i), end=" ")
    print(" "*(n-i))
    i=i+1'''
a=str(input())
n=int(input())
i=1
if n>=1 and n<=20:
    for i in range(1,n+1):
        for j in range(1,1+i):
            print(a,end=" ")
        print("")
