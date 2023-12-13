import pandas as pd
import random

# Создаем DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Выводим исходные данные
print(f"{data} \n")

# Получаем уникальные значения из столбца 'whoAmI'
unique_values = data['whoAmI'].unique()

# Создаем новые столбцы в DataFrame для каждого уникального значения
for value in unique_values:
    data[value] = (data['whoAmI'] == value).astype(int)

# Удаляем исходный столбец 'whoAmI'
data.drop('whoAmI', axis=1, inplace=True)

# Выводим результат
data.head()
print(data)