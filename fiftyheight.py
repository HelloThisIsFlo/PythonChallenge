from PIL import Image


def solve():
    with Image.open(r'./files/cave.jpg') as image:
        # image.show()
        width = image.size[0]
        height = image.size[1]

        # Create the new image with the extracted pixels
        new_image = Image.new(image.mode, (int(width/2), height))
        pixels = list()
        for j in range(0, height):
            if j % 2 == 0:
                # Extract subpixel starting with the first pixel of the line
                line = [image.getpixel((i, j)) for i in range(0, width, 2)]
                print(len(pixels))
            else:
                # Extract subpixel starting with the second pixel of the line
                line = [image.getpixel((i, j)) for i in range(1, width, 2)]
                print(len(pixels))
            pixels = pixels + line

        new_image.putdata(pixels)
        new_image.show()

