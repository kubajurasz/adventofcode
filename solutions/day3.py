def load_data(file):
    with open(file) as file:
        data = [line.strip().split(",") for line in file]
    return data


def zad_3a():
    data = load_data("data/day3.csv")
    counter = 0
    for i in range(0, len(data)):
        if data[i][0][(i * 3) % len(data[i][0])] == "#":
            counter += 1
    return counter


def zad_3b():
    data = load_data("data/day3.csv")
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    ans = 1

    for slope in slopes:
        i, j = 0, 0
        counter = 0
        while i < len(data):
            if data[i][0][j] == '#':
                counter += 1
            i += slope[1]
            j = (j + slope[0]) % len(data[0][0])

        ans *= counter
    
    return ans


print("Zad 1: {}\nZad 2: {}".format(zad_3a(), zad_3b()))
