from soupy import getBSObject
import random
from enum import Enum

soup = getBSObject('https://en.wikipedia.org/wiki/List_of_pasta_dishes')


class Regions(Enum):
    BURMESE = '1'
    CENTRAL_ASIAN_TURKIC = '2'
    CHINESE = '3'
    JAPANESE = '4'
    KOREAN = '5'
    FILIPINO = '6'
    THAI = '7'
    VIETNAMESE = '8'
    INDONESIAN = '9'
    MALAYSIAN_SINGAPOREAN = '10'


def get_random_noodles_region(region):
    noodles = region
    print()
    print(f'Your mystery noodle dish is {random.choice(noodles)} !!!\n')


def get_region_noodles(region):
    if region == Regions.BURMESE.value:
        get_random_noodles_region(get_burmese())
    elif region == Regions.CENTRAL_ASIAN_TURKIC.value:
        get_random_noodles_region(get_central_asian_turkic())
    elif region == Regions.CHINESE.value:
        get_random_noodles_region((get_chinese()))
    elif region == Regions.JAPANESE.value:
        get_random_noodles_region(get_japanese())
    elif region == Regions.KOREAN.value:
        get_random_noodles_region(get_korean())
    elif region == Regions.FILIPINO.value:
        get_random_noodles_region(get_filipino())
    elif region == Regions.THAI.value:
        get_random_noodles_region(get_thai())
    elif region == Regions.VIETNAMESE.value:
        get_random_noodles_region(get_vietnamese())
    elif region == Regions.INDONESIAN.value:
        get_random_noodles_region(get_vietnamese())
    elif region == Regions.MALAYSIAN_SINGAPOREAN.value:
        get_random_noodles_region(get_malaysian_singaporean())
    else:
        print('Sorry, didn\'t understand that, try again\n')


def get_random_noodles():
    noodles_array = [get_burmese(), get_central_asian_turkic(), get_chinese(), get_japanese(), get_korean(),
                     get_filipino(),
                     get_thai(), get_vietnamese(), get_indonesian(), get_malaysian_singaporean()]

    noodles = []
    for i in noodles_array:  # loops through the array of functions
        for y in i:
            noodles.append(y)  # actually executes the func and assigns all the noods to a list

    print(f'Your mystery noodles are {random.choice(noodles)} !!!\n')


def display_regions():
    regions = ['Burmese', 'Central Asian/Turkic', 'Chinese', 'Japanese', 'Korean',
               'Filipino', 'Thai', 'Vietnamese', 'Indonesian', 'Malaysian/Singaporean']
    count = 1
    for i in regions:
        print(f'{count}. {i}')
        count += 1


def get_burmese():
    pasta_div = soup.select('#mw-content-text > div.mw-parser-output > div:nth-child(27) > table > tbody > '
                            'tr:nth-child(3) > td > table > tbody > tr:nth-child(1) > td > div > ul > li')
    noodles = []
    for link in pasta_div:
        noodles.append(link.get_text('a'))

    return noodles


def get_central_asian_turkic():
    pasta_div = soup.select('#mw-content-text > div.mw-parser-output > div:nth-child(27) > table > tbody > '
                            'tr:nth-child(3) > td > table > tbody > tr:nth-child(2) > td > div > ul > li')
    noodles = []
    for link in pasta_div:
        noodles.append(link.get_text('a'))

    return noodles


def get_chinese():
    pasta_div = soup.select('#mw-content-text > div.mw-parser-output > div:nth-child(27) > table > tbody > '
                            'tr:nth-child(3) > td > table > tbody > tr:nth-child(3) > td > div > ul > li')
    noodles = []
    for link in pasta_div:
        noodles.append(link.get_text('a'))

    return noodles


def get_japanese():
    pasta_div = soup.select('#mw-content-text > div.mw-parser-output > div:nth-child(27) > table > tbody > '
                            'tr:nth-child(3) > td > table > tbody > tr:nth-child(4) > td > div > ul > li')
    noodles = []
    for link in pasta_div:
        noodles.append(link.get_text('a'))

    return noodles


def get_korean():
    pasta_div = soup.select('#mw-content-text > div.mw-parser-output > div:nth-child(27) > table > tbody > '
                            'tr:nth-child(3) > td > table > tbody > tr:nth-child(5) > td > div > ul > li')
    noodles = []
    for link in pasta_div:
        noodles.append(link.get_text('a'))

    return noodles


def get_filipino():
    pasta_div = soup.select('#mw-content-text > div.mw-parser-output > div:nth-child(27) > table > tbody > '
                            'tr:nth-child(3) > td > table > tbody > tr:nth-child(6) > td > div > ul > li')
    noodles = []
    for link in pasta_div:
        noodles.append(link.get_text('a'))

    return noodles


def get_thai():
    pasta_div = soup.select('#mw-content-text > div.mw-parser-output > div:nth-child(27) > table > tbody > '
                            'tr:nth-child(3) > td > table > tbody > tr:nth-child(7) > td > div > ul > li')
    noodles = []
    for link in pasta_div:
        noodles.append(link.get_text('a'))

    return noodles


def get_vietnamese():
    pasta_div = soup.select('#mw-content-text > div.mw-parser-output > div:nth-child(27) > table > tbody > '
                            'tr:nth-child(3) > td > table > tbody > tr:nth-child(8) > td > div > ul > li')
    noodles = []
    for link in pasta_div:
        noodles.append(link.get_text('a'))

    return noodles


def get_indonesian():
    pasta_div = soup.select('#mw-content-text > div.mw-parser-output > div:nth-child(27) > table > tbody > '
                            'tr:nth-child(3) > td > table > tbody > tr:nth-child(9) > td > div > ul > li')
    noodles = []
    for link in pasta_div:
        noodles.append(link.get_text('a'))

    return noodles


def get_malaysian_singaporean():
    pasta_div = soup.select('#mw-content-text > div.mw-parser-output > div:nth-child(27) > table > tbody > '
                            'tr:nth-child(3) > td > table > tbody > tr:nth-child(10) > td > div > ul > li')
    noodles = []
    for link in pasta_div:
        noodles.append(link.get_text('a'))

    return noodles
