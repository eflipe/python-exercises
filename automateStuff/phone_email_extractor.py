import pyperclip
import re

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?  # optional area code
(\s|-|\.)?  # separator: space, guion o punto
(\d{3})  # first 3 digits
(\s|-|\.)
(\d{4})  # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
)''', re.VERBOSE)

# email regex
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+ # username
@ # @ symbol
[a-zA-Z0-9.-]+  # domain name
(\.[a-zA-Z]{2,4})  # punto-algo
)''', re.VERBOSE)

'''
800-420-7240
415-863-9900
415-863-9950
info@nostarch.com
media@nostarch.com
academic@nostarch.com
help@nostarch.com
'''
# find matches in clipboard Text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    print(groups[1])
    print(groups[2])
    print(groups[3])
    print(groups[4])
    print(groups[5])
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
# pyperclip.copy() takes only a single string value, not a list of strings, so you call the join() on matches list.
# copy results to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Info copiada!')
    print('\n'.join(matches))
else:
    print('No se encontró infromación')
