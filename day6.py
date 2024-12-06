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
    initial_guard_pos = None
    initial_guard_dir = (0, -1)
    y = 0

    with open(getPath(6, example=False), "r") as f:
        for line in f.readlines():
            if '^' in line:
                initial_guard_pos = (line.index('^'), y) 
            layout.append(line.strip())
            y += 1
    
    guard_pos = initial_guard_pos
    guard_direction = initial_guard_dir

    o_guard_traversed = [guard_pos]
    
    while True:
        
        # Move guard
        next_pos = get_next_pos(layout, guard_pos, guard_direction)
        if (next_pos == None):
            break

        next_value = layout[next_pos[1]][next_pos[0]]

        if (next_value == '#'):
            guard_direction = get_next_guard_direction(guard_direction)
        else:
            if not next_pos in o_guard_traversed:
                o_guard_traversed.append(next_pos)
            guard_pos = next_pos

    loops = 0

    for pos in o_guard_traversed:

        guard_pos = initial_guard_pos
        guard_direction = initial_guard_dir

        guard_traversed = {(guard_pos, guard_direction): ""}
        
        x = pos[0]
        y = pos[1]

        if layout[y][x] == '#':
            continue
        
        while True:
            # Move guard
            next_pos = get_next_pos(layout, guard_pos, guard_direction)

            if (next_pos, guard_direction) in guard_traversed:
                loops += 1
                break

            # Guard out of bounds
            if (next_pos == None):
                break

            next_value = layout[next_pos[1]][next_pos[0]]

            if (next_pos == pos or next_value == '#'):
                guard_direction = get_next_guard_direction(guard_direction)
            else:
                guard_traversed[((next_pos, guard_direction))] = ""
                guard_pos = next_pos
            
    print(loops)

if __name__ == "__main__":
    part2()
