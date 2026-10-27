import pandas as pd

data = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Paris'],
    ['Charlie', 35, 'London']
]

df = pd.DataFrame(
    data,
    columns=['Name', 'Age', 'City'],
    index=['p1', 'p2', 'p3']
)

print(df)

df = df.reset_index(drop=True)
print(df)