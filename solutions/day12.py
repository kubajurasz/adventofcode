import math
import numpy as np


def load_data():
    with open("data/day12.txt", "r") as file:
        data = file.read()

    return [[line[0], int(line[1:])]for line in data.splitlines()]


def zad12a():
    pos = [0, 0]
    direction = -90     # deg from x axis counterclockwise, west is x axis, north is y axis
    instructions = load_data()
    for instruction in instructions:
        if instruction[0] == 'R':
            direction += instruction[1]
        elif instruction[0] == 'L':
            direction -= instruction[1]
        elif instruction[0] == 'F':
            pos[0] += math.cos(math.radians(direction)) * instruction[1]
            pos[1] += math.sin(math.radians(direction)) * instruction[1]
        elif instruction[0] == 'N':
            pos[1] += instruction[1]
        elif instruction[0] == 'S':
            pos[1] -= instruction[1]
        elif instruction[0] == 'E':
            pos[0] += instruction[1]
        elif instruction[0] == 'W':
            pos[0] -= instruction[1]

    return abs(pos[0]) + abs(pos[1])


def zad12b():
    pos = np.array([0, 0])
    waypoint = np.array([10, 1])

    instructions = load_data()
    for instruction in instructions:
        if instruction[0] == 'R':
            mag = np.linalg.norm(waypoint)
            alpha = math.atan2(waypoint[1], waypoint[0])
            waypoint = np.array([mag * math.cos(- math.radians(instruction[1]) + alpha), mag * math.sin(- math.radians(instruction[1]) + alpha)])
        elif instruction[0] == 'L':
            mag = np.linalg.norm(waypoint)
            alpha = math.atan2(waypoint[1], waypoint[0])
            waypoint = np.array([mag * math.cos(math.radians(instruction[1]) + alpha), mag * math.sin(math.radians(instruction[1]) + alpha)])
        elif instruction[0] == 'F':
            pos = pos + waypoint * instruction[1]
        elif instruction[0] == 'N':
            waypoint[1] += instruction[1]
        elif instruction[0] == 'S':
            waypoint[1] -= instruction[1]
        elif instruction[0] == 'E':
            waypoint[0] += instruction[1]
        elif instruction[0] == 'W':
            waypoint[0] -= instruction[1]

    return abs(pos[0]) + abs(pos[1])


print("Zad 1: {}\nZad 2: {}".format(zad12a(), zad12b()))
