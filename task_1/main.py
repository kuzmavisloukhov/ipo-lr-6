#Kuzma Visloukhov

print("")

list = []

c = 0
a = int(input("Введите колличество элементов в списке: "))

for i in range(a):
    word = str(input(f"Введите {i + 1}-ый для заполнения в список: ")) 
    list.append(word.lower())

print(list)
print(len(list))
for i in list:
    for j in i:
        if (j == "a"):
            c += 1
print(c)
