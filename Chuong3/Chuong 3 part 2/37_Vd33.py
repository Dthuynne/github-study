# n=1
# while n<=9:
#     j=1
#     while j<=9:
#         if (n*j)<10 and j!=1:
#             print("",end=" ")
#         print(n*j,end=" ")
#         j=j+1
#     print('\n')
#     n=n+1
n=1
for n in range(1,10):
    j=1
    for j in range(1,10):
        if (n*j)<10 and j!=1:
            print("",end=" ")
        print(n*j, end=" ")
    print("\n")

