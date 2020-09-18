from soupy import getBSObject
import random

soup = getBSObject('https://en.wikipedia.org/wiki/List_of_pasta_dishes')


def get_list_of_pastas():
    pasta_div = soup.select(
        '#mw-content-text > div.mw-parser-output > div:nth-child(26) > '
        'table > tbody > tr:nth-child(3) > td > div > ul > li')

    pastas = []

    for link in pasta_div:
        pastas.append(link.get_text('a'))

    return pastas


def get_random_pasta():
    pastas = get_list_of_pastas()

    print(f'Your mystery pasta is {random.choice(pastas)} !!!\n')


def cant_decide():
    rand = random.randint(1,2)

    return str(rand)
