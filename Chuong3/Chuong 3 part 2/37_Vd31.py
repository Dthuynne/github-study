'''n=int(input("n="))
while n<=0 and n>=51:
    print("Khong hop le\nMoi nhap lai")
    n=int(input("n="))'''
n=int(input("n="))
while n<=0 or n>=51:
    print("Khong hop le\nMoi nhap lai")
    n=int(input("n="))