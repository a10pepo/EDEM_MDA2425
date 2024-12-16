import pandas as pd
df = pd.read_csv('pokemon_data.csv')
# pd.set_option('display.max_columns',None)
# print(df.head)

# print(df.head())  

# print(df.tail()) 

print(df.columns)

# print(df['Name'])

# print(df[['Name','Speed']])

# print(df['Name'][0:5])

# pd.set_option('display.max_rows', None)
# print(df)

# rango_filas = df.iloc[10:20]
# print(rango_filas)

# nombre=df.iloc[9]['Name']
# print(nombre)

# print(df['#']['Name'])

# for index, row in df.iterrows():
#     print(f"Índice: {index}, Nombre: {row['Name']}")

# for index, row in df.iterrows():
#     if(row['Type 1']=="Water"):
#         print(f"{index}, Nombre: {row['Name']}")

# stats=df.describe()
# print(stats)

# df_grouped=df.sort_values(by='Name',ascending=False)
# print(df_grouped)

# df['TOTAL']=df['HP']+df['Attack']+df['Defense']+df['Speed']
# print(df)

# df=df.drop('TOTAL',axis=1)
# print(df)

# filtro= df[(df['Type 1'].isin(['Water', 'Poison']) & df['Type 2'].isin(['Water', 'Poison']))]
# print(filtro)

# filtro= df[(df['Type 1'].isin(['Fire', 'Poison']) | df['Type 2'].isin(['Fire', 'Poison']))]
# print(filtro)


# filtro=(
#     (df['Type 1'].isin(['Water', 'Poison']) & df['Type 2'].isin(['Water', 'Poison'])) &
#     (df['HP'] >= 70)
# )
# df_filtrado=df[filtro]
# print(df_filtrado)

# si_mega= df[df['Name'].str.contains('MEGA',case=False, na=False)]
# print(si_mega)

# no_mega= df[~df['Name'].str.contains('MEGA',case=False, na=False)]
# print(no_mega)

# df_pi = df[df['Name'].str.startswith("Pi", na=False)]
# print(df_pi)

# df = df.rename(columns={'Fire': 'Flame'})
# print(df)

# df = df.rename(columns={'Flame': 'Fire'})
# print(df)

# df['Type 1'] = df['Type 1'].replace('Fire', 'Flame')
# print(df)

# df['Type 1'] = df['Type 1'].replace('Flame', 'Fire')
# print(df)

# df_legen=df.copy()
# df_legen.loc[df_legen['Legendary'] == True, 'Type 1'] = 'Fire'
# print(df_legen)

# media_stats=df.groupby('Type 1').mean(numeric_only=True)
# sorted=media_stats.sort_values(by='Defense',ascending=False)
# print(sorted)

# media_stats=df.groupby('Type 1').mean(numeric_only=True)
# sorted=media_stats.sort_values(by='Attack',ascending=False)
# print(sorted)

# media_stats=df.groupby('Type 1').mean(numeric_only=True)
# sorted=media_stats.sort_values(by='HP',ascending=False)
# print(sorted)

# sum_stats=df.groupby('Type 1').sum(numeric_only=True)
# print(sum_stats)

# count_stats=df.groupby('Type 1').count()
# sorted=count_stats.sort_values(by='Name',ascending=False)
# print(sorted)

count_stats=df.groupby(['Type 1','Type 2']).count()
sorted=count_stats.sort_values(by='Name',ascending=False)
print(sorted)