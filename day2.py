def sol1():
    lines = open('input/day2.txt').readlines()

    correct = 0

    for line in lines:
        split = line.split(' ')
        leftNum = int(split[0].split('-')[0])
        rightNum = int(split[0].split('-')[1])

        char = split[1][0]

        string = split[2]

        if leftNum <= string.count(char) <= rightNum:
            correct += 1

    return correct


def sol2():
    lines = open('input/day2.txt').readlines()

    correct = 0

    for line in lines:
        split = line.split(' ')
        leftNum = int(split[0].split('-')[0])
        rightNum = int(split[0].split('-')[1])

        char = split[1][0]

        string = split[2]

        if (string[leftNum-1] == char) ^ (string[rightNum-1] == char):
            correct += 1

    return correct
