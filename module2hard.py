stone1 = int(input('Введите число с камней первого поля: '))
stone2 = []
result = []


def check(a, b):    # Функция проверки на обратное повторение пар цифр
    for k in range(len(stone2)):
        if stone2[k] == [b, a]:
            return False
    return True


for i in range(1, stone1):  # Ищим кратные суммы цифр
    for j in range(1, stone1):
        if stone1 % (i + j) == 0 and i != j and check(i, j):
            stone2.append([i, j])
for i in range(len(stone2)):    # Перевод цифровых вложенных строк в одну стринговую
    for j in 0, 1:
        result += (str(stone2[i][j]))
print(*result)
