'''n=int(input(""))
while n>=0:
    s=1
    i=2
    while i<=n:
        s=s*i
        i=i+1
    print(s)
    n=int(input())'''
n=int(input(""))
for i in range(1,1000000000000000):
    s=1
    if n<0: break 
    for j in range(2,n+1,1):
        s=s*j
    print(s)
    n=int(input())
    