import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv('rent.csv', sep=';')
print("Размер данных:", df.shape)
print(df.head())




rooms_counts = df['rooms'].value_counts().sort_index()
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='rooms', palette='viridis')
plt.title('Распределение количества объявлений по числу комнат')
plt.xlabel('Количество комнат')
plt.ylabel('Количество объявлений')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Добавим подписи значений
for i, v in enumerate(rooms_counts):
    plt.text(i, v + 1, str(v), ha='center')
plt.show()




skew_rent = df['rent'].skew()
kurt_rent = df['rent'].kurtosis()   # избыточный эксцесс
print(f"Асимметрия rent: {skew_rent:.3f}")
print(f"Избыточный эксцесс rent: {kurt_rent:.3f}")
print(f"Эксцесс (приведённый к нормальному): {kurt_rent + 3:.3f}")




stat, p_value = stats.normaltest(df['rent'])
alpha = 0.05
print(f"Статистика теста: {stat:.3f}")
print(f"p-value: {p_value:.5f}")
if p_value < alpha:
    print("Отвергаем H0: распределение не является нормальным (p < 0.05)")
else:
    print("Не отвергаем H0: распределение может быть нормальным")




corr = df['rent'].corr(df['s'])
print(f"Коэффициент корреляции Пирсона (rent, s): {corr:.3f}")
plt.scatter(df['s'], df['rent'], alpha=0.5)
plt.xlabel('Площадь, кв.м')
plt.ylabel('Арендная плата, руб')
plt.title('Зависимость аренды от площади')
plt.grid(True)
plt.show()




groups = [df[df['rooms'] == r]['rent'] for r in sorted(df['rooms'].unique())]
f_stat, p_anova = stats.f_oneway(*groups)
print(f"ANOVA: F = {f_stat:.3f}, p = {p_anova:.5f}")




corr_coef, p_corr = stats.pearsonr(df['s'], df['rent'])
print(f"r = {corr_coef:.3f}, p = {p_corr:.5f}")




# Создание фиктивных переменных
df_dummies = pd.get_dummies(df, columns=['walls', 'district'], drop_first=True)
X = df_dummies.drop('rent', axis=1)
y = df_dummies['rent']

# Разделение на обучающую (80%) и тестовую (20%) выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Оценка качества
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
print(f"MAE = {mae:.1f} руб")
print(f"RMSE = {rmse:.1f} руб")
print(f"R² = {r2:.3f}")

# Коэффициенты модели
coef_df = pd.DataFrame({'Признак': X.columns, 'Коэффициент': model.coef_})
print(coef_df)
