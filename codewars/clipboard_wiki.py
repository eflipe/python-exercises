import pyperclip

list_text = '''Lists of animals\nLists of aquarium life\nLists of biologists by author
abbreviation\nLists of cultivars'''

text = pyperclip.paste()
# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):    # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list

text = '\n'.join(lines)

print("TEXT: ", text)
pyperclip.copy(text)
