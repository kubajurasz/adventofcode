import copy


def load_data():
    with open("data/day11.txt", "r") as file:
        data = file.read()

    return [[i for i in line.strip()] for line in data.splitlines()]


def add_offset(data):
    dupsko = [['x' for _ in range(len(data[0]) + 2)]]
    for line in data:
        dupsko.append(['x'] + line + ['x'])
    dupsko.append(['x' for _ in range(len(data[0]) + 2)])
    return dupsko


def check_neighbors(data, i, j):
    return (data[i][j:j+3] + [data[i + 1][j]] + [data[i + 1][j + 2]] + data[i + 2][j:j+3]).count('#')


def zad11a():
    data = load_data()
    data = add_offset(data)
    change = True
    while change:
        change = False
        temp = []
        for i in range(0, len(data) - 2):
            dupsko = []
            for j in range(0, len(data[i]) - 2):
                if (check_neighbors(data, i, j) == 0) and (data[i + 1][j + 1] == 'L'):
                    dupsko.append('#')
                    change = True
                elif (check_neighbors(data, i, j) > 3) and (data[i + 1][j + 1] == '#'):
                    dupsko.append('L')
                    change = True
                else:
                    dupsko.append(data[i + 1][j + 1])

            temp.append(dupsko)

        data = add_offset(temp)

    counter = 0
    for line in data:
        counter += line.count('#')
    return counter


def is_empty(data, position):
    directions = [[0, 1], [1, -1], [1, 0], [1, 1], [-1, -1], [-1, 0], [-1, 1], [0, -1]]
    taken = False
    for direction in directions:
        i = position[0]
        j = position[1]

        empty_path = True
        while 0 <= i < len(data) and 0 <= j < len(data[0]) and empty_path:
            if data[i][j] == 'L' and not (i == position[0] and j == position[1]):
                empty_path = False
            elif data[i][j] == '#' and not (i == position[0] and j == position[1]):
                taken = True

            i += direction[0]
            j += direction[1]

    return taken


def is_taken(data, position):
    directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    counter = 0
    for direction in directions:
        i = position[0]
        j = position[1]
        clear = True
        while 0 <= i < len(data) and 0 <= j < len(data[0]) and clear:
            if data[i][j] == '#' and not (i == position[0] and j == position[1]):
                counter += 1
                clear = False
            elif data[i][j] == 'L' and not (i == position[0] and j == position[1]):
                clear = False
            i += direction[0]
            j += direction[1]

    return True if counter > 4 else False


def zad11b():
    data = load_data()
    change = True
    while change:
        change = False
        new_data = []
        for i in range(0, len(data)):
            temp = []
            for j in range(0, len(data[0])):
                if data[i][j] == 'L' and not is_empty(data, [i, j]):
                    temp.append('#')
                    change = True
                elif data[i][j] == '#' and is_taken(data, [i, j]):
                    temp.append('L')
                    change = True
                else:
                    temp.append(data[i][j])
            new_data.append(temp)

        data = copy.deepcopy(new_data)

    counter = 0
    for line in data:
        counter += line.count('#')
    return counter


print("Zad 1: {}\nZad 2: {}".format(zad11a(), zad11b()))
