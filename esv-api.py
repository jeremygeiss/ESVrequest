#!/usr/bin/env python3

import sys
import requests


API_KEY = '<YOUR API KEY>'
API_URL = 'https://api.esv.org/v3/passage/text/'


def get_esv_text(passage):
    params = {
        'q': passage,
        'include-headings': True,
        'include-footnotes': False,
        'include-verse-numbers': True,
        'include-short-copyright': True,
        'include-passage-references': True
    }

    headers = {
        'Authorization': 'Token %s' % API_KEY
    }

    response = requests.get(API_URL, params=params, headers=headers)

    passages = response.json()['passages']

    return passages[0].strip() if passages else 'Error: Passage not found'


if __name__ == '__main__':
    passage = ' '.join(sys.argv[1:])

    if passage:
        print(get_esv_text(passage))
