#!/usr/bin/python3
import random
li = []
n = int(input("Ввести довжину списку: "))
for x in range (0, n):
    li.append(random.randint(1, 100))
print(li)
i = 1
while i < n:
    for j in range(n-i):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]
    i += 1
print(li)
