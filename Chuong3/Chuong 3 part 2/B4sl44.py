a=float(input("a="))
b=float(input("b="))
c=input("Toan tu:")
if c=='+': print('',a,'+',b,'=',round(a+b,1),sep='')
elif c=='-': print('',a,'-',b,'=',round(a-b,1),sep='')
elif c=='': print('',a,'',b,'=',round(a*b,1),sep='')
elif (c=='/') and (b!=0): print('',a,'/',b,'=',round(a/b,1),sep='')
elif (c=='/') and (b==0): print('Khong hop le')
d=input('Tiep tuc:')
while True:
    if d!='t' or d!='T': 
        continue
    else: 
        break