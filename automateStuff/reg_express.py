'''
Finding Patterns of Text with Regular Expressions
1. Import the regex module with import re.
2. Create a Regex object with the re.compile() function. (Remember to use a raw string.)
3. Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
4. Call the Match object’s group() method to return a string of the actual matched text.



'''
import re
# Passing a string value representing your regular expression to re.compile()
# returns a Regex pattern object
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(type(phoneNumRegex))  # class re.pattern
# putting an r before the first quote of the string value,
# you can mark the string as a raw string, which does not escape characters.

# search() method searches the string it is passed for any matches to the regex.
# the search() method returns a Match object. Match objects have a group()
# method that will return the actual matched text from the searched string.
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
searchNumber = phoneNumRegex.search('My number is 415-555-4242.')
print(type(searchNumber))
print('Phone number found: ' + searchNumber.group())
# URL:  http://regexpal.com/
# URL: pythex.org

# Grouping with Parentheses

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
searchNum = phoneNumRegex.search('mi número es 321-573-7685')
print(searchNum.group(1))
print(searchNum.group(2))
print(searchNum.group(0))
print(searchNum.group())
# groups()
print(searchNum.groups())  # returns a tuple

areaCode, mainNumber = searchNum.groups()  # multiple-assignment trick
print(areaCode)
print(mainNumber)
# if you need to match a parenthesis
# The \( and \) escape characters
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
mo.group(1)
#'(415)'
mo.group(2)
#'555-4242'

# Matching Multiple Groups with the Pipe ||
# You can use it anywhere you want to match one of many expressions.
otroRegex = re.compile(r'Pepe|Fulano')
search_1 = otroRegex.search('Existe un Pepe y otro Fulano')
print(search_1.group())
search_1 = otroRegex.search('Existe un Fulano y otro Pepe')
print(search_1.group())
# utilizando prefijo
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))
# the ?: “Match zero or one of the group preceding this question mark.”
# The (wo)? part of the regular expression means that the pattern wo is an optional group.
batRegex = re.compile(r'Bat(wo)?man')
bat_1 = batRegex.search('Lalala Batman se fue')
print(bat_1.group())
bat_2 = batRegex.search('Lalala Batwoman se fue')
print(bat_2.group())
# The regex will match text that has zero instances or one instance of wo in it

# the regex look for phone numbers that do or do not have an area code
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
phone_obj = phoneRegex.search('Mi tel es 321-321-4323')
print(phone_obj.group())
phone_obj = phoneRegex.search('Mi tel es 321-4323')
print(phone_obj.group())
# puedo o no tener los 3 primeros digits

#The *: means “match zero or more”—the group that precedes the star can occur any number of times in the text
batRegex = re.compile(r'Bat(wo)*man')
bat_1 = batRegex.search('Lalala Batman se fue')
print(bat_1.group())
bat_2 = batRegex.search('Lalala Batwoman se fue')
print(bat_2.group())
bat_3 = batRegex.search('Lalala Batwowowowoman se fue')
print(bat_3.group())

# the + : match zero or more
# greedy = matchea la cadena más larga
#  The non-greedy version of the curly brackets, which matches the shortest
# string possible, has the closing curly bracket followed by a question mark.
greedyRegex = re.compile(r'(Ha){3,5}')
greedy_obj = greedyRegex.search('HaHaHaHaHa')
print(greedy_obj.group())
# no-greedy
nongreedyRegex = re.compile(r'(Ha){3,5}?')
greedy_obj = nongreedyRegex.search('HaHaHaHaHa')
print(greedy_obj.group())

# The findall() Method: return a list of strings
#  search() devuelve un ObjectoRegex
# will return the strings of every match in the searched string.
# findall() vs search()
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())
phoneFindAll = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(phoneFindAll)
# If there are groups in the regular expression, then findall() will return a list of tuples.
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
phoneTuples = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(phoneTuples)
'''
To summarize what the findall() method returns, remember the following:

When called on a regex with no groups,
such as \d\d\d-\d\d\d-\d\d\d\d, the method findall()
returns a list of string matches,
such as ['415-555-9999', '212-555-0000'].
When called on a regex that has groups,
such as (\d\d\d)-(\d\d\d)-(\d\d\d\d),
the method findall() returns a list of tuples
of strings (one string for each group),
such as [('415', '555', '9999'), ('212', '555', '0000')].
'''


#ejemplo: d+ = uno o más digitos numericos
# \s = seguido por un whitespace
# \w+ = followed by one or more letter/digit/underscore characters
xmasRegex = re.compile(r'\d+\s\w+')
ejemplo_1 = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 \
swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(ejemplo_1)

# [] : You can define your own character class using square brackets.
vocalesRegex = re.compile(r'[aeiouAEIOU]')
vocales = vocalesRegex.findall('Ni idea, que palabra de mierda. MIERDA')
print(vocales)
# negative character class: will match all the characters that are not in the character class
vocalesRegex = re.compile(r'[^aeiouAEIOU]')
vocales = vocalesRegex.findall('Ni idea, que palabra de mierda. MIERDA')
print(vocales)

# dot
atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')

# the dot-star (.*)
# Remember that the dot character means “any single character except the newline,” and the star character means “zero or more of the preceding character.”
nameRegex = re.compile(r'Nombre: (.*) Apellido: (.*)')
name_obj = nameRegex.search('Nombre: Leo Apellido: Paredes')
print(name_obj.group(1))
print(name_obj.group(2))
# re.DOTALL : you can make the dot character match all characters, including the newline character
noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
# con DOTALL
newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\
\nUphold the law.').group())
# Case-Insensitive Matching
nombre = re.compile(r'filomeno', re.I)
print(nombre.search('FILOMENO etc etc etc etcectetc').group())
# sub() Method
# substitute new text in place of those patterns.
# The sub() method returns a string with the substitutions applied.
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)
