import pandas as pd

data = [
    [1, 'Alice', 10],
    [2, 'Bob', 15],
    [3, 'Don', 25]
]

df = pd.DataFrame(data, columns=['ID', 'Name', 'Score'])
print(df)