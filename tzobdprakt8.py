import pandas as pd

# Загрузка данных (путь к файлу может отличаться)
df = pd.read_csv('films.csv')

# Преобразование даты в datetime
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

# Удаление строк, где нет режиссёра или даты
df_clean = df.dropna(subset=['director', 'release_date']).copy()



# Извлекаем месяц
df_clean['month'] = df_clean['release_date'].dt.month

# Зимние месяцы
winter_months = [12, 1, 2]
winter_films = df_clean[df_clean['month'].isin(winter_months)]

# Количество зимних фильмов по режиссёрам
winter_count = winter_films['director'].value_counts()

# Режиссёр с максимумом
top_winter_director = winter_count.idxmax()
top_winter_count = winter_count.max()

print(f"Режиссёр, выпустивший больше всего фильмов зимой: {top_winter_director}")
print(f"Количество зимних фильмов: {top_winter_count}")



# Подсчёт количества фильмов по режиссёрам
director_counts = df_clean['director'].value_counts()

# Режиссёр с максимумом
top_director = director_counts.idxmax()
top_count = director_counts.max()

print(f"Режиссёр, снявший больше всего фильмов: {top_director}")
print(f"Количество фильмов: {top_count}")