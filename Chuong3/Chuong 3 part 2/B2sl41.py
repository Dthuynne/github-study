<<<<<<< HEAD
n=int(input("n="))
s = True
if (n < 2):
    s = False
elif (n == 2):
    s = True
elif (n % 2 == 0):
    s = False
else:
    for i in range(3, n, 2):
        if (n % i == 0):
            s = False
if s == True:
    print(n,"la SNT")
else:
    print(n,"khong la SNT")
=======
n=int(input("n="))
flag = True
if (n < 2):
    flag = False
elif (n == 2):
    flag = True
elif (n % 2 == 0):
    flag = False
else:
    for i in range(3, n, 2):
        if (n % i == 0):
            flag = False
if flag == True:
    print(n,"là số nguyên tố")
else:
    print(n,"không phải là số nguyên tố")
>>>>>>> a6686becd1f7f7f4dfe82a5e483613462bd7894c
