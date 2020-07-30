'''
Paste text from the clipboard

Do something to it

Copy the new text to the clipboard

#! python3
# Adds something to the start
# of each line of text on the clipboard.
'''

import pyperclip

text = pyperclip.paste()
print('Texto original :')
print(text)
print(type(text))

# split() return a list of strings, one for each line in the original string
lines = text.split('\n')
print(type(lines))
for i in range(len(lines)):
    # print(i)
    lines[i] = '- ' + lines[i].lower() # agregamos '- ' y lowercase
    # print(lines[i])
# join(): to make a single string value from the list Lines
text = '\n'.join(lines)
print('Texto modificado :\n')
print(text)
print(type(text))
print('\n El texto ha sido modificado con éxito')
pyperclip.copy(text)
