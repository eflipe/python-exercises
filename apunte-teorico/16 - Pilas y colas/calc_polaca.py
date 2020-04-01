# Calculadora Polaca invesa

"""
- Mientras se lean números, se apilan.
- En el momento en el que se detecta una operación binaria +, -, * o / se desapilan los dos últimos números apilados, se ejecuta la operación indicada, y el resultado de esa operación
se apila

- Si la expresión está bien formada, tiene que quedar al final un único número en la pila (el
resultado).

Posibles errores:
    – Queda más de un número al final (por ejemplo si la cadena de entrada fue "5 3"),

    – Ingresa algún caracter que no se puede interpretar ni como número ni como una de
    las cinco operaciones válidas (por ejemplo si la cadena de entrada fue "5 3 &")

    – No hay suficientes operandos para realizar la operación (por ejemplo si la cadena
    de entrada fue "5 3 - +").

"""

from ejemplo import Pila


def calculadora_polaca(elementos):
    print(elementos)

    p = Pila()
    for elemento in elementos:
        print("DEBUG: ", elemento)
        print("PILA", p.items)
        try:
            numero = float(elemento)
            p.apilar(numero)
            print("DEBUG: apila", numero)
            print("PILA", p.items)
        # Si no se puede convertir en número, debería ser un operando
        except ValueError:
            # Si NO es un operando válido, levanta ValueError
            if elemento not in ('+', '-', '*', '/'):
                raise ValueError("Operando inválido")
            # Si es un operando válido, intenta desapilar y operar
            try:
                a1 = p.desapilar()
                print("DEBUG: desapila", a1)
                a2 = p.desapilar()
                print("DEBUG: desapila", a2)
            except IndexError:
                raise ValueError("Faltan operandos")

            if elemento == '+':
                resultado = a2 + a1
            elif elemento == '-':
                resultado = a2 - a1
            elif elemento == '*':
                resultado = a2 * a1
            elif elemento == '/':
                resultado = a2 / a1
            print("DEBUG: apila Resultado", resultado)
            p.apilar(resultado)

    resultado = p.desapilar()
    if not p.esta_vacia():
        raise ValueError("Sobrando operandos")
    return "Resultado: ", resultado


def main():
    expresion = input("ingrese la expresion a evaluar: ")
    elementos = expresion.split()
    print(elementos)
    print(calculadora_polaca(elementos))


main()
