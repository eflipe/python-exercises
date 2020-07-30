import sys
import string


def load_text(file):
    """Load a text file as a string"""
    with open(file) as f:
        file = f.read().strip()
        return file


def sole_null_cipher(message, lookahead):

    for i in range(1, lookahead+1):
        plaintext = ''
        count = 0
        found_first = False
        for char in message:
            if char in string.punctuation:
                count = 0
                found_first = True
            elif found_first is True:
                count += 1
            if count == i:
                plaintext += char
        print("Using offset of {} after punctuation = {}".format(i, plaintext))
        print()


def main():
    filename = input("\nIngresa el mensaje: ")
    try:
        loaded_message = load_text(filename)
    except IOError as e:
        print(f'{e}. Error!')
        sys.exit(1)
    print("\nMensaje =")
    print("{}".format(loaded_message), "\n")
    print("\nList of punctuation marks to check = {}".format(string.punctuation))
    message = ''.join(loaded_message.split())

    while True:
        lookahead = input("\nLetras a checkear después de" \
                          "un signo de puntuación: ")
        if lookahead.isdigit():
            lookahead = int(lookahead)
            break
        else:
            print("Pls, ingresa un número")
    print()
    sole_null_cipher(message, lookahead)


if __name__ == '__main__':
    main()
