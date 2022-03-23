import pandas as pd

df = pd.read_csv('/Users/glebspivakovskij/Documents/GitHub/IMMC/models/res.csv', sep=';')
df.to_excel('/Users/glebspivakovskij/Documents/GitHub/IMMC/models/res.csv', index=False)