from itertools import islice
import time


def new_number(numbers):
    last_number = numbers[-1]
    if last_number in numbers[:-1]:
        return len(numbers) - 1 - max(loc for loc, val in enumerate(numbers[:-1]) if val == last_number)
    else:
        return 0


def zad15a():
    with open("data/day15.txt", "r") as file:
        numbers = [int(i) for i in file.read().splitlines()[0].split(',')]
    while len(numbers) < 2020:
        numbers.append(new_number(numbers))
    return numbers[-1]


def zad15b():
    n, seen, val = 5, {1: 0, 0: 1, 18: 2, 10: 3, 19: 4}, 6
    while True:
        yield val
        last = {val: n}
        val = n - seen.get(val, n)
        seen.update(last)
        n += 1


print("Zad 1: {}\nZad 2: {}".format(zad15a(), list(islice(zad15b(), 30000000))[-6]))
