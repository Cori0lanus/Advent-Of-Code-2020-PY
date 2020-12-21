def sol1():
    lines = open('input/day5.txt').readlines()

    highestID = 0

    for line in lines:
        row_position = 0
        seat_id = 0
        for index, bit in enumerate(line[:7]):
            if bit == 'B':
                row_position += (1 << (6 - index))
        for index, bit in enumerate(line[7:]):
            if bit == 'R':
                seat_id += (1 << (2 - index))

        if row_position * 8 + seat_id > highestID:
            highestID = row_position * 8 + seat_id

    return highestID


def sol2():
    lines = open('input/day5.txt').readlines()

    seat_ids = []

    for line in lines:
        row_position = 0
        seat = 0
        for index, bit in enumerate(line[:7]):
            if bit == 'B':
                row_position += (1 << (6 - index))
        for index, bit in enumerate(line[7:]):
            if bit == 'R':
                seat += (1 << (2 - index))

        seat_ids.append(row_position * 8 + seat)

    for seat in seat_ids:
        if seat_ids.count(seat + 1) < 1 and seat_ids.count(seat + 2) > 0:
            return seat + 1
