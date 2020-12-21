def sol1():
    lines = open('input/day7.txt').readlines()

    bag_colors = [line.split('bag')[0][:-1] for line in lines]
    contains = []

    for line in lines:
        for key in line.split('contain')[1:]:
            contains.append(key.replace('.', '').replace('\n', '').split(','))
            for index, item in enumerate(contains[-1]):
                stripped = contains[-1][index].lstrip().split(' ')
                if stripped[0] != 'no':
                    contains[-1][index] = {stripped[1] + ' ' + stripped[2]: int(stripped[0])}
                else:
                    bag_colors.pop(len(contains) - 1)
                    contains.pop(-1)

    bags = dict(zip(bag_colors, contains))
    can_contain_gold = []

    while len(bags) > 0:
        to_pop = []
        for bag, inside in bags.items():
            bags_inside = [list(i)[0] for i in inside]
            # print(inside)
            if not inside:
                to_pop.append(bag)

            if 'shiny gold' in bags_inside:  # if shiny gold is in bags inside
                to_pop.append(bag)
                can_contain_gold.append(bag)

            for b in bags_inside:  # for every bag inside
                if b not in bags.keys():  # if the bag inside isnt in bag dict
                    for elem in inside:  # for element in inside
                        if list(elem.keys())[0] == b:  # if that element is the bag not in the dict
                            bags[bag].pop(inside.index(elem))
                            # print(elem, bag.count(b))

            for possible in can_contain_gold:  # for every bag that can contain gold
                if possible in bags_inside:  # if that bag is in inside bags
                    to_pop.append(bag)  # remove that bag from the main list
                    can_contain_gold.append(bag)  # add it to the list that can contain gold

        for pop in set(to_pop):
            bags.pop(pop)

    return len(set(can_contain_gold))
