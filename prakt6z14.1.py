n = int(input("Введите размер массива: "))
mas = []

print("Введите элементы массива:")
for i in range(n):
    element = int(input(f"Элемент {i+1}: "))
    mas.append(element)

print("\nИсходный массив:", mas)

min_index = mas.index(min(mas))
max_index = mas.index(max(mas))

print(f"Минимальный: mas[{min_index}] = {mas[min_index]}")
print(f"Максимальный: mas[{max_index}] = {mas[max_index]}")

mas[min_index], mas[max_index] = mas[max_index], mas[min_index]

print("После обмена min и max:", mas)