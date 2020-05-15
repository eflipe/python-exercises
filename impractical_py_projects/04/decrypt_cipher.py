"""
Decriptador
"""

import math
import itertools

# texto a descifrar

ciphertext = """MNAEU ESCEO ERTSM ESJSP RERTS CEÍIO"""


def main():
    message = prep_ciphertext(ciphertext)
    row1, row2 = split_rails(message)
    decrypt(row1, row2)


def prep_ciphertext(ciphertext):
    """Remueve los espacios en blanco"""
    message = "".join(ciphertext.split())
    print("\nciphertext = {}".format(ciphertext))
    print("\nmessage = {}".format(message))
    return message


def split_rails(message):
    row_1_len = math.ceil(len(message)/2)
    row1 = message[:row_1_len]
    row2 = message[row_1_len:]
    return row1, row2


def decrypt(row1, row2):
    plaintext = []
    for r1, r2 in itertools.zip_longest(row1, row2):
        plaintext.append(r1.lower())
        plaintext.append(r2.lower())
    if None in plaintext:
        plaintext.pop()
    print("rail 1 = {}".format(row1))
    print("rail 2 = {}".format(row2))
    print("\nplaintext = {}".format(''.join(plaintext)))


if __name__ == '__main__':
    main()
