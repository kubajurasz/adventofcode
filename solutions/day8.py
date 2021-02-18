def load_data_zad8():
    with open("data/day8.txt", "r") as file:
        data = file.read()
    ret = []
    for line in data.splitlines():
        ret.append(line.strip().split(' '))
    return ret


def zad8(data):
    visited_indices = []
    current_index = 0
    accumulator = 0
    while (current_index not in visited_indices) and (current_index < len(data)):
        visited_indices.append(current_index)
        if data[current_index][0] == 'jmp':
            current_index += int(data[current_index][1])
        elif data[current_index][0] == 'acc':
            accumulator += int(data[current_index][1])
            current_index += 1
        else:
            current_index += 1
    return [accumulator, current_index]


def zad8a():
    data = load_data_zad8()
    return zad8(data)[0]


def zad8b():
    data = load_data_zad8()
    for i in range(len(data)):
        if data[i][0] == 'jmp':
            data[i][0] = 'nop'
            result = zad8(data)
            if result[1] >= len(data):
                return result[0]
            else:
                data[i][0] = 'jmp'
        elif data[i][0] == 'nop':
            data[i][0] = 'jmp'
            result = zad8(data)
            if result[1] >= len(data):
                return result[0]
            else:
                data[i][0] = 'nop'
    return ['invalid data']


print("Zad 1: {}\nZad 2: {}".format(zad8a(), zad8b()))
