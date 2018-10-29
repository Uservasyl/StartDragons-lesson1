x = 25
n = int(input("Вгадайте, яке загадано число: \n"))
while True:
    if x == n:
        print ("Вітаю, загадане число - це {}".format(n))
        break
    if n < x:
        print("Загадане число є більшим")
    elif n > x:
        print("Загадане число є меншим")
    n = int(input("Спробуйте знову: \n"))
