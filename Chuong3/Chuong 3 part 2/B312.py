# n = int(input("Nhập số nguyên n: "))

# # Tạo một từ điển để mã hoá các chữ số
# makh = {
#     0: 'A',
#     1: 'B',
#     2: 'C',
#     3: 'D',
#     4: 'E',
#     5: 'F',
#     6: 'G',
#     7: 'H',
#     8: 'I',
#     9: 'J'
# }

# # Chuyển đổi các chữ số trong số nguyên n thành ký tự được mã hoá
# encoded_str = ''.join([makh[int(i)] for i in str(n)])

# # In ra giá trị được mã hoá
# print(encoded_str)
n = int(input())
m=""
if n==0:
    print("A")
while n>0 and n<=9999:
    i=n%10
    if i==0:
        m="A"+m
    elif i==1:
        m="B"+m
    elif i==2:
        m="C" + m
    elif i==3:
        m= "D" + m
    elif i==4:
        m= "E" + m
    elif i==5:
        m= "F" + m
    elif i==6:
        m= "G" + m
    elif i==7:
        m= "H" + m
    elif i==8:
        m= "K" + m
    elif i==9:
        m= "L" + m
    n //= 10
print(m)