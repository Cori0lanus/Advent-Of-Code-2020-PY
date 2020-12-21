def sol1():
    lines = open('input/day6.txt').read()

    groups = [group.split('\n') for group in lines.split('\n\n')]

    yeses = [[list(answer) for answer in answers] for answers in groups]

    count = 0

    for group in yeses:
        x = set(group[0])
        for person in group:
            for letter in person:
                x.add(letter)

        count += len(x)

    return count


def sol2():
    lines = open('input/day6.txt').read()

    groups = [group.split('\n') for group in lines.split('\n\n')]

    yeses = [[list(answer) for answer in answers] for answers in groups]

    count = 0

    for group in yeses:
        x = set(group[0])
        for person in group:
            x.intersection_update(person)

        count += len(x)

    return count
