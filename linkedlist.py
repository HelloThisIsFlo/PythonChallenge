from urllib.request import urlopen
from urllib.parse import urlencode
import re


def solve():
    go_deep(12345)


def go_deep(number):
    # Create url
    base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?"
    param = {'nothing': number}
    url = ''.join([base_url, urlencode(param)])

    with urlopen(url) as response:
        res_string = response.read()
        num_res = re.findall('[0-9]+$', res_string.decode())
        print(url)
        if len(num_res) == 1:
            go_deep(num_res[0])
        elif in_divide_step(res_string.decode()):
            go_deep(int(number) / 2)
        else:
            print(res_string.decode())


def in_divide_step(data):
    div = re.findall('Divide by two', data)
    if len(div) == 1:
        return True
    else:
        return False