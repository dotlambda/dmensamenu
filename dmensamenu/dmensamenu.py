import argparse
from argparse import RawTextHelpFormatter
import requests
import os
from subprocess import Popen, PIPE
import sys

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
    return meals

def formatmenu(meals):
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
        if maxpricelen == 0: # if no menu entry has a price
            del meal[1]
        else:
            meal[1] = ' ' * (maxpricelen - len(meal[1])) + meal[1] # right-align prices
        if maxcategorylen == 0: # if no menu entry has a category
            del meal[0]
        else:
            meal[0] += ' ' * (maxcategorylen - len(meal[0]))
    return ['  '.join(meal) for meal in menu]

def showmenu(menu, dmenu):
    env = os.environ.copy()
    env['lines'] = str(len(menu))
    p = Popen(dmenu, stdout=PIPE, stdin=PIPE, shell=True, env=env)
    selected, err = p.communicate(input=str.encode('\n'.join(menu)))

def getcanteens(ids):
    canteens = []
    nextlink = 'http://openmensa.org/api/v2/canteens?page=1'
    while True:
        req = requests.get(nextlink)
        if ids:
            for canteen in req.json():
                if canteen['id'] in ids:
                    canteens.append(canteen)
        else:
            canteens += req.json()

        links = requests.utils.parse_header_links(req.headers['link'])
        nextlink = None
        for link in links:
            if link['rel'] == 'next':
                nextlink = link['url']
        if nextlink is None:
            break
    return canteens

def showcanteens(canteens, dmenu, printid=False):
    env = os.environ.copy()
    env['lines'] = '0'
    p = Popen(dmenu, stdout=PIPE, stdin=PIPE, shell=True, env=env)
    selected, err = p.communicate(input=str.encode('\n'.join(canteen['name'] for canteen in canteens)))

    name = selected.decode().strip()
    for canteen in canteens:
        if canteen['name'] == name:
            if printid:
                print(canteen['id'])
            return canteen['id']

def main():
    parser = argparse.ArgumentParser(description='Show today\'s canteen menu.', add_help=False)
    parser.add_argument('id', type=int, nargs='*',
                        help='Openmensa.org canteen ID.'
                            +' If no ID is given, a menu for selecting from available canteens is shown.'
                            +' If multiple IDs are given, only those will be available for selection.')
    parser.add_argument('-s', '--search', action='store_true',
                        help='Search for a canteen.'
                            +'\nThe selected canteen\'s ID will be printed to stdout.')
    parser.add_argument('--dmenu', metavar='cmd', default='dmenu -i -l $lines',
                        help='Command to execute instead of \'dmenu -i -l $lines\'.'
                            +' Can be used to pass custom parameters to dmenu.'
                            +' The shell variable $lines will be set to the number of items on the menu.')
    parser.add_argument('-v', '--version', action='version',
                        version='dmensamenu-0.0.1', help="Show version number and exit.")
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help='Show this help message and exit.')
    args = parser.parse_args()

    if len(args.id) != 1:
        canteens = getcanteens(args.id)
        canteen = showcanteens(canteens, args.dmenu, args.search)
    else:
        canteen = args.id[0]
    if canteen is not None and not args.search:
        meals = getmenu(canteen)
        menu = formatmenu(meals)
        showmenu(menu, args.dmenu)
    
if __name__ == '__main__':
    main()
