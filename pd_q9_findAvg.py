import pandas as pd

data = [
    ['Alice', 'Teacher', 25000],
    ['Bob', 'Doctor', 55000],
    ['Charlie', 'Teacher', 20000],
    ['Dylan', 'Doctor', 35000],
    ['Emma', 'Engineer', 65000]
]

df = pd.DataFrame(data, columns=['Name', 'Job', 'Salary'])
print(df)

avg_by_job = df.groupby('Job')['Salary'].mean()
print(avg_by_job)