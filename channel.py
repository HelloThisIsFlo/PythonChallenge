import re, os, zipfile


def solve():

    comments = build_comment_dict()

    string = go_deep(90052, comments)
    print(string)

    print('Note : solution is not hockey, but the letters composing it : oxygen!')


def go_deep(current, comments, string=None, counter=0):
    if string is None:
        string = str()

    # Generate path
    path = ''.join([r'files/channel/', str(current), '.txt'])

    with open(path) as current_file:
        line = current_file.readline()
        next_num = re.findall('[0-9]+$', line)
        if len(next_num) == 1:
            string = ''.join([string, comments.get(current, '')])
            string = go_deep(int(next_num[0]), comments, string, counter + 1)
        else:
            print(current_file)

    return string


def build_comment_dict():
    with zipfile.ZipFile(r'files/channel.zip') as zip_file:

        list_infos = zip_file.infolist()
        comment = dict()
        for file_info in list_infos:
            try:
                filename = file_info.filename
                file_number = int(filename[:len(filename) - 4])
                comment[file_number] = file_info.comment.decode()
            except ValueError:
                pass
        return comment


def build_file_list():
    path = r'files/channel/'
    listdir = os.listdir(path)
    result = list()
    for filename in listdir:
        try:
            result.append(int(filename[:len(filename) - 4]))
        except ValueError:
            pass
    return result


def simpler_version():
    pattern = re.compile('[0-9]+$')
    current_number = '90052'
    filename = '%s.txt'
    comments = list()

    with zipfile.ZipFile(r'files/channel.zip') as zip_file:
        while True:
            content = zip_file.read(filename % current_number).decode()
            match = pattern.search(content)
            if match is not None:
                # Add comment to the list
                comments.append(zip_file.getinfo(filename % current_number).comment.decode())

                # Update current number
                current_number = match.group(0)
            else:
                break

    print(''.join(comments))


'''
Ok, so first : Build the dictionary where everyfile is associated with his comment then display the comment

Try to do with double iteration : zipo method in python

'''