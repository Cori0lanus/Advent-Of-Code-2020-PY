import re
import string


def sol1():
    correct = 0

    lines = open('input/day4.txt').read()
    splitLines = lines.split('\n\n')

    passports = [line.split() for line in splitLines]

    for passport in passports:
        passportMap = {}
        for detail in passport:
            passportMap[detail.split(':')[0]] = detail.split(':')[1]

        if len(passportMap) > 7 or len(passportMap) == 7 and "cid" not in passportMap:
            correct += 1

    return correct


def sol2():
    correct = 0

    lines = open('input/day4.txt').read()
    splitLines = lines.split('\n\n')

    passports = [line.split() for line in splitLines]

    for passport in passports:
        passportMap = {}
        for detail in passport:
            passportMap[detail.split(':')[0]] = detail.split(':')[1]

        if len(passportMap) > 7 or len(passportMap) == 7 and "cid" not in passportMap:
            valid = True

            valid &= 1920 <= int(passportMap["byr"]) <= 2002
            valid &= 2010 <= int(passportMap["iyr"]) <= 2020
            valid &= 2020 <= int(passportMap["eyr"]) <= 2030

            if passportMap['hgt'][-1] == 'm':
                valid &= 150 <= int(re.findall(r'\d+', passportMap["hgt"])[0]) <= 193
            elif passportMap['hgt'][-1] == 'n':
                valid &= 59 <= int(re.findall(r'\d+', passportMap["hgt"])[0]) <= 76
            else:
                continue

            valid &= all(c in string.hexdigits for c in passportMap["hcl"][1:]) and passportMap["hcl"][0] == '#' and len(passportMap["hcl"]) == 7
            valid &= passportMap["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            valid &= len(passportMap["pid"]) == 9 and re.findall(r'\d+', passportMap["pid"])[0] == passportMap["pid"]

            if valid:
                correct += 1

    return correct
