import csv

data = []
with open('StudentsPerformance.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        row['math score'] = int(row['math score'])
        row['reading score'] = int(row['reading score'])
        row['writing score'] = int(row['writing score'])
        data.append(row)

print(f"Всего записей: {len(data)}")



# Фильтрация
filtered = filter(lambda row: row['gender'] == 'female' and row['parental level of education'] == "master's degree", data)
count = len(list(filtered))

print(f"Количество девочек с родителями-магистрами: {count}")



# Шаг 1: максимальный балл по математике
max_math = max(row['math score'] for row in data)

# Шаг 2: отфильтровать учеников с максимальным баллом
top_math_students = [row for row in data if row['math score'] == max_math]

# Шаг 3: средний балл по чтению
if top_math_students:
    avg_reading = sum(row['reading score'] for row in top_math_students) / len(top_math_students)
else:
    avg_reading = 0

# Шаг 4: округление
avg_reading_rounded = round(avg_reading, 3)

print(f"Максимальный балл по математике: {max_math}")
print(f"Количество учеников с таким баллом: {len(top_math_students)}")
print(f"Средний балл по чтению среди них: {avg_reading_rounded}")