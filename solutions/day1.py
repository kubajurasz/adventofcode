def load_data(file):
    with open(file) as file:
        data = [int(line.strip().split(",")[0]) for line in file]
    return data


def zad_1a():
    numbers = load_data("data/day1.csv")

    for i in numbers:
        for j in numbers:
            if i + j == 2020:
                print(i * j)


def zad_1b():
    numbers = load_data("data/day1.csv")

    for i in numbers:
        for j in numbers:
            for k in numbers:
                if i + j + k == 2020:
                    print(i * j * k)


zad_1a()
zad_1b()
