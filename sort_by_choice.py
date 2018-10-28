import random
n = int(input("Ввести довжину списку: "))
li = []
for x in range (0, n):
    li.append(random.randint(1, 100))
print(li)
i = 0
while i < n-1:
    k = 1
    for i in range(n):
        for k in range(n):
            if li[i] < li[k]:
                li[i], li[k] = li[k], li[i]
        k += 1
    i +=1
print(li)

