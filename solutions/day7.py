def load_data():
    with open("data/day7.txt", "r") as file:
        data = file.read()
    ret, temp = [], []
    for line in data.splitlines():
        temp.append(line.strip().split(" "))
    for line in temp:
        ind = [i for i, j in enumerate(line) if 'bag' in j]
        ret.append([line[i - 2:i] for i in ind])
    return ret


class Color:
    def __init__(self, color, colors):
        self.color = color
        self.contains = colors


def zad7a():
    data = load_data()
    colors = []
    for line in data:
        colors.append(Color(line[0], line[0:]))
    valid = [['shiny', 'gold']]
    added = True
    while added:
        added = False
        for color in colors:
            if any(item in valid for item in color.contains) and color.color not in valid:
                added = True
                valid.append(color.color)
    return len(valid) - 1


def load_data2():
    with open("data/day7.txt", "r") as file:
        data = file.read()
    ret, temp = [], []
    for line in data.splitlines():
        temp.append(line.strip().split(" "))
    for line in temp:
        ind = [i for i, j in enumerate(line) if 'bag' in j]
        ret.append([line[0:2]] + [line[ind[i] - 3:ind[i]] for i in range(1, len(ind))])
    return ret


def so_recursive(colors, color):
    bags = 1
    if color.contains == [['contain', 'no', 'other']]:
        return bags
    else:
        for bag in color.contains:
            for another_color in colors:
                if another_color.color == [bag[1], bag[2]]:
                    bags += int(bag[0]) * so_recursive(colors, another_color)

        return bags


def zad7b():
    data = load_data2()
    colors = []
    bags = 0
    for line in data:
        colors.append(Color(line[0], line[1:]))
    for color in colors:
        if color.color == ['shiny', 'gold']:
            bags = so_recursive(colors, color) - 1
    return bags


print("Zad 1: {}\nZad 2: {}".format(zad7a(), zad7b()))
