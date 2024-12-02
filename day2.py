from utils.files import getPath

def part1():

    reports = []

    with open(getPath(2, example=False), "r") as f:
        for line in f.readlines():
            reports.append(line.split(" "))

    result = 0
    for report in reports:
        if (checkReport(report)):
            result += 1

    print(result)

def part2():
    reports = []

    with open(getPath(2, example=False), "r") as f:
        for line in f.readlines():
            reports.append(line.split(" "))

    result = 0
    for report in reports:
        i = 0
        while (i < len(report)):
            report_copy = report.copy()
            del report_copy[i]
            if (checkReport(report_copy)):
                result += 1
                break
            i += 1

    print(result)

def checkReport(report):
    direction = 0
    i = 0
    print(report)
    while (i + 1 < len(report)):
        li = int(report[i])
        lii = int(report[i + 1])

        if (direction == 0 and li > lii):
            direction = -1
        elif (direction == 0 and li < lii):
            direction = 1
        elif (li == lii):
            return False
        elif (direction == 1 and li > lii):
            return False
        elif (direction == -1 and li < lii):
            return False

        diff = lii - li

        if (direction == 1 and (diff < 1 or diff > 3)):
            return False
        elif (direction == -1 and (diff < -3 or diff > -1)):
            return False
        
        i += 1
    
    return True

if __name__ == "__main__":
    part2()
