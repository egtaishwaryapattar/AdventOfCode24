def is_obstacle_ahead(coord, obstacles):
    return coord in obstacles

def is_area_visited_before(coord, distinct_pos):
    return coord in distinct_pos

def is_out_of_map(pos, num_rows, num_cols):
    if pos[0] < 0 or pos[0] > num_rows - 1:
        return True
    if pos[1] < 0 or pos[1] > num_cols - 1:
        return True
    return False

#######################################################################
with open('C:\SourceCode\AdventOfCode24\Day6\puzzle_input.txt', 'r') as f:
    lines = f.readlines()

obstacles = []
distinct_pos = []
pos = (0,0)
dir = 'u'   # directions can be 'u', 'd, 'l', 'r'

# go through the input file and identify obstacles and current pos
row = 0
for line in lines:
    for col in range(len(line)):
        if line[col] == '#':
            obstacles.append((row, col))
        elif line[col] == '^':
            pos = (row, col)
            distinct_pos.append((row, col))
    row += 1

in_map = True
next_pos = (0,0)
next_dir = ''
num_cols = len(line)

while (in_map):
    # determine next action - rotate 90 degrees or take a step forward
    if dir == 'u':
        next_pos = (pos[0] - 1, pos[1])
        next_dir = 'r'
    elif dir == 'r':
        next_pos = (pos[0], pos[1] + 1)
        next_dir = 'd'
    elif dir == 'd':
        next_pos = (pos[0] + 1, pos[1])
        next_dir = 'l'
    elif dir == 'l':
        next_pos = (pos[0], pos[1] - 1)
        next_dir = 'u'

    if (is_out_of_map(next_pos, row, num_cols)):
        in_map = False
    elif (is_obstacle_ahead(next_pos, obstacles)):
            dir = next_dir
    else:
        pos = next_pos
        if is_area_visited_before(next_pos, distinct_pos) == False:
            distinct_pos.append(next_pos)

print("Part 1 = ", len(distinct_pos))