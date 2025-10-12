# 1 Дан одномерный массив, состоящий из N вещественных элементов. Ввести массив с клавиатуры. 
# Найти и вывести минимальный по модулю элемент. Вывести массив на экран в обратном порядке.


N = int(input("Введите количество элементов массива: "))

mas = []

print("Введите элементы массива:")
for i in range(N):
    element = float(input(f"Элемент {i+1}: "))
    mas.append(element)

min_abs = abs(mas[0])  
min_element = mas[0]

for element in mas:
    if abs(element) < min_abs:
        min_abs = abs(element)
        min_element = element

print("\nИсходный массив:", mas)
print("Минимальный по модулю элемент:", min_element)
print("Массив в обратном порядке:", mas[::-1])