import re
from utils.files import getPath

def part1():

    with open(getPath(4, example=True), "r") as f:
        word_search = f.readlines()

    result = 0
    for y in range(len(word_search)):
        for x in range(len(word_search[y])):
            value = word_search[y][x]

            if value == "X":
                if(checkXmas(word_search, x, y)):
                    print(f"Found XMAS at {x}, {y}")
                    result += 1
    print(result)

def checkXmas(map, x, y):
    print(f"Checking for XMAS at {x}, {y}")
    next_x, next_y = x, y
    for letter in "MAS":
        next_x, next_y = findLetterAround(map, letter, next_x, next_y)
        if next_x == None or next_y == None:
            return False

def findLetterAround(map, letter, center_x, center_y):
    
    start_y = max(center_y - 1, 0)
    end_y = min(center_y + 1, len(map) - 1)

    start_x = max(center_x - 1, 0)
    end_x = min(center_x + 1, len(map[0]) - 1)

    print(f"Search Area: x {start_x}, {end_x} - y {start_y}, {end_y}")

    for y in range(start_y, end_y + 1):
        for x in range(start_x, end_x + 1):
            print(f"Checking {x}, {y} for {letter}")
            value = map[y][x]
            if value == letter:
                return x, y
    
    return None, None

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
    part1()
