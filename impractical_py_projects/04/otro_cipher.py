"""
encriptador de la guerra civil.
"""

# USER INPUT:

# texto a ser encriptado
plaintext = """Mensaje super secreto secretísimo"""


def main():
    message = prep_plaintext(plaintext)
    rails = build_rails(message)
    encrypt(rails)


def prep_plaintext(plaintext):
    # juntamos el mensaje
    message = "".join(plaintext.split())
    message = message.upper()
    print(f"\nplaintext = {plaintext}")

    return message


def build_rails(message):
    evens = message[::2]
    odds = message[1::2]
    rails = evens + odds
    return rails


def encrypt(rails):
    ciphertext = ' '.join([rails[i:i+5] for i in range(0, len(rails), 5)])
    print(f"ciphertext = {ciphertext}")


if __name__ == '__main__':
    main()
