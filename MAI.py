multiplication = []
root = []
try:
    # Ввод количества критериев
    k_number = int(input("Введите колличество критериев: "))
    # Создание матрицы с единичной диагональю и ввод значений под диагональю матрицы
    matrex = [[0 for i in range(k_number)] for j in range(k_number)]
    for i in range(k_number):
        for j in range(k_number):
            if i == j:
                matrex[i][j] = 1
            elif i - j > -1:
                matrex[i][j] = int(
                    input('Введите данные попарного сравнения критериев ' + str(j + 1) + " и " + str(i + 1)
                          + " : "))
                if (matrex[i][j] < 1 or matrex[i][j] > 9):
                    quit("Ошибка! Шкала сравнения включает в себя числа от 1 до 9! Перезапустите программу!")
                matrex[j][i] = matrex[i][j]

    count = 1
    hz = 0
    hz2 = 1
    root_summ = 0
    for g in range(k_number):
        for i in range(k_number):
            if i < hz2:
                count = count * matrex[hz][i]
            else:
                count = count * (1 / matrex[hz][i])  # Заполнение над диагональю матрицы зеркально числами 1/aij
        multiplication.append(count)  # Произведения всех чисел одной строки
        root.append(pow(multiplication[g], 1 / k_number))  # Корни произведений всех чисел одной строки
        root_summ += root[g]  # Сумма корней произведений всех чисел одной строки
        count = 1
        hz += 1
        hz2 += 1
    for i in range(k_number):  # Вывод весовых коэффициентов для всех критериев
        print("Весовой коэффициент для " + str(i + 1) + "-го критерия: " + str(round((root[i] / root_summ), 2)))
except ValueError:
    quit("Ошибка! Введено не число! Перезапустите программу!")
