print("Для виходу натисніть число - 0")
while True:
    n = int(input("Введіть число: "))
    if n == 0:
        break
    if n % 2 == 0:
        print("Введене число парне")
    elif n % 2 == 1:
        print("Введене число непарне")
