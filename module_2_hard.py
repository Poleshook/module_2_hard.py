import random
numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
z = random.choice(numbers)
print("Постоянно меняющееся число: ", z)
print("Шифр: ", end="")
for i in range(1, len(numbers) + 2):
    for j in range(1, len(numbers) + 2):
        if i >= j:
            continue
        if z % (i + j) == 0:
            print(i, end="")
            print(j, end="")