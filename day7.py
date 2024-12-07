from utils.files import getPath

def part1():

    equations = []

    with open(getPath(7, example=False), "r") as f:
        for line in f.readlines():
            total = int(line.split(':')[0])
            numbers = []
            for n in line.split(':')[1].strip().split(' '):
                numbers.append(int(n)) 
            equations.append((total, numbers))
    
    print(equations)
    
    valid = []
    for equation in equations:
        goal = equation[0]
        numbers = equation[1]
        if evaluate(goal, numbers[1:], numbers[0]):
            valid.append(goal)

    print(f"Sum: {sum(valid)}")

def evaluate(goal, numbers, current_total):
    if current_total == goal and len(numbers) == 0:
        return True
    elif len(numbers) == 0:
        return False
    elif current_total > goal:
        return False
    
    next_number = numbers[0]
    add_total = current_total + next_number
    mul_total = current_total * next_number

    return evaluate(goal, numbers[1:], add_total) or evaluate(goal, numbers[1:], mul_total)

def part2():
    equations = []

    with open(getPath(7, example=False), "r") as f:
        for line in f.readlines():
            total = int(line.split(':')[0])
            numbers = []
            for n in line.split(':')[1].strip().split(' '):
                numbers.append(int(n)) 
            equations.append((total, numbers))
    
    print(equations)
    
    valid = []
    for equation in equations:
        goal = equation[0]
        numbers = equation[1]

        if evaluate2(goal, numbers[1:], numbers[0]):
            valid.append(goal)
            
    print(f"Sum: {sum(valid)}")


def evaluate2(goal, numbers, current_total):
    if current_total == goal and len(numbers) == 0:
        return True
    elif len(numbers) == 0:
        return False
    elif current_total > goal:
        return False
    
    next_number = numbers[0]
    add_total = current_total + next_number
    mul_total = current_total * next_number
    con_total = int(str(current_total) + str(next_number))

    return evaluate2(goal, numbers[1:], add_total) \
        or evaluate2(goal, numbers[1:], mul_total) \
        or evaluate2(goal, numbers[1:], con_total)


if __name__ == "__main__":
    part2()
