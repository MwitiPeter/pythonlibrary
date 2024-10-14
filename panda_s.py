import pandas as pd
data = {'name': ['Alice', 'bob','Charlie'],
        'age': [25,30,35],
        'city':['NewYork','Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

df['salary'] = [5000, 6000, 7000]
grouped = df.groupby('age')['salary'].mean()

print(grouped)
# print(df['name'])
# print(df[['name', 'age']])
# print(df.loc[1])
# print(df[df['age'] > 30 ])
# print(df)