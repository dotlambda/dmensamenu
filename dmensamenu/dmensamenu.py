import argparse
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
from subprocess import Popen, PIPE

CANTEENS = {
    'INF': 'Mensa Im Neuenheimer Feld 304',
    'Marstall': 'zeughaus-Mensa im Marstall',
    'Triplex': 'Triplex-Mensa am Uniplatz'
}

CLOSING = {
    'INF': 14,
    'Marstall': 22,
    'Triplex': 14
}

def getmeals(canteen, day):
    meals = []
    maxoutlen = 0
    maxpricelen = 0

    page = requests.get('http://stw.uni-heidelberg.de/de/speiseplan').text
    html = BeautifulSoup(page, 'html.parser')
    h2 = html.body.find('h2', text=CANTEENS[canteen])
    for h4 in h2.find_next_sibling('div').find_all('h4'):
        if datetime.strptime(h4.text.split(' ')[1], '%d.%m.%Y').date() == day:
            for tr in h4.next_sibling.find_all('tr'):
                tds = tr.find_all('td')
                if tds:
                    meal = ' '.join(tds[0].text.split()) # replace any whitespaces by a single ' '
                    out = tds[1].text
                    price = tds[2].text + '€'

                    maxoutlen = max(maxoutlen, len(out))
                    maxpricelen = max(maxpricelen, len(price))

                    meals.append([out, price, meal])

    for meal in meals:
        meal[0] += ' ' * (maxoutlen - len(meal[0]))
        meal[1] += ' ' * (maxpricelen - len(meal[1]))
    return ['  '.join(meal) for meal in meals]

def showmeals(canteen, day, meals, dmenuargs):
    # remaining command line args are passed to dmenu
    p = Popen(['dmenu', '-p', canteen + ' ' + day.strftime('%d.%m.%Y'), '-l', str(len(meals))] + dmenuargs, stdin=PIPE)
    p.communicate(input=str.encode('\n'.join(meals)))

def main():
    parser = argparse.ArgumentParser(description='Show today\'s canteen menu.')
    parser.add_argument('canteen', type=str,
                        help='the canteen whose menu to show',
                        choices=['INF', 'Marstall', 'Triplex'])
    parser.add_argument('dmenuargs', metavar='...', nargs=argparse.REMAINDER,
                        help='Any additional arguments are passed on to dmenu.')
    args = parser.parse_args()

    daytoshow = date.today()
    if datetime.now().hour >= CLOSING[args.canteen]: # if canteen is already closed, show tomorrow's menu instead
        daytoshow += timedelta(days=1)

    meals = getmeals(args.canteen, daytoshow)
    showmeals(args.canteen, daytoshow, meals, args.dmenuargs)

if __name__ == '__main__':
    main()
