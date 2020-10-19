import pandas as pd

df = pd.read_excel('SoftwareList.xlsx')
print(df.loc[df['Difficulty'] == 1])
#print(df['Difficulty'])
