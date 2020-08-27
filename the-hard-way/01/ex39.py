states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville', 'NY': 'New York', 'OR': 'Portland'}

#adding

print('-' * 10)
print('NY states has: ', cities['NY'])
print('OR State has: ', cities['OR'])
print('-' * 10)
print('Michigan...', states['Michigan'])
print('Florida...', states['Florida'])

print('-' * 10)
print('Accedes usando un dict dentro de un dict', cities[states['Michigan']])
print('Accedes usando un dict dentro de un dict', cities[states['Florida']])

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f'{state} is abbreviated {abbrev}')

for abb, city in list(cities.items()):
    print(f"{abb} has the city {city}")

# los dos al mismo tiempo
print('-' * 10)
for state, abb in list(states.items()):
    print(f"{state} is una abbreviation de {abb}")
    print(f'y tiene la ciudad de {cities[abb]}')

# get
state = states.get('Texas')

if not state:
    print('No existe')

city = cities.get('TX', "No está")
print(f'Sorry, no existe {city}')

print("list(states.items()): ", list(states.items()))
