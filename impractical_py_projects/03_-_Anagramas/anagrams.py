import load_dict

word_list = load_dict.load('X')

anagram_list = []

# iput para buscar el anagrama(s):
name = input('Ingresar un nombre: ')
print("Input name = {}".format(name))
name = name.lower()
print("Using name = {}".format(name))

name_sorted = sorted(name)
print(f"Sorted: {name_sorted}")
for word in word_list:
    word = word.lower()
    if word != name:
        if sorted(word) == name_sorted:
            anagram_list.append(word)

if len(anagram_list) == 0:
    print('No hay suficientes palabras en el dictionario.')
else:
    print("Anagrams =", *anagram_list, sep='\n')
