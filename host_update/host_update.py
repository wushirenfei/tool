# -*- coding=utf-8 -*-

import re
import requests
import pprint


def update_hosts(url=None):
    if not url:
        url = 'https://github.com/racaljk/hosts/blob/master/hosts'

        response = requests.get(url)

        res = re.findall(r'<td id="LC(.*)</td>', response.text)

        file = open('./hosts','w')
        for line in res:
            file.write('{}\n'.format(re.findall(r'>(.*)', line)[0]))
        file.flush()
        file.close()


if __name__ == '__main__':
    update_hosts()