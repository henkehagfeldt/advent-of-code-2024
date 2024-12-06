from utils.files import getPath

def part1():

    layout = []
    guard_pos = None
    y = 0

    guard_direction = (0, -1)

    with open(getPath(6, example=False), "r") as f:
        for line in f.readlines():
            if '^' in line:
                guard_pos = (line.index('^'), y) 
            layout.append(line.strip())
            y += 1

    print(layout)
    print(guard_pos)

    guard_traversed = [guard_pos]

    while True:
        
        # Move guard
        next_pos = get_next_pos(layout, guard_pos, guard_direction)
        if (next_pos == None):
            break

        next_value = layout[next_pos[1]][next_pos[0]]

        if (next_value == '#'):
            guard_direction = get_next_guard_direction(guard_direction)
        else:
            if not next_pos in guard_traversed:
                guard_traversed.append(next_pos)
            guard_pos = next_pos
    
    print(len(guard_traversed))

def get_next_guard_direction(guard_direction):
    if guard_direction == (0, -1):
        return (1, 0)
    elif guard_direction == (1, 0):
        return (0, 1)
    elif guard_direction == (0, 1):
        return (-1, 0)
    else:
        return (0, -1)

def get_next_pos(layout, guard_pos, guard_direction):
    next_x = guard_pos[0] + guard_direction[0]
    next_y = guard_pos[1] + guard_direction[1]
    
    if pos_in_layout(layout, (next_x, next_y)):
        return (next_x, next_y)
    else:
        return None

def pos_in_layout(layout, guard_pos):
    return guard_pos[0] >= 0 and guard_pos[0] < len(layout[0]) and guard_pos[1] >= 0 and guard_pos[1] < len(layout)

def part2():
    layout = []
    guard_pos = None
    y = 0

    guard_direction = (0, -1)

    with open(getPath(6, example=False), "r") as f:
        for line in f.readlines():
            if '^' in line:
                guard_pos = (line.index('^'), y) 
            layout.append(line.strip())
            y += 1

    print(layout)
    print(guard_pos)

    turns = 0
    steps_taken = 0
    steps_loop = []
    loopies = 0

    current_obstacle = None
    start_guard_pos = None
    start_guard_direction = None

    previous = []
    previous_directions = []

    while True:
        # Move guard
        next_pos = get_next_pos(layout, guard_pos, guard_direction)
        previous.append((next_pos, guard_direction))

        print(f"Next: {next_pos}, Start Guard: {start_guard_pos} {start_guard_direction}, Obstacle: {current_obstacle}")

        if (next_pos == None):
            if (current_obstacle == None):
                break
            else:
                clear(layout, current_obstacle)
                current_obstacle = None
                guard_pos = start_guard_pos
                guard_direction = start_guard_direction
                previous = []
                continue

        next_value = layout[next_pos[1]][next_pos[0]]

        # Next is a wall
        if (next_value == '#'):
            if (guard_pos, guard_direction) in previous and current_obstacle != None:
                print(f"Found loopy - {current_obstacle[0]}, {current_obstacle[1]}")
                loopies += 1
                clear(layout, current_obstacle)
                current_obstacle = None
            else:
                guard_direction = get_next_guard_direction(guard_direction)
                steps_loop.append(steps_taken)
                steps_taken = 0
                turns += 1

        # Next is not a wall
        else:
            guard_pos = next_pos
            steps_taken += 1

            # No obstacle set
            if current_obstacle == None and turns > 3:
                start_guard_direction = guard_direction
                start_guard_pos = guard_pos
                current_obstacle = next_pos
                set(layout, current_obstacle)
        
    print(loopies)

def clear(layout, obstacle):
    layout[obstacle[1]] = f"{layout[obstacle[1]][:obstacle[0]]}.{layout[obstacle[1]][obstacle[0] + 1:]}"

def set(layout, obstacle):
    layout[obstacle[1]] = f"{layout[obstacle[1]][:obstacle[0]]}#{layout[obstacle[1]][obstacle[0] + 1:]}"

if __name__ == "__main__":
    part2()
