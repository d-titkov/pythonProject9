# Узнать какая максимальная households в зоне минимального значения population.

import pandas as pd

# Загрузка данных из файла csv
data = pd.read_csv('california_housing_test.csv')

# Фильтрация данных по числу жителей
filtered_data = data[data["population"] == data["population"].min()]

# Нахождение максимальной households
max_households = filtered_data["households"].max()

# Вывод результата
print("Максимальное число households в зоне минимального значения population:", max_households)