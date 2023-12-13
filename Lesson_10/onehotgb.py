import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

print(f"{data} \n")

unique_values = data['whoAmI'].unique()

for value in unique_values:
    data[value] = (data['whoAmI'] == value).astype(int)
    
data.drop('whoAmI', axis=1, inplace=True)
data.head()

print(data)