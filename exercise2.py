import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа
N = 10000  # Кількість випадкових точок

# Генерація випадкових точок
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)

# Визначення кількості точок під кривою
points_under_curve = y_random < f(x_random)
points_above_curve = y_random >= f(x_random)

# Обрахунок інтегралу
area_under_curve = points_under_curve.sum() / N
estimated_area = area_under_curve * (b - a) * f(b)

# Підготовка даних для графіка
x_plot = np.linspace(-0.5, 2.5, 400)
y_plot = f(x_plot)
ix = np.linspace(a, b)
iy = f(ix)

# Візуалізація результату
plt.figure(figsize=(8, 6))
plt.plot(x_plot, y_plot, 'r', linewidth=2, label='f(x) = x^2')
plt.scatter(x_random[points_under_curve], y_random[points_under_curve], color='green', s=1)
plt.scatter(x_random[points_above_curve], y_random[points_above_curve], color='blue', s=1)
plt.fill_between(ix, iy, color='gray', alpha=0.3)
plt.title(f'Монте-Карло Інтеграція (Оцінка = {estimated_area:.4f})')
plt.legend()
plt.grid(True)
plt.show()

# Обчислення інтеграла аналітично
result, _ = spi.quad(f, a, b)
print("Аналітично обчислений інтеграл:", result)
print("Метод Монте-Карло інтеграл:", estimated_area)
