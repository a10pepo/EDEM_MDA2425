import pandas as pd
import time
from termcolor import colored
from functions import make_header

pokemon_data = pd.read_csv('ALUMNOS/MIA/COKE_STUYCK/PYTHON/Session_5/Exercise_1/data/pokemon_data.csv')
names = pokemon_data['Name']


def pokemon_database_analysis():
    firstTime = True
    while True:
        if firstTime:
            make_header('POKEMON DATABASE ANALYSIS', 'Run some queries on the pokemon database.', bg_color='red')
            firstTime = False
            print('\nWhat would you like to do?')
        else:
            time.sleep(1)
            print('What would you like to do now?')

        print('''
[1]  1 Display 
[2]  2 Filter
[3]  3 Modify
[4]  4 Stats
[X]  Exit
    ''')
        option = input().lower()
        options = {
            '1': display_functions,
            '2': filter_functions,
            '3': modify_functions,
            '4': stats_functions
        }
        if option in options:
            options[option]()
        elif option == 'x':
            print('''            
Thank you for your time!

-----------------------
''')
            break
        else:
            print(colored("Oops! That's not a valid option. Try again...\n", 'red'))


def display_functions():
    while True:
        print('''
[1] Display every value
[2] Display first 5 values
[3] Display last 5 values
[4] Display every row
[5] Display a range of rows
[6] Display every column name
[7] Display every name
[8] Display every name and speed
[9] Display first 5 names using [::]
[X] Exit
        ''')
        option = input().lower()
        options = {
            '1': every_value,
            '2': first_5_values,
            '3': last_5_values,
            '4': every_row,
            '5': range_of_rows,
            '6': every_column_name,
            '7': every_name,
            '8': every_name_and_speed,
            '9': first_5_names_using_slice
        }
        if option in options:
            options[option]()
        elif option == 'x':
            break
        else:
            print(colored("Oops! That's not a valid option. Try again...\n", 'red'))


def filter_functions():
    while True:
        print('''
[1] Type 1 Water Pokemons
[2] Type 'Grass' or 'Poison' Pokemons
[3] Type 'Fire' or 'Poison' Pokemons
[4] Type 'Grass' or 'Poison' Pokemons with HP >= 70
[5] Pokemons containing 'Mega' in their name
[6] Pokemons not containing 'Mega' in their name
[7] Pokemons with name starting with 'Pi'
[X] Exit
        ''')
        option = input().lower()
        options = {
            '1': type_1_water_pokemons,
            '2': type_grass_or_poison_pokemons,
            '3': type_fire_or_poison_pokemons,
            '4': type_grass_or_poison_pokemons_with_hp,
            '5': pokemons_with_mega_in_name,
            '6': pokemons_without_mega_in_name,
            '7': pokemons_with_name_starting_with_pi
        }
        if option in options:
            options[option]()
        elif option == 'x':
            break
        else:
            print(colored("Oops! That's not a valid option. Try again...\n", 'red'))


def modify_functions():
    while True:
        print('''
[1] Rename 'Fire' column to 'Flame'
[2] Rename 'Flame' column back to 'Fire'
[3] Change all legendary Pokemons type to 'Fire'
[4] Create a new 'Total' column by adding 'HP', 'Attack', 'Defense' and 'Speed'
[5] Drop the 'Total' column
[X] Exit
        ''')
        option = input().lower()
        options = {
            '1': rename_fire_column_to_flame,
            '2': rename_flame_column_back_to_fire,
            '3': change_all_legendary_pokemons_type_to_fire,
            '4': create_new_total_column,
            '5': drop_total_column
        }
        if option in options:
            options[option]()
        elif option == 'x':
            break
        else:
            print(colored("Oops! That's not a valid option. Try again...\n", 'red'))


def stats_functions():
    while True:
        print('''
[1] Stats using describe()
[2] Sort by 'Name' ascending
[3] Average stats per type arranged by 'Defense' descending
[4] Average stats per type arranged by 'Attack' descending
[5] Average stats per type arranged by 'HP' descending
[6] Sum stats per type
[7] Number of pokemons for each type 1 category
[8] Number of pokemons for each type 1 and type 2 category
[X] Exit
        ''')
        option = input().lower()
        options = {
            '1': stats_describe,
            '2': sort_by_name,
            '3': average_stats_per_type_by_defense,
            '4': average_stats_per_type_by_attack,
            '5': average_stats_per_type_by_hp,
            '6': sum_stats_per_type,
            '7': number_per_type_1_category,
            '8': number_per_type_1_and_type_2_category
        }
        if option in options:
            options[option]()
        elif option == 'x':
            break
        else:
            print(colored("Oops! That's not a valid option. Try again...\n", 'red'))

# Read the CSV file with Pandas from 'pokemon_data.csv' stored in the 'data' folder and perform the following operations

# [1][1] Display every value
def every_value():
    print(pokemon_data)

# [1][2] Display first 5 values
def first_5_values():
    print(pokemon_data[:5])

# [1][3] Display last 5 values
def last_5_values():
    print(pokemon_data[-5:])

# [1][4] Display every row
def every_row():
    print(pokemon_data)

# [1][5] Display a range of rows
def range_of_rows():
    range_start = int(input('Enter the start of the range: '))
    range_end = int(input('Enter the end of the range: '))
    print(pokemon_data[range_start:range_end])

# [1][6] Display every column name
def every_column_name():
    column_names = ", ".join(pokemon_data.columns)
    print(column_names)

# [1][7] Display every name
def every_name():
    names_string = ", ".join(pokemon_data['Name'].tolist())
    print(names_string)

# [1][8] Display every name and speed
def every_name_and_speed():
    print(pokemon_data[['Name', 'Speed']])

# [1][9] Display first 5 names using [::]
def first_5_names_using_slice():
    print(pokemon_data[['Name']][:5])

# [2][1] Type 1 Water Pokemons
def type_1_water_pokemons():
    print(pokemon_data[pokemon_data['Type 1'] == 'Water'])

# [2][2] Type 'Grass' or 'Poison' Pokemons
def type_grass_or_poison_pokemons():
    print(pokemon_data[(pokemon_data['Type 1'] == 'Grass') | (pokemon_data['Type 2'] == 'Grass')])

# [2][3] Type 'Fire' or 'Poison' Pokemons
def type_fire_or_poison_pokemons():
    print(pokemon_data[(pokemon_data['Type 1'] == 'Fire') | (pokemon_data['Type 2'] == 'Fire')])

# [2][4] Type 'Grass' or 'Poison' Pokemons with HP >= 70
def type_grass_or_poison_pokemons_with_hp():
    print(pokemon_data[(pokemon_data['Type 1'] == 'Grass') | (pokemon_data['Type 2'] == 'Grass') & (pokemon_data['HP'] >= 70)])

# [2][5] Pokemons containing 'Mega' in their name
def pokemons_with_mega_in_name():
    print(pokemon_data[pokemon_data['Name'].str.contains('Mega')])

# [2][6] Pokemons not containing 'Mega' in their name
def pokemons_without_mega_in_name():
    print(pokemon_data[~pokemon_data['Name'].str.contains('Mega')])

# [2][7] Pokemons with name starting with 'Pi'
def pokemons_with_name_starting_with_pi():
    print(pokemon_data[pokemon_data['Name'].str.startswith('Pi')])
    
# [3][1] Rename 'Fire' column to 'Flame'
def rename_fire_column_to_flame():
    pokemon_data.rename(columns={'Fire': 'Flame'}, inplace=True)
    print(pokemon_data)

# [3][2] Rename 'Flame' column back to 'Fire'
def rename_flame_column_back_to_fire():
    pokemon_data.rename(columns={'Flame': 'Fire'}, inplace=True)
    print(pokemon_data)

# [3][3] Change all legendary pokemons type to 'Fire'
def change_all_legendary_pokemons_type_to_fire():
    pokemon_data.loc[pokemon_data['Legendary'] == True, 'Type 1'] = 'Fire'
    print(pokemon_data)

# [3][4] Create a new 'Total' column by adding 'HP', 'Attack', 'Defense' and 'Speed'
def create_new_total_column():
    pokemon_data['Total'] = pokemon_data['HP'] + pokemon_data['Attack'] + pokemon_data['Sp. Atk'] + pokemon_data['Defense'] + pokemon_data['Sp. Def'] + pokemon_data['Speed']
    print(pokemon_data)

# [3][5] Delete the 'Total' column
def drop_total_column():
    pokemon_data.drop(columns=['Total'], inplace=True)
    print(pokemon_data)
    
# [4][1] Stats using describe()
def stats_describe():
    print(pokemon_data.describe().round(1))

# [4][2] Sort by 'Name' ascending
def sort_by_name():
    print(pokemon_data.sort_values('Name', ascending=True))
    
# [4][3] Average stats per type by defense
def average_stats_per_type_by_defense():
    stats_mean = pokemon_data.groupby('Type 1')[['Defense', 'Attack', 'HP', 'Speed']].mean().round(1)
    stats_mean_sorted = stats_mean.sort_values(by='Defense', ascending=False)
    print(stats_mean_sorted)
# [4][4] Average stats per type by attack
def average_stats_per_type_by_attack():
    stats_mean = pokemon_data.groupby('Type 1')[['Defense', 'Attack', 'HP', 'Speed']].mean().round(1)
    stats_mean_sorted = stats_mean.sort_values(by='Attack', ascending=False)
    print(stats_mean_sorted)

# [4][5] Average stats per type by hp
def average_stats_per_type_by_hp():
    stats_mean = pokemon_data.groupby('Type 1')[['Defense', 'Attack', 'HP', 'Speed']].mean().round(1)
    stats_mean_sorted = stats_mean.sort_values(by='HP', ascending=False)
    print(stats_mean_sorted)

# [4][6] Sum stats per type
def sum_stats_per_type():
    print(pokemon_data.groupby('Type 1')[['Defense', 'Attack', 'HP', 'Speed']].sum())
    
# [4][7] Number of pokemons for each type 1 category
def number_per_type_1_category():
    print(pokemon_data.groupby(['Type 1']).size())

# [4][8] Number of pokemons for each type 1 and type 2 category
def number_per_type_1_and_type_2_category():
    print(pokemon_data.groupby(['Type 1', 'Type 2']).size())



# LEE EL ARCHIVO CVS SEPARÁNDOLO POR CHUNKS Y CON UN TAMAÑO DE (chunksize=5)
# ITERA POR LOS CHUNKS Y MUÉSTRALOS POR CONSOLA



if __name__ == '__main__':
    pokemon_database_analysis()