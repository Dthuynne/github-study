t=float(input())
l=float(input())
h=float(input())
dtb=(t*2+l*3+h)/6
if dtb<3:
    print("Kem")
elif dtb>=3 and dtb<5:
    print("Yeu")
elif dtb>=5 and dtb<6:
    print("Trung binh")
elif dtb>=6 and dtb<7:
    print("Trung binh Kha")
elif dtb>=7 and dtb<8:
    print("Kha")
elif dtb>=8 and dtb<9:
    print("Gioi")
else:
    print("Xuat sac")