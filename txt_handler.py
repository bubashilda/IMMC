import pandas as pd

df = pd.read_csv('results/res.csv')
df.to_excel('results/res.xlsx', index=False)