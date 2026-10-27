import pandas as pd

data = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Paris'],
    ['Charlie', 35, 'London']
]

df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
print(df.iloc[0:2, :])