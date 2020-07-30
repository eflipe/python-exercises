link = 'https://www.codewars.com/kata/5aee86c5783bb432cd000018/train/python'
drink_string = "1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer"
import re


def hydrate(drink_string):
    result = [int(i) for i in re.findall(r'\d+', drink_string)]
    print(type(result[0]))
    print(result)
    print(sum(result))
    print(f"{sum(result)} glasses of water")


hydrate(drink_string)
print(type(drink_string[0]))


def hydrate(drink_string):
    c=sum(int(c) for c in drink_string if c.isdigit())
    return "{} {} of water".format(c,'glass') if c==1 else "{} {} of water".format(c,'glasses')


def hydrate(drink_string):
    n = sum([int(a) for a in drink_string if a.isnumeric()])
    return str(n) +' glass of water' if n==1 else str(n) +' glasses of water'
