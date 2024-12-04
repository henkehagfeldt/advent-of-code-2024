from utils.files import getPath

xmas = "XMAS"
all_directions = [(-1, -1), (0, -1), (1, -1),(-1, 0),(1, 0),(-1, 1),(0, 1),(1, 1)]

def part1():

    word_search = []
    with open(getPath(4, example=False), "r") as f:
        for line in f.readlines():
            word_search.append(line.strip())

    result = 0
    for y in range(len(word_search)):
        for x in range(len(word_search[y])):
            value = word_search[y][x]

            if value == "X":
                for dir in all_directions:
                    if findLetter(word_search, 1, x, y, dir[0], dir[1]):
                        result += 1
    print(result)

def findLetter(map, li, x, y, xd, yd):

    if li == 4:
        return True

    if x + xd < 0 or x + xd >= len(map[0]):
        return False
    
    if y + yd < 0 or y + yd >= len(map):
        return False
    
    if map[y+yd][x+xd] == xmas[li]:
        return findLetter(map, li + 1, x+xd, y+yd, xd, yd)
    
    return False

def part2():
    word_search = []
    with open(getPath(4, example=False), "r") as f:
        for line in f.readlines():
            word_search.append(line.strip())

    result = 0
    for y in range(len(word_search)):
        for x in range(len(word_search[y])):
            value = word_search[y][x]

            if value == "A":
                if(checkCross(word_search, x, y)):
                    result += 1

    print(result)

def checkCross(map, x, y):
    
    if x < 1 or x >= len(map[0]) - 1:
        return False
    
    if y < 1 or y >= len(map) - 1:
        return False
    
    corners = [
        map[y-1][x-1],
        map[y+1][x-1],
        map[y-1][x+1],
        map[y+1][x+1]
    ]
    
    return corners.count("M") == 2 \
        and corners.count("S") == 2 \
        and corners[0] != corners[3]

if __name__ == "__main__":
    part1()
