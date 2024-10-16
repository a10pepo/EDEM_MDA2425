import pandas as pd

data = pd.read_csv('Datos/pokemon_data.csv')

print(data)

print(data.head())

print(data.tail())

print(data.columns)

print(data['Name'])

print(data[['Name', 'Speed']])

print(data['Name'][:5])

print(data.iloc[:])

print(data.iloc[5:10])

print(data.iloc[9]['Name'])

for index, row in data.iterrows():
    print(index, row['Name'])

print(data[data['Type 1'] == 'Water'])

print(data.describe())

print(data.sort_values('Name'))

data['Total'] = data['HP'] + data['Attack'] + data['Defense'] + data['Speed']
print(data)

data = data.drop(columns=['Total'])

print(data[(data['Type 1'] == 'Grass') and (data['Type 2'] == 'Poison')])

print(data[(data['Type 1'] == 'Fire') | (data['Type 2'] == 'Poison')])

print(data[(data['Type 1'] == 'Grass') & (data['Type 2'] == 'Poison') & (data['HP'] >= 70)])

print(data[data['Name'].str.contains('Mega')])

print(data[~data['Name'].str.contains('Mega')])

print(data[data['Name'].str.startswith('Pi')])

data.rename(columns={'Type 1': 'Flame'}, inplace=True)
print(data)

data.rename(columns={'Flame': 'Type 1'}, inplace=True)
print(data)

data.loc[data['Legendary'] == True, 'Type 1'] = 'Fire'
print(data)

print(data.groupby('Type 1').mean().sort_values('Defense'))

print(data.groupby('Type 1').mean().sort_values('Attack'))

print(data.groupby('Type 1').mean().sort_values('HP'))

print(data.groupby('Type 1').sum())

print(data['Type 1'].value_counts())

print(data.groupby(['Type 1', 'Type 2']).size())

chunk_size = 5
for chunk in pd.read_csv('pokemon_data.csv', chunksize=chunk_size):
    print(chunk)