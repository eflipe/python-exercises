import collections

numberOfPets = {'dogs': 2}
print('I have', numberOfPets.get('cats', 0), 'cats.')

'''
The numberOfPets.get('cats', 0) call checks whether the key 'cats' exists in the numberOfPets dictionary.
If it does, the method call returns the value for the 'cats' key. If it doesn’t, it returns the second argument, 0, instead.
'''

numberOfPets.setdefault('cats', 0)
numberOfPets['cats'] += 10
print(numberOfPets['cats'])


scores = collections.defaultdict(int)
scores['Pepe'] += 11
scores['Fulano'] += 8
print(scores)

booksReadBy = collections.defaultdict(list)
booksReadBy['Pepe'].append('La biblia')
booksReadBy['Pepe'].append('Coran')
print(booksReadBy)

for key, values in booksReadBy.items():
    print(key, values)
    for item in values:
        print(item)
