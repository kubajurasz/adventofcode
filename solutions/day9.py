def load_data():
    with open("data/day9.txt", "r") as file:
        data = file.read()

    return [int(line.strip()) for line in data.splitlines()]


def number_valid(preamble, number):
    for i in range(len(preamble)):
        for j in range(len(preamble)):
            if i != j and preamble[i] + preamble[j] == number:
                return True
    return False


def zad9a():
    data = load_data()
    for i in range(26, len(data)):
        if not number_valid(data[i - 26:i - 1], data[i - 1]):
            return data[i - 1]
    return 0


def zad9b():
    data = load_data()
    invalid_number = 507622668
    for i in range(0, len(data)):
        sum_of_sublist = 0
        j = i
        while sum_of_sublist < invalid_number and j < len(data):
            sum_of_sublist += data[j]
            j += 1
            if sum_of_sublist == invalid_number:
                return min(data[i:j + 1]) + max(data[i:j + 1])

    return 0

print("Zad 1: {}\nZad 2: {}".format(zad9a(), zad9b()))
