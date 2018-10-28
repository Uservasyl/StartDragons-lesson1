n = int(input("Введіть довжину списку: \n"))
a = 0
b = 1
li = []
while len(li) < n:
    c = a + b
    a = b
    b = c
    li.append(c)
print(li)
