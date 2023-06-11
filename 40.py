#Работать с файлом california_housing_train.csv, который находится в папке sample_data.
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)

import pandas as pd

# Загрузка данных из файла csv
data = pd.read_csv('california_housing_test.csv')

# Фильтрация данных по числу жителей
filtered_data = data[data["population"] <= 500]

# Вычисление средней стоимости дома
mean_house_value = filtered_data["median_house_value"].mean()

# Вывод результата
print("Средняя стоимость дома, где число жителей не превышает 500:", mean_house_value)