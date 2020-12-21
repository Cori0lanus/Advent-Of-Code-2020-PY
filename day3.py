def calcSlope(lines, xOff, yOff):
    correct = 0
    x = 0
    for i in range(0, len(lines), yOff):
        if lines[i][x] == '#':
            correct += 1
        x += xOff
        x %= len(lines[0]) - 1

    return correct


def sol1():
    lines = open('input/day3.txt').readlines()

    return calcSlope(lines, 3, 1)


def sol2():
    lines = open('input/day3.txt').readlines()

    return calcSlope(lines, 1, 1) * calcSlope(lines, 3, 1) * calcSlope(lines, 5, 1) * calcSlope(lines, 7, 1) * \
        calcSlope(lines, 1, 2)
