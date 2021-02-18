def load_data(day):
    with open("data/day" + day + ".txt", "r") as file:
        data = file.read()
    return [line.strip() for line in data.splitlines()]


def zad5a():
    data = load_data("5")
    max_seat = 0
    for line in data:
        line = line.replace('F', '0')
        line = line.replace('B', '1')
        line = line.replace('R', '1')
        line = line.replace('L', '0')
        seat_id = int(line[:-3], 2) * 8 + int(line[-3:], 2)
        if seat_id > max_seat:
            max_seat = seat_id

    return max_seat


def zad5b():
    data = load_data("5")
    seats_ids = []
    for line in data:
        line = line.replace('F', '0')
        line = line.replace('B', '1')
        line = line.replace('R', '1')
        line = line.replace('L', '0')
        seats_ids.append(int(line[:-3], 2) * 8 + int(line[-3:], 2))
    seats_ids.sort()
    my_seat = 0
    for i in range(0, len(seats_ids) - 1):
        if seats_ids[i + 1] - seats_ids[i] > 1:
            my_seat = (seats_ids[i + 1] + seats_ids[i]) / 2
    return my_seat


print("Zad 1: {}\nZad 2: {}".format(zad5a(), zad5b()))
