'''Python Program to scrap downdetector site find status'''

import requests
from bs4 import BeautifulSoup


def downdetector(link):
    '''Function that displays the status of a site.
    Args: link
    returns: status of the site
    '''

    if requests.get(link):  # checks for the site name
        res = requests.get(link)
        soup = BeautifulSoup(res.text, 'html.parser')
        results = soup.find('div', class_='h2 entry-title')
        print(results.text)  # prints the status of the site

    else:
        print('Site could not be found')


if __name__ == '__main__':
    # user input site name
    site_name = str(input('Enter the name of the site to find status for:'))
    link = 'https://downdetector.in/status/' + site_name
    downdetector(link)
