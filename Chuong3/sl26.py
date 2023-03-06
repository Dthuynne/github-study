a=int(input("yrsOfService = "))
b=int(input("salary = "))
c=int(input("bonus = "))
if a<5:
        if b<500:
          c=100
        else:
            c=200
else:
    c=700
print("Bonus amount: ",c)
        