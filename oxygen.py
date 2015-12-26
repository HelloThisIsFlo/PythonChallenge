from PIL import Image
from urllib.request import urlopen
import itertools
import re


def solve():
    with urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png') as raw_image:
        image = Image.open(raw_image)
        image, _, _, _ = image.split()  # Keep only red band, since values are grey

        # Get the middle pixel line
        width, height = image.size
        mid_h = int(height / 2)

        # The first version used groupby to remove sequential repetition of values, the problem is that for char that
        # are repeated it doesn't work anymore (removes the repeated characters). So I manually found the ammount of
        # pixels per grey band : 7
        pixels = [image.getpixel((i, mid_h)) for i in range(0, width, 7)]

        # Convert to ascii
        print(''.join(map(chr, pixels)))

        # Result from the first run ;)
        test = [105, 110, 116, 101, 103, 114, 105, 116, 121]
        print()
        print('Result : ')
        print(''.join(map(chr, test)))
