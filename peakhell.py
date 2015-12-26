import pickle
from urllib.request import urlopen


def test_pickle():
    a = ['hello', 'ocucou', 'comment ca va ? ']

    with open(r'files/testfile', 'wb') as file:
        pickle.dump(a, file, protocol=0)


def deserialize():
    with urlopen("http://www.pythonchallenge.com/pc/def/banner.p") as webpage:
        data = pickle.load(webpage)

        for line in data:
            print(''.join(tuple[0] * tuple[1] for tuple in line))