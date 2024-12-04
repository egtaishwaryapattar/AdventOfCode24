def search_up(row, col, lines):
    return (lines[row - 1][col] == 'M' and lines[row - 2][col] == 'A' and lines[row - 3][col] == 'S')

def search_down(row, col, lines):
    return (lines[row + 1][col] == 'M' and lines[row + 2][col] == 'A' and lines[row + 3][col] == 'S')

def search_left(row, col, lines):
    return(lines[row][col - 1] == 'M' and lines[row][col - 2] == 'A' and lines[row][col - 3] == 'S')

def search_right(row, col, lines):
    return (lines[row][col + 1] == 'M' and lines[row][col + 2] == 'A' and lines[row][col + 3] == 'S')

def search_north_east(row, col, lines):
    return (lines[row - 1][col + 1] == 'M' and lines[row - 2][col + 2] == 'A' and lines[row - 3][col + 3] == 'S')

def search_north_west(row, col, lines):
    return (lines[row - 1][col - 1] == 'M' and lines[row - 2][col - 2] == 'A' and lines[row - 3][col - 3] == 'S')

def search_south_east(row, col, lines):
    return (lines[row + 1][col + 1] == 'M' and lines[row + 2][col + 2] == 'A' and lines[row + 3][col + 3] == 'S')

def search_south_west(row, col, lines):
    return (lines[row + 1][col - 1] == 'M' and lines[row + 2][col - 2] == 'A' and lines[row + 3][col - 3] == 'S')

#######################################################################
with open('C:\SourceCode\AdventOfCode24\Day4\puzzle_input.txt', 'r') as f:
    lines = f.readlines()

num_rows = len(lines)
num_cols = len(lines[0])
total_xmas = 0

# iterate through each line to find an 'X'
line_number = 0
for line in lines:
    list = ([pos for pos, char in enumerate(line) if char == 'X'])
    
    for index in list:
        if line_number >= 3:
            total_xmas += search_up(line_number, index, lines)
        if line_number <= (num_rows - 4):
            total_xmas += search_down(line_number, index, lines)
        if index >= 3:
            total_xmas += search_left(line_number, index, lines)
        if index <= (num_cols - 4):
            total_xmas += search_right(line_number, index, lines)
        if line_number >= 3 and index <= (num_cols - 4):
            total_xmas += search_north_east(line_number, index, lines)
        if line_number >= 3 and index >= 3:
            total_xmas += search_north_west(line_number, index, lines)
        if line_number <= (num_rows - 4) and index <= (num_cols - 4):
            total_xmas += search_south_east(line_number, index, lines)
        if line_number <= (num_rows - 4) and index >= 3:
            total_xmas += search_south_west(line_number, index, lines)

    line_number += 1

print("Part 1: ", total_xmas)