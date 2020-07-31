import os

this_file_path = os.path.abspath(__file__)
# print(this_file_path)
BASE_DIR = os.path.dirname(this_file_path)
PROJECT_DIR = os.path.dirname(BASE_DIR)
# print(PROJECT_DIR)
fname_path = '/home/felipe/workspace/30-days-py/30-days/day_10/ejemplo_texto.txt'
email_path = os.path.join(BASE_DIR, 'templates', 'email.txt')

content = ''

with open(email_path, 'r') as f:
    content = f.read()

print(content.format(name='Pepe', item="Piedra filosofal"))

