import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні для кількості кожного продукту
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# Функція цілі: максимізувати кількість продуктів
model += lemonade + fruit_juice, "Total_Production"

# Обмеження ресурсів
model += 2 * lemonade + fruit_juice <= 100, "Water_Limit"
model += lemonade <= 50, "Sugar_Limit"
model += lemonade <= 30, "Lemon_Juice_Limit"
model += 2 * fruit_juice <= 40, "Fruit_Puree_Limit"

# Розв'язування задачі
model.solve()

# Вивід результатів
print("Production Plan:")
print(f"Lemonade: {lemonade.varValue}")
print(f"Fruit Juice: {fruit_juice.varValue}")