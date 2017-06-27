import argparse
from argparse import RawTextHelpFormatter
import requests
import os
from subprocess import Popen, PIPE

def getmenu(canteen, day=None):
    if day is None:
        days = requests.get('http://openmensa.org/api/v2/canteens/{}/days'.format(canteen)).json()
        for day_ in days:
            if day_['closed'] == False:
                daystring = day_['date']
                break
    else:
        daystring = day.strftime('%Y-%m-%d')
    meals = requests.get('http://openmensa.org/api/v2/canteens/{}/days/{}/meals'.format(canteen, daystring)).json()

    menu = []
    maxcategorylen = 0
    maxpricelen = 0
    for meal in meals:
        price = '' if meal['prices']['students'] is None else '{:.2f}€'.format(meal['prices']['students'])
        name = ' '.join(meal['name'].split())
        menu.append([meal['category'], price, name])
        maxcategorylen = max(maxcategorylen, len(meal['category']))
        maxpricelen = max(maxpricelen, len(price))

    for meal in menu:
        meal[0] += ' ' * (maxcategorylen - len(meal[0]))
        meal[1] += ' ' * (maxpricelen - len(meal[1]))
    return ['  '.join(meal) for meal in menu]

def showmeals(menu, dmenu):
    env = os.environ.copy()
    env['lines'] = str(len(menu))
    p = Popen(dmenu, stdin=PIPE, shell=True, env=env)
    p.communicate(input=str.encode('\n'.join(menu)))

def main():
    parser = argparse.ArgumentParser(description='Show today\'s canteen menu.',
                                     formatter_class=RawTextHelpFormatter)
    parser.add_argument('id', type=int, #nargs=argparse.REMAINDER,
                        help='openmensa.org canteen ID')
    parser.add_argument('--dmenu', metavar='cmd', default='dmenu -l $lines',
                        help='execute cmd instead of \'dmenu\','
                        + ' can be used to pass custom parameters to dmenu\n'
                        + 'the shell variable $lines will be set to the number of lines in the menu')
    args = parser.parse_args()

    menu = getmenu(args.id)
    showmeals(menu, args.dmenu)
    
if __name__ == '__main__':
    main()
