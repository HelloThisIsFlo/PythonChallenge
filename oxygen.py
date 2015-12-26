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
        pixels = list()
        for i in range(0, width):
            pixels.append(image.getpixel((i, mid_h)))

        # Curate the pixel list
        pixels_curated = [v for v, _ in itertools.groupby(pixels)]

        # Convert to ascii
        print(''.join(map(chr, pixels_curated)))

        test = [105, 10, 16, 101, 103, 14, 105, 16, 121]
        # test_bis = [chr(c) for c in test]
        print(''.join(map(chr, test)))
