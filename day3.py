import re
from utils.files import getPath

def part1():

    data = ""

    with open(getPath(3, example=False), "r") as f:
        data = f.readline()

    pattern = "mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, data)

    result = 0
    for match in matches:
        result += int(match[0]) * int(match[1])

    print(result)

def part2():
    data = ""

    with open(getPath(3, example=True), "r") as f:
        data = f.readline()

    pattern = "mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))"
    matches = re.findall(pattern, data)

    enabled = True
    result = 0
    for match in matches:
        print(match)

        if match[2] != '':
            enabled = True
        elif match[3] != '':
            enabled = False
        elif enabled:
            result += int(match[0]) * int(match[1])

    print(result)

if __name__ == "__main__":
    part2()