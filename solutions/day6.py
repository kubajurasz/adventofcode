import string


def load_data():
    with open("data/day6.txt", "r") as file:
        data = file.read()
    temp, ret = '', []
    for line in data.splitlines():
        if line == '':
            ret.append(temp)
            temp = ''
        else:
            temp += line.strip()
    return ret


def zad6a():
    data = load_data()
    sum_of_counts = 0
    for line in data:
        line = "".join(set(line))
        sum_of_counts += len(line)
    return sum_of_counts


def load_data2():
    with open("data/day6.txt", "r") as file:
        data = file.read()
    temp, ret = [], []
    for line in data.splitlines():
        if line == '':
            ret.append(temp)
            temp = []
        else:
            temp += [line.strip()]
    return ret


def zad6b():
    data = load_data2()
    alphabet = string.ascii_lowercase
    counter = 0
    for group in data:
        letters = ''
        for line in group:
            line = "".join(set(line))
            letters += line
        for letter in alphabet:
            if letters.count(letter) == len(group):
                counter += 1
    return counter


print("Zad 1: {}\nZad 2: {}".format(zad6a(), zad6b()))
