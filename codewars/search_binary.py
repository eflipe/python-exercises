import math
def find_secret_number(low, high, guess_bot):
    print("High", high)
    print("Low", low)
    list_numbers = list(range(low, high+1))
    print(list_numbers)
    n = 0
    min = 0
    max = len(list_numbers) - 1
    while min <= max:
        mid = int((max + min)/2)
        n += 1
        print ("DEBUG:", "min:", min, "max:", max, "mid:", mid)
        print("Valor medio", list_numbers[mid])
        print("Intentos", n)
        guess_num = guess_bot.guess_number(list_numbers[mid])
        print("Guess BOT", guess_num)

        if guess_num == 'Correct':
            break
        else:
            if guess_num == 'Smaller':
                max = mid - 1
            else:
                min = mid + 1
    secret_integer = list_numbers[mid]
    return secret_integer
    # Good luck

    def find_secret_number(low, high, guess_bot):

    min = 0
    max = high
    while min <= max:
        mid = int((max + min)/2)
        secret_integer = mid
        guess_num = guess_bot.guess_number(secret_integer)

        if guess_num == 'Smaller':
            max = mid - 1
        elif guess_num == "Larger":
            min = mid + 1
        elif guess_num == "Correct":
            break

    return secret_integer


def find_secret_number(low, high, guess_bot):
    while True:
        m = (low + high) // 2
        x = guess_bot.guess_number(m)
        if x == "Smaller":
            high = m
        elif x == "Larger":
            low = m
        elif x == "Correct":
            return m
        else:
            return m + 1
