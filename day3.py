import re
from utils.files import getPath

def part1():

    data = ""
    with open(getPath(3, example=False), "r") as f:
        data = f.readline()

    pattern = "mul\((\d{1,3}),(\d{1,3})\)"
    result = 0
    
    for match in re.findall(pattern, data):
        result += int(match[0]) * int(match[1])

    print(result)

def part2():
    data = ""

    with open(getPath(3, example=True), "r") as f:
        data = f.readline()

    pattern = "mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))"
    enabled = True
    result = 0

    for match in re.findall(pattern, data):
        if match[2] != '':
            enabled = True
        elif match[3] != '':
            enabled = False
        elif enabled:
            result += int(match[0]) * int(match[1])

    print(result)

if __name__ == "__main__":
    part2()
