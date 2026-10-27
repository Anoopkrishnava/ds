import pandas as pd

listdata = [
    [1, 'Alice', 15],
    [2, 'Bob', 15],
    [3, 'Don', 45]
]

df = pd.DataFrame(listdata, columns=['ID', 'Name', 'Score'])

print("Data frame")
print(df)

# Sorting first by score, then by ascending order of name
sorted_df = df.sort_values(
    by=['Score', 'Name'],
    ascending=[False, True]
)

print("Sorted Dataframe")
print(sorted_df)