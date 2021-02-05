lyrics_beer = '99 bottles of beer on the wall, 99 bottles of beer.\
Take one down and pass it around, 98 bottles of beer on the wall.'


def sing():
    lyrics_beer = ''
    max_beer = 99
    min_beer = 1
    for bottle in range(max_beer, 0, -1):

        if bottle == min_beer:
            lyrics_beer += f'''
            {bottle} bottle of beer on the wall, {bottle} bottle of beer.
            Take one down and pass it around, no more bottles of beer on the wall.
            No more bottles of beer on the wall, no more bottles of beer.
            Go to the store and buy some more, {max_beer} bottles of beer on the wall.'''
        else:
            single_plural = 'bottles'
            if (bottle - 1) == 1:
                single_plural = 'bottle'

            lyrics_beer += f'''
            {bottle} bottles of beer on the wall, {bottle} bottles of beer.
            Take one down and pass it around, {bottle-1} {single_plural} of beer on the wall.'''


    lyrics_beer_array = [line.strip() for line in lyrics_beer.split('\n') if line]
    print("LEN", len(lyrics_beer_array))
    print(lyrics_beer_array[0])
    print(lyrics_beer_array[199])
    return lyrics_beer_array



print(sing())

# otra

def sing():
    R = []
    for i in range(99, 1, -1):
        R.append(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        R.append(f"Take one down and pass it around, {i-1} bottle{'s' if i>2 else ''} of beer on the wall.")
    R.append("1 bottle of beer on the wall, 1 bottle of beer.")
    R.append("Take one down and pass it around, no more bottles of beer on the wall.")
    R.append("No more bottles of beer on the wall, no more bottles of beer.")
    R.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
    return R

    def sing():
    line = "{} bottle{} of beer on the wall, {} bottle{} of beer.\nTake one down and pass it around, {} bottle{} of beer on the wall.\n"
    ans = ''
    for i in range(99, 0, -1):
        n1 = i
        s1 = "" if n1 == 1 else "s"
        n2 = str(i-1) if i > 1 else "no more"
        s2 = "" if n2 == '1' else "s"
        ans += line.format(n1, s1, n1, s1, n2, s2)
    ans += "No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall."
    return ans.split('\n')

def sing():
    s = 'bottles of beer'
    o = 'on the wall'
    a = []
    for i in range(99, 2, -1):
        a.append(f"{i} {s} {o}, {i} {s}.")
        a.append(f"Take one down and pass it around, {i-1} {s} {o}.")

    a.append(f"2 {s} {o}, 2 {s}.")
    a.append(f"Take one down and pass it around, 1 bottle of beer {o}.")

    a.append(f"1 bottle of beer {o}, 1 bottle of beer.")
    a.append(f"Take one down and pass it around, no more {s} {o}.")

    a.append(f"No more {s} {o}, no more {s}.")
    a.append(f"Go to the store and buy some more, 99 {s} {o}.")
    return a
