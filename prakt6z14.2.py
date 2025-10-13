mas = []

print("Введите 10 целых чисел:")
for i in range(10):
    num = int(input(f"Число {i+1}: "))
    mas.append(num)

print("\nИсходный массив:", mas)

sum_mas = sum(mas)
avg = sum_mas / len(mas)

print(f"Сумма элементов: {sum_mas}")
print(f"Среднее арифметическое: {avg}")

for i in range(len(mas)):
    if mas[i] > avg:
        mas[i] = 1

print("Массив после замены:", mas)