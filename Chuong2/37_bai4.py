import  math 
a=float(input("a= "))
b=float(input("b= "))
c=float(input("c= "))
s=((a+b+c)/2)
print("Dien tich=", math.sqrt(s*(s-a)*(s-b)*(s-c)),sep="")