money = int(input())
if money % 100 in [11, 12, 13, 14]:
    print(money, 'рублей')
elif money % 10 == 1:
    print(money, "рубль")
elif money % 10 in [2, 3, 4]:
    print(money, 'рубля')
else:
    print(money, 'рублей')
