import re
import ocr


def find_vip():
    with open(r'files/equality') as file:
        equality = file.read()

        # Find the vips
        with_bodyguard = re.findall('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', equality)
        list_vips = list()
        for vip in with_bodyguard:
            print(vip)
            list_vips.append(vip[4])

        print(ocr.find_permut_english(list_vips))


def find_vip_better():
    with open(r'files/equality') as file:
        equality = file.read()
        # Better version
        print(''.join(re.findall('[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', equality)))

