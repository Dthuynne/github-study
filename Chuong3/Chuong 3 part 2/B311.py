a=0
b=0
for i in range(-100000000,100000000):
    n=int(input())
    if n>0:
        a=a+1
    elif n<0:
        b=b+1
    if n!=0: 
        continue
    elif n==0: 
        break 
print(a,'so duong') 
print(b,'so am')