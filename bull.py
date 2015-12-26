import itertools


"""
    The hint here is : a = [1, 11, 21, 1211, 111221,
    This is a famous pattern. the second hint is : len(a[30]) = ?

    So let's try to generate a, at least to the 31th step
"""


def solve():
    a = generate_a(31)
    print(''.join(['The result is len(a[30]) = ', str(len(a[30]))]))


def generate_next_step(current_step):
    # For every repetition save in a list :
    #   - The number of occurence of the figure
    #   - The figure
    # Then convert to a string
    next_step = list()
    for k, g in itertools.groupby(current_step):
        next_step.append(len(list(g)))
        next_step.append(k)

    return ''.join([str(i) for i in next_step])


def generate_a(length):
    current_step = '1'
    result = list()
    result.append(current_step)
    for i in range(1, length):
        current_step = generate_next_step(current_step)
        result.append(current_step)

    return result
