import re

def get_num_xmas_in_lines(lines):
    xmas_found = 0

    for line in lines:
        x = re.findall("XMAS", line)
        xmas_found += x.count()

    return xmas_found

#######################################################################
with open('C:\SourceCode\AdventOfCode24\Day4\\test.txt', 'r') as f:
    lines = f.readlines()

rows = lines.count
cols = len(lines[0])
total_xmas = 0

# get number of xmas when reading wordsearch left to right
total_xmas += get_num_xmas_in_lines(lines)

# right to left
horizontal_backwards = []
for line in lines:
    horizontal_backwards.append(line[::-1])

total_xmas += get_num_xmas_in_lines(horizontal_backwards)

# up to down
vertical = []
for i in range(cols):
    new_line = ""
    for line in lines:
        new_line += line[i]
    vertical.append(new_line)

total_xmas += get_num_xmas_in_lines(horizontal_backwards)

# down to up (reverse vertical)
vertical_backwards = []
for line in vertical:
    vertical_backwards.append(line[::-1])

total_xmas += get_num_xmas_in_lines(horizontal_backwards)

# diagonally reading NE
diagonal_north_east = []
for start_row in range(rows):
    row = start_row

    if start_row < row - 1:
        new_line = ""
        col = 0
        while row >= 0 and col < cols:
            new_line += lines[row][col]
            row -= 1
            col += 1
        diagonal_north_east.append(new_line)
    else:
        # on the last row iterate through the remaining cols
        for start_col in range(cols):
            







# diagonally bottom left to top right

# diagonally top right to bottom left

# diagonally bottom right to top left