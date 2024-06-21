import pandas as pd
import random

# Создание исходного DataFrame
lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Преобразование в one hot вид
one_hot_encoded = pd.concat([
    data,
    pd.DataFrame({
        'robot': (data['whoAmI'] == 'robot').astype(int),
        'human': (data['whoAmI'] == 'human').astype(int)
    })
], axis=1)

# Вывод первых пяти строк нового DataFrame
print(one_hot_encoded.head())
