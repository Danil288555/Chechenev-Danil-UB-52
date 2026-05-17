import numpy as np

# Ввод размеров матрицы
n = int(input("Введите количество строк n: "))
m = int(input("Введите количество столбцов m: "))

# Генерация матрицы целых чисел от 0 до 20
np.random.seed(42)  # для воспроизводимости
A = np.random.randint(0, 20, size=(n, m))
print("Исходная матрица A:")
print(A)

# Сортировка последней строки по возрастанию
A[-1, :] = np.sort(A[-1, :])
print("\nМатрица после сортировки последней строки:")
print(A)

# Последняя строка после сортировки
last_row = A[-1, :]
print("\nПоследняя строка:", last_row)

# Способ 1: встроенная функция np.median
median_builtin = np.median(last_row)
print(f"Медиана (np.median): {median_builtin}")

# Способ 2: ручное вычисление медианы
sorted_row = np.sort(last_row)  # строка уже отсортирована, но для общности
k = len(sorted_row)
if k % 2 == 1:
    median_manual = sorted_row[k // 2]
else:
    median_manual = (sorted_row[k // 2 - 1] + sorted_row[k // 2]) / 2
print(f"Медиана (ручной расчёт): {median_manual}")