from utils.files import getPath

def readLists():
    list1 = []
    list2 = []
    with open(getPath(1, example=False), "r") as f:
        
        for line in f.readlines():
            list1.append(int(line.split(" ")[0]))
            list2.append(int(line.split(" ")[-1]))
    
    return list1, list2

def part1():
    list1, list2 = readLists()

    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)

    result = 0
    for value_pair in zip(sorted_list1, sorted_list2):
        result += abs(value_pair[0] - value_pair[1])

    print(result)

def part2():
    list1, list2 = readLists()

    result = 0
    for value in list1:
        result += value * list2.count(value)

    print(result)

if __name__ == "__main__":
    part2()