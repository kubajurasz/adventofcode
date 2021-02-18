def load_data():
    with open("data/day14.txt", "r") as file:
        data = file.read()
    ret, temp = [], []
    for line in data.splitlines():
        line = line.strip().split(' ')
        if line[0] == 'mask' and temp == []:
            temp.append([line[2]])
        elif line[0] == 'mask' and temp != []:
            ret.append(temp)
            temp = [[line[2]]]
        else:
            temp.append([int(line[0][4:-1]), int(line[2])])
    ret.append(temp)
    return ret


def mask_on(mask, numba):
    return ''.join(numba[i] if mask[i] == 'X' else mask[i] for i in range(0, len(numba)))


def zad14a():
    data = load_data()
    addresses = []
    values_in_addresses = []
    for line in data:
        for i in line[1:]:
            if i[0] in addresses:
                values_in_addresses[addresses.index(i[0])] = int(mask_on(line[0][0], format(i[1], '#038b')[2:]), 2)
            else:
                addresses.append(i[0])
                values_in_addresses.append(int(mask_on(line[0][0], format(i[1], '#038b')[2:]), 2))

    return sum(values_in_addresses)


def write_to_addresses(address, mask):
    result = [''.join(mask[i] if mask[i] == 'X' or mask[i] == '1' else address[i] for i in range(0, len(address)))]
    exes = [i for i, e in enumerate(result[0]) if e == 'X']
    for x in exes:
        result = replace_exes(result, x)
    return result


def replace_exes(addresses, x):
    ret = []
    for address in addresses:
        temp = [list(address), list(address)]
        temp[0][x] = '0'
        temp[1][x] = '1'
        temp2 = [''.join(temp[0]), ''.join(temp[1])]
        ret += temp2
    return ret


def zad14b():
    data = load_data()
    addresses = []
    values_in_addresses = []
    for line in data:
        for i in line[1:]:
            for address in write_to_addresses(format(i[0], '#038b')[2:], line[0][0]):
                if address in addresses:
                    values_in_addresses[addresses.index(address)] = i[1]
                else:
                    addresses.append(address)
                    values_in_addresses.append(i[1])

    return sum(values_in_addresses)


print("Zad 1: {}\nZad 2: {}".format(zad14a(), zad14b()))
