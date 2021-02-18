def load_data2(file):
    data = []
    with open(file) as file:
        for line in file:
            temp = line.strip().split(" ")
            temp = [int(temp[0].split("-")[0]), int(temp[0].split("-")[1]), temp[1][0], temp[2]]
            data.append(temp)
    return data


def zad_2a():
    data = load_data2("data/day2.csv")
    counter = 0
    for i in data:
        if i[0] <= i[3].count(i[2]) <= i[1]:
            counter += 1

    print(counter)



def zad_2b():
    data = load_data2("data/day2.csv")
    counter = 0

    for i in data:
        if (i[3][i[0] - 1] == i[2] and i[3][i[1] - 1] != i[2]) or (i[3][i[0] - 1] != i[2] and i[3][i[1] - 1] == i[2]):
            counter += 1
    print(counter)


zad_2a()
zad_2b()
