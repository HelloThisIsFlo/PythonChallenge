from urllib.request import urlopen
import urllib.parse
import xml.dom.minidom as minidom
import xmlrpc.client


def solve():
    """
    The idea here is that phonebook.php is actualy a RPC api.
    Haha that was a rewarding level. With all these REST api I completely forgot about RPC. Lucky enough (as with
    everything apparently) it was easy enough in python

    The remote method is 'phone'
    From the previous level we know that "Bert" is evil
    """
    url = 'http://www.pythonchallenge.com/pc/phonebook.php'
    proxy = xmlrpc.client.ServerProxy(url)

    italy_digit = '58259'
    multicall = xmlrpc.client.MultiCall(proxy)
    multicall.system.listMethods()
    multicall.system.methodSignature('phone')
    multicall.system.methodHelp('phone')
    multicall.phone('Bert')
    multicall.phone('ITALY')
    multicall.phone('2378')
    for result in multicall():
        print(result)

    # Omg I'm stupid the solution was 'ITALY' ^_^


def temp_test():
    values = {'evil': 'Bert'}

    data = urllib.parse.urlencode(values).encode()
    with urlopen('http://www.pythonchallenge.com/pc/phonebook.php', data=data) as response:

        res_string = response.read().decode().replace('\n', '')
        xml = minidom.parseString(res_string)
        print(xml.toprettyxml())