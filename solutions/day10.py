
def load_data():
    with open("data/day10.txt", "r") as file:
        data = file.read()

    return [int(line.strip()) for line in data.splitlines()]


def zad10a():
    data = sorted(load_data())
    data = [0] + data + [max(data) + 3]
    differences = [data[current_index + 1] - data[current_index] for current_index in range(0, len(data) - 1)]
    return differences.count(1) * differences.count(3)


def zad10b():
    data = sorted(load_data())
    data = [0] + data + [max(data) + 3]
    ways_from_vertex = [1, 1]
    for i in range(2, len(data)):
        new_vertex = ways_from_vertex[i - 1]
        if i - 2 >= 0 and data[i - 2] + 3 >= data[i]:
            new_vertex += ways_from_vertex[i - 2]
        if i - 3 >= 0 and data[i - 3] + 3 >= data[i]:
            new_vertex += ways_from_vertex[i - 3]
        ways_from_vertex.append(new_vertex)

    return ways_from_vertex[-1]


print("Zad 1: {}\nZad 2: {}".format(zad10a(), zad10b()))
