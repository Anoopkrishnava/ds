import pandas as pd
import numpy as np

data = {
    'A': [1, 2, np.nan, 4],
    'B': [np.nan, 2, 3, 4]
}

df = pd.DataFrame.from_dict(data, orient='index')
print(df)

df = df.fillna(0)
print(df)