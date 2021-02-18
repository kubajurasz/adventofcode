def load_data():
    with open("data/day13.txt", "r") as file:
        data = file.read()
    return int(data.splitlines()[0]), data.splitlines()[1].split(',')


def zad13a():
    timestamp, buses = load_data()
    winner_time, winner_id = 100000, 1000000
    for bus in buses:
        if bus != 'x':
            bus_id = int(bus)
            time = bus_id - timestamp % bus_id
            if time < winner_time:
                winner_time = time
                winner_id = bus_id
    return winner_time * winner_id


def load_data2():
    with open("data/day13.txt", "r") as file:
        data = file.read()
    return data.splitlines()[1].split(',')


def zad13b():
    data = load_data2()
    buses = []
    for i in range(0, len(data)):
        if data[i] != 'x':
            buses.append([i, int(data[i])])
    timestamp = 0
    increment = buses[0][1]
    for i in range(1, len(buses)):
        val_timestamp = False
        while not val_timestamp:
            if all([(timestamp + bus[0]) % bus[1] == 0 for bus in buses[0:i + 1]]):
                val_timestamp = True
                increment *= buses[i][1]
            else:
                timestamp += increment
    return timestamp


print("Zad 1: {}\nZad 2: {}".format(zad13a(), zad13b()))
