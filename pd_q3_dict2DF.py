import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 30, 28],
    "City": ["Delhi", "Mumbai", "Bangalore"]
}
df = pd.DataFrame(data)
print("Dictionary to DataFrame:\n", df)