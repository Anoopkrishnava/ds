import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("medal.csv",delimiter=":")
countries = df['Country'].to_numpy()
medals=df['Gold_Medal'].to_numpy()
plt.pie(medals,labels=countries,autopct='%1.1f%%')
plt.show()