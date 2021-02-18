def load_data():
    with open("data/day4.txt", "r") as file:
        data = file.read()
    temp, ret = [], []
    for line in data.splitlines():
        if line == '':
            ret.append([elem.split(":") for elem in temp])
            temp = []
        else:
            temp += line.strip().split(" ")
    return ret


def zad4a():
    dat = load_data()

    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_passports = 0

    for line in dat:
        if all(item in [elem[0] for elem in line] for item in fields):
            valid_passports += 1

    return valid_passports


def zad4b():
    dat = load_data()

    field = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']

    valid_passports = 0

    for line in dat:
        line.sort(key=lambda x: x[0])
        for elem in line:
            if elem[0] == "cid":
                line.remove(elem)

        if all(item in [elem[0] for elem in line] for item in field):
            byr, ecl, eyr, hcl, hgt, iyr, pid = [elem[1] for elem in line]
            rules = [len(byr) == 4 and byr.isdigit() and 1920 <= int(byr) <= 2002, ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
                     len(eyr) == 4 and eyr.isdigit() and 2020 <= int(eyr) <= 2030,
                     len(hcl) == 7 and hcl[0] == '#' and all([c.isdigit() or 'a' <= c <= 'f' for c in hcl[1:7]]),
                     (hgt[-2:] == 'cm' and hgt[:-2].isdigit() and 150 <= int(hgt[:-2]) <= 193) or
                     (hgt[-2:] == 'in' and hgt[:-2].isdigit() and 59 <= int(hgt[:-2]) <= 76),
                     len(iyr) == 4 and iyr.isdigit() and 2010 <= int(iyr) <= 2020,
                     len(pid) == 9 and byr.isdigit()]
            if all(rules):
                valid_passports += 1

    return valid_passports


print("Zad 1: {}\nZad 2: {}".format(zad4a(), zad4b()))
