import numpy as np

# Ввод размера квадратной матрицы
n = int(input("Введите размер квадратной матрицы n: "))

# Генерация матрицы
np.random.seed(42)
A = np.random.randint(0, 20, size=(n, n))
print("Исходная матрица A:")
print(A)

# Преобразование: для каждой строки меняем максимум с диагональным элементом
B = A.copy()  # работаем с копией, чтобы сохранить исходную при необходимости
for i in range(n):
    # Находим индекс максимального элемента в строке i
    max_idx = np.argmax(B[i, :])
    # Меняем местами B[i, i] и B[i, max_idx]
    B[i, i], B[i, max_idx] = B[i, max_idx], B[i, i]

print("\nПреобразованная матрица (максимум строки на диагонали):")
print(B)

# Главная диагональ преобразованной матрицы
diag = np.diag(B)
print("\nЭлементы главной диагонали после обмена:", diag)

# Способ 1: встроенная функция
median_builtin = np.median(diag)
print(f"Медиана диагонали (np.median): {median_builtin}")

# Способ 2: ручное вычисление
sorted_diag = np.sort(diag)
k = len(sorted_diag)
if k % 2 == 1:
    median_manual = sorted_diag[k // 2]
else:
    median_manual = (sorted_diag[k // 2 - 1] + sorted_diag[k // 2]) / 2
print(f"Медиана диагонали (ручной расчёт): {median_manual}")