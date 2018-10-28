print("Натисніть 'у' для виходу")
while True:
    n = input("Введіть слово: \n")
    if n == 'y':
        break
    c = n[::-1]
    if c == n:
        print("Слово є поліндромом")
    else:
        print("Слово не є поліндромом")