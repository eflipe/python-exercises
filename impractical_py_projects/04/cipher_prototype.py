ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"

cipherlist = list(ciphertext.split())
print(cipherlist)

# inicilizamos las variables

COLS = 4
ROWS = 5
key = '-1 2 -3 4'
translation_matrix = [None] * COLS  # nested list, a list of lists
plaintext = ''
start = 0
stop = ROWS

key_int = [int(key) for key in key.split()]
print(key_int)
# turn columns into items in list of lists
for key in key_int:
    if key < 0:  # reading bottom-to-top of column
        print(f'Key < 0: {key}')
        col_items = cipherlist[start:stop]
        print(f'Col_items: {col_items}')
    elif key > 0:  # reading top-to-bottom of columnn
        print(f'Key > 0: {key}')
        col_items = list((reversed(cipherlist[start:stop])))
        print(f'Col_items reversed: {col_items}')

    translation_matrix[abs(key)-1] = col_items
    print(f'translation_matrix: {translation_matrix}')
    start += ROWS
    stop += ROWS

print("\nciphertext = {}".format(ciphertext))
print("\ntranslation matrix=", *translation_matrix, sep="\n")
print("\nkey length= {}".format(len(key_int)))

# loop through nested lists popping off last item to new list
for i in range(ROWS):
    for col_items in translation_matrix:
        word = str(col_items.pop())
        plaintext += word + ''

print("\nplaintext = {}".format(plaintext))
