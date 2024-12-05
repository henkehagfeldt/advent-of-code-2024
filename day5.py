from utils.files import getPath

def part1():

    rules = {}
    updates = []

    with open(getPath(5, example=False), "r") as f:
        for line in f.readlines():
            if ('|' in line):
                before, after = line.split('|')
                before = before.strip()
                after = after.strip()

                if not after in rules:
                    rules[after] = set()
                rules[after].add(before)

            elif (',' in line):
                updates.append(line.strip().split(','))
    
    print(rules)
    correct_updates = []
    for update in updates:
        printed = set()
        correct = True
        for value in update:
            if value in rules:
                required = rules[value]
                print(f"Value: {value} Req: {required}, Up: {update}, Printed: {printed}")
                if not required.intersection(set(update)).issubset(printed):
                    print("Not Satisfied!")
                    correct = False
                    break
                else:
                    printed.add(value)
            else:
                printed.add(value)
        if correct:
            correct_updates.append(update)
    
    print(correct_updates)
    
    result = 0
    for correct in correct_updates:
        result += int(correct[int(len(correct)/2)])
    print(result)

def part2():
    
    rules = {}
    updates = []

    with open(getPath(5, example=True), "r") as f:
        for line in f.readlines():
            if ('|' in line):
                before, after = line.split('|')
                before = before.strip()
                after = after.strip()

                if not after in rules:
                    rules[after] = set()
                rules[after].add(before)

            elif (',' in line):
                updates.append(line.strip().split(','))
    
    print(rules)
    incorrect_updates = []
    for update in updates:
        printed = set()
        correct = True
        for value in update:
            if value in rules:
                required = rules[value]
                print(f"Value: {value} Req: {required}, Up: {update}, Printed: {printed}")
                if not required.intersection(set(update)).issubset(printed):
                    issues = required.intersection(set(update)).difference(printed)
                    print(f"Issues: {issues}")
                    #index_previous = update.index()
                    print("Not Satisfied!")
                    correct = False
                    break
                else:
                    printed.add(value)
            else:
                printed.add(value)
        if not correct:
            incorrect_updates.append(update)
    
    print(incorrect_updates)


    
    result = 0
    for incorrect in incorrect_updates:
        result += int(incorrect[int(len(incorrect)/2)])
    print(result)

if __name__ == "__main__":
    part2()
