import csv

with open('StudentsPerformance.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)

print(f"Всего записей: {len(data)}")
print("Пример первой записи:", data[0])

# Преобразуем writing score в целое число для всех записей
for row in data:
    row['writing score'] = int(row['writing score'])

# Фильтрация
high_writing = list(filter(lambda row: row['writing score'] > 90, data))
count_high_writing = len(high_writing)

print(f"Количество абитуриентов с writing score > 90: {count_high_writing}")

# Извлечение столбца race/ethnicity с помощью map
ethnicities = set(map(lambda row: row['race/ethnicity'], data))
count_ethnicities = len(ethnicities)

print(f"Уникальные этнические группы: {ethnicities}")
print(f"Количество разных этнических групп: {count_ethnicities}")