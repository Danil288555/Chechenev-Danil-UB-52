import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных
df = pd.read_csv('films.csv')

# Преобразование бюджетов и сборов в числа (убираем возможные символы)
df['budget'] = pd.to_numeric(df['budget'], errors='coerce')
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')

# Вычисление прибыли
df['profit'] = df['revenue'] - df['budget']

# Удаление фильмов с отсутствующими значениями бюджета, сборов или режиссёра
df_clean = df.dropna(subset=['budget', 'revenue', 'director', 'profit'])

print(f"Всего фильмов после очистки: {len(df_clean)}")



# Топ-10 режиссёров по количеству фильмов
top_directors = df_clean['director'].value_counts().head(10).index
df_top = df_clean[df_clean['director'].isin(top_directors)]

# Построение боксплота
plt.figure(figsize=(12, 6))
sns.boxplot(data=df_top, x='director', y='profit', palette='Set2')
plt.xticks(rotation=45, ha='right')
plt.title('Распределение прибыли фильмов по режиссёрам (топ-10 по числу фильмов)')
plt.xlabel('Режиссёр')
plt.ylabel('Прибыль (доллары)')
plt.tight_layout()
plt.show()



# Группировка по году
films_per_year = df_clean.groupby('release_year').size().reset_index(name='count')

# Построение графика
plt.figure(figsize=(12, 6))
plt.plot(films_per_year['release_year'], films_per_year['count'], marker='o', linestyle='-', color='teal')
plt.title('Количество выпускаемых фильмов по годам')
plt.xlabel('Год выпуска')
plt.ylabel('Количество фильмов')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()