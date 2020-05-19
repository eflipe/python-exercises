from random import randint
import string
import load_dict

input_message = "Ayuda fijarse bien"

message = ''

for char in input_message:
    if char in string.ascii_letters:
        # ascii_letters cotiene: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        message += char

print(message, "\n")
message = "".join(message.split())
print(message, "\n")


word_list = load_dict.load('C:\\Users\\Felipe\\Exercism\\python\\python-exercises\\impractical_py_projects\\02_-_p\\palabras_todas.txt')

vocab_list = []
for letter in message:
    size = randint(6, 12)
    for word in word_list:
        if len(word) == size and word[0].lower() == letter.lower() and word not in vocab_list:
            vocab_list.append(word)
            break
if len(vocab_list) < len(message):
    print("El diccionario no es suficiente")
else:
    print("Vocabulario words for Unit 1: \n", *vocab_list, sep="\n")
