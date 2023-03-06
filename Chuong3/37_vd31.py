a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
max=a
min=b
if max<b: max=b
if max<c: max=c
if min>c: mim=c
if min>a: min=a
print("SLN=",max,sep="")
print("SBN=",min,sep="")