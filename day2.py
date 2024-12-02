from utils.files import getPath

def part1():

    reports = []

    with open(getPath(2, example=False), "r") as f:
        for line in f.readlines():
            reports.append(line.split(" "))

    result = 0
    for report in reports:
        direction = 0
        for i in range(0, len(report) - 1):
            li = int(report[i])
            lii = int(report[i + 1])

            diff = lii - li
            if diff == 0:
                break
            
            new_direction = diff / abs(diff)
            if (direction != 0 and new_direction != direction):
                break

            direction = new_direction

            if (direction == 1 and (diff < 1 or diff > 3)):
                break
            elif (direction == -1 and (diff < -3 or diff > -1)):
                break

            if i == len(report) - 2:
                result += 1

    print(result)

def part2():
    reports = []

    with open(getPath(2, example=True), "r") as f:
        for line in f.readlines():
            reports.append(line.split(" "))

    result = 0
    for r, report in enumerate(reports):
        direction = 0
        t = 0
        i = 0

        while (i + t + 1 < len(report)):
            if (t > 1):
                break

            li = int(report[i])
            lii = int(report[i + t + 1])

            if (direction == 0 and li > lii):
                direction = -1
            elif (direction == 0 and li < lii):
                direction = 1
            elif (li == lii):
                t += 1
                continue

            if (not checkValid(li, lii, direction)):
                t += 1
                continue

            if i + t == (len(report) - 2):
                print(f"Report {r + 1} safe, t {t}")
                result += 1
            
            i += 1

    print(result)

def checkValid(v1, v2, direction):
    
    diff = v2 - v1

    if diff == 0:
        print("No diff")
        return False

    vDir = diff / abs(diff)

    if (vDir != direction):
        print("New dir")
        return False

    #print(f"Dir: {direction}, Diff: {diff}")

    if (direction == 1 and (diff < 1 or diff > 3)):
        return False
    elif (direction == -1 and (diff < -3 or diff > -1)):
        return False
    
    return True

if __name__ == "__main__":
    part2()