import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Загрузка данных
df = pd.read_csv('mycar_lin.csv')

print(df.head())
print(df.describe())




plt.scatter(df['Speed'], df['Stopping_dist'])
plt.xlabel('Speed (mph)')
plt.ylabel('Stopping distance (ft)')
plt.title('Зависимость тормозного пути от скорости')
plt.grid(True)
plt.show()




X = df[['Speed']]
y = df['Stopping_dist']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print(f"Коэффициент w1: {model.coef_[0]:.3f}")
print(f"Свободный член w0: {model.intercept_:.3f}")




y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

mae_train = mean_absolute_error(y_train, y_pred_train)
rmse_train = np.sqrt(mean_squared_error(y_train, y_pred_train))
r2_train = r2_score(y_train, y_pred_train)

mae_test = mean_absolute_error(y_test, y_pred_test)
rmse_test = np.sqrt(mean_squared_error(y_test, y_pred_test))
r2_test = r2_score(y_test, y_pred_test)

print("Обучающая выборка:")
print(f"  MAE = {mae_train:.3f}")
print(f"  RMSE = {rmse_train:.3f}")
print(f"  R² = {r2_train:.3f}")

print("Тестовая выборка:")
print(f"  MAE = {mae_test:.3f}")
print(f"  RMSE = {rmse_test:.3f}")
print(f"  R² = {r2_test:.3f}")




plt.scatter(X_test, y_test, color='blue', label='Фактические значения')
plt.plot(X_test, y_pred_test, color='red', linewidth=2, label='Предсказания')
plt.xlabel('Speed (mph)')
plt.ylabel('Stopping distance (ft)')
plt.title('Линейная регрессия: тестовая выборка')
plt.legend()
plt.grid(True)
plt.show()