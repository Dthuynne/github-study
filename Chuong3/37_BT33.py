x=float(input("x="))
y=float(input("y="))
ch=str(input("Phep toan:"))
if y==0 and ch=="/":
    print("Khong hop le")
elif ch=="+":
    print(x,"+",y,"=",round(x+y,1), sep="")
elif ch=="-":
         print(x,"-",y,"=",round(x-y,1), sep="")
elif ch=="*":
        print(x,"*",y,"=",round(x*y,1), sep="")
elif ch=="/" and ch!=0:
     print(x,"/",y,"=",round(x/y,1), sep="")
else:
    print("Khong hop le")
# if y==0 and ch=="/":
#     print("Khong hop le")
    
    