a=int(input("M1="))
b=int(input("M2="))
c=int(input("M3="))
S=int(input("S="))
if S<=100:
    print("Phai tra=",S*a,sep="")
if S>100 and S<=150:
    print("Phai tra=",a*100+(S-100)*b,sep="")
if S>=151:
    print("Phai tra=",a*100+50*b+(S-100-50)*c,sep="")