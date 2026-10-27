import pandas as pd

data1 = [
    [101, 'John', 30000],
    [102, 'Amith', 35000],
    [103, 'Sona', 20000]
]

df1 = pd.DataFrame(
    data1, columns=['ID', 'Name', 'Stipend']
)

data2 = [
    [101, 'Developer'],
    [102, 'Developer'],
    [103, 'Tester']
]

df2 = pd.DataFrame(
    data2, columns=['ID', 'Position']
)

df3 = pd.merge(df1, df2, how='inner', on='ID')

print(df3)