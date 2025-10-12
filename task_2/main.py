import random

a = 0

rows = random.randint(4, 8)
colomns = random.randint(4, 8)

list = [-15, 4, -2, -7, 0, 3, 5, 12, 7]

matrix = []

for i in range(rows):
    rows_list = []
    for j in range(colomns):
        rows_list.append(random.choice(list))
    matrix.append(rows_list)
print(matrix)

print("Ваша матрица:")
for i in matrix:
    for j in i:
        print(f"{j:4}", end = " ")
    print()

for i in matrix:
    for j in i:
        if(j % 2 == 1):
            a += j
print(a)