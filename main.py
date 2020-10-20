from pastas import get_random_pasta, cant_decide, get_list_of_pastas, unique_pasta_chooser, append_pasta_list
from asian_noodles import *

# This script uses the BeautifulSoup library to scrape the Wikipedia page of pasta/noodle 
# dishes, and lets you choose a random dish based on some prompts

__author__ = 'Judson King'
__credits__ = ['Judson King', 'Wikipedia', 'Pasta']
__license__ = 'idc do what you want with it'
__email__ = 'judking@protonmail.ch'
__status__ = 'meh at best'


noodle_banner = open('noods.txt', 'r')
file_content = noodle_banner.read()
print(file_content)
noodle_banner.close()

print(f'\nWelcome to the Random Pasta Generator! Or, RPG for short (unrelated to the big boom stick)')
print('Basically there are two types of dishes here: Western (mostly Italian) and East Asian\n')

control = True
first_time = True

while control != False:
  west_or_east = input('Type \'1\' for Western, \'2\' for Asian, and \'3\' if you can\'t decide: ')

  if west_or_east == '1':
      print()
      if (first_time == True):
        pasta = get_random_pasta() 
        append_pasta_list(pasta)
        print(f'Your mystery pasta is {pasta} !!!\n')
      else:
        unique_pasta_chooser()
  elif west_or_east == '2':
      print('\nSo there are a TON of different (mostly East) Asian Noodle dishes listed on Wiki. If you want a truly \nrandom dish, '
            'then indicate that. Else, I\'ll display all the regions, and you can choose \nthe region you want '
            'your noodles from.\n')
      choice_1 = input('If you want a random dish, type 1, if you want to choose a region, type 2: ')
      print()

      if choice_1 == '1':
          get_random_noodles()
      elif choice_1 == '2':
          display_regions()
          print()

          choice_2 = input('Choose the number of the region you want (i.e.: type \'1\' for Burmese): ')

          get_region_noodles(choice_2)
      else:
          print('Sorry, didn\'t understand that, try again\n')
  elif west_or_east == '3':
      r = cant_decide()
      if r == '1':
        print('\nSince you couldn\'t decide, I decided for you: Italian!\n')
        if (first_time == True):
          pasta = get_random_pasta() 
          append_pasta_list(pasta)
          print(f'Your mystery pasta is {pasta} !!!\n')
        else:
          unique_pasta_chooser()
      elif r == '2':
          print('\nSince you couldn\'t decide, I decided for you: Asian!\n')
          print(
              '\nSo there are a TON of different Asian Noodle dishes listed on Wiki. If you want a truly \nrandom dish, '
              'then indicate that. Else, I\'ll display all the regions, and you can choose \nthe region you want '
              'your noodles from.\n')
          choice_1 = input('If you want a random dish, type 1, if you want to choose a region, type 2: ')
          print()

          if choice_1 == '1':
              get_random_noodles()
          elif choice_1 == '2':
              display_regions()
              print()

              choice_2 = input('Choose the number of the region you want (i.e.: type \'1\' for Burmese): ')

              get_region_noodles(choice_2)
  else:
      print('Sorry, didn\'t understand that, try again\n')

  choice_3 = input('Do you want to generate another random pasta/noodle dish? (y/n): ')
  print()
  if choice_3.lower() == 'y':
      first_time = False
      continue
  elif choice_3.lower() == 'n':
      print('Bye :)')
      control = False
  else:
      print('Sorry, didn\'t understand that, try again')
