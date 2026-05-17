import pandas as pd

# Загрузка данных
df = pd.read_csv('football.csv', encoding='utf-8')

# Первые 5 строк
print("head(5):\n", df.head())

# Последние 5 строк
print("\ntail(5):\n", df.tail())

# Информация о датафрейме
print("\ninfo():\n")
df.info()

# Основные статистики
print("\ndescribe():\n", df.describe())



# Средняя зарплата
mean_wage = df['Wage'].mean()
print(f"Средняя зарплата всех игроков: {mean_wage:.2f}")

# Фильтр: игроки с зарплатой выше среднего
high_wage = df[df['Wage'] > mean_wage]

# Средняя скорость SprintSpeed
mean_sprint = high_wage['SprintSpeed'].mean()
result_5 = round(mean_sprint, 2)

print(f"Средняя скорость (SprintSpeed) игроков с зарплатой выше среднего: {result_5}")


# Группа A
mean_reactions = df['Reactions'].mean()
max_penalties = df['Penalties'].max()

group_A = df[(df['Reactions'] > mean_reactions) & (df['Penalties'] == max_penalties)]
mean_age_A = group_A['Age'].mean()

print(f"Средняя реакция: {mean_reactions:.2f}")
print(f"Максимальное число пенальти: {max_penalties}")
print(f"Размер группы A: {len(group_A)}")
print(f"Средний возраст группы A: {mean_age_A:.2f}")

# Группа B
mean_aggression = df['Aggression'].mean()
max_sprint = df['SprintSpeed'].max()

group_B = df[(df['Aggression'] > mean_aggression) & (df['SprintSpeed'] == max_sprint)]
mean_age_B = group_B['Age'].mean()

print(f"\nСредняя агрессия: {mean_aggression:.2f}")
print(f"Максимальная скорость: {max_sprint}")
print(f"Размер группы B: {len(group_B)}")
print(f"Средний возраст группы B: {mean_age_B:.2f}")

# Разница
diff = mean_age_A - mean_age_B
result_15 = round(diff, 2)
print(f"\nРазница средних возрастов (группа A - группа B): {result_15}")