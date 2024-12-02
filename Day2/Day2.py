##########################################
### functions
def is_diff_valid(diff, is_increasing):
    # check the difference is valid
    if (abs(diff) == 0 or abs(diff) > 3):
        # difference if invalid
        return False
    else:
        # difference if valid
        # ensure the whole line in increasing or decreasing
        if ((is_increasing and diff < 0)
            or (is_increasing == False and diff > 0)):
            return False
        else:
            return True

def is_line_safe(line):
    count = len(line)
    index = 0
    is_increasing = False

    while index < count - 1:
        diff = (line[index + 1]) - (line[index])

        if (index == 0):
            if (diff > 0):
                is_increasing = True

        valid = is_diff_valid(diff, is_increasing)
        if (valid == False):
            return False
            break

        # increment index for while loop
        index += 1
    
    return True

def part_1(matrix):
    global part1_safe
    part1_safe = 0
    unsafe_lines = []

    for line in matrix:
        # check if line is safe
        if (is_line_safe(line)):
            part1_safe += 1
        else:
            unsafe_lines.append(line)

    print("Part 1 number safe = ", part1_safe)
    return unsafe_lines
'''
def create_diff_matrix(lines):
    # for each line, calculate the numerical diff and construct a matrix of diffs 
    diff_matrix = []

    for line in lines:
        numbers = line.split()
        diffs = []
        index = 0
        count = len(numbers)

        while index < count - 1:
            diff = (int)(numbers[index + 1]) - (int)(numbers[index])
            diffs.append(diff)
            index +=1
        
        diff_matrix.append(diffs)

    return diff_matrix
'''
def are_levels_increasing(diff_line):
    # determine if the list is increasing or decreasing
    if ((diff_line[0] > 0) == (diff_line[1] > 0)):
        return diff_line[0] > 0
    else:
        if ((diff_line[0] > 0) == (diff_line[2] > 0)):
            return diff_line[0] > 0
        else:
            return diff_line[2] > 0

def part_2(matrix):
    global part2_safe
    part2_safe = 0

    # know that all the lines coming in are unsafe. Need to find out if the removal of one level will make the line safe
    # brute force
    for list in matrix:
        for number in list:
            # remove the number from the list and test if it is valid
            list_copy = list.copy()
            list_copy.remove(number)
            if (is_line_safe(list_copy)):
                part2_safe += 1
                break

    print("Part 2 number safe = ", part2_safe)



    '''
    diff_matrix = create_diff_matrix(lines)
    num_safe = 0
    line_number = 0
    
    # go through each line and identify which are safe and if the unsafe ones can be made safe
    for diff_line in diff_matrix:
        is_increasing = are_levels_increasing(diff_line)

        invalid_diff_pos = []
        index = 0
        is_safe = False

        # check validity
        for diff in diff_line:
            if (is_diff_valid(diff, is_increasing) == False):
                invalid_diff_pos.append(index)

            index += 1

        # handle invalid cases
        num_invalid_levels = len(invalid_diff_pos)
        if (num_invalid_levels == 0):
            is_safe = True

        elif (num_invalid_levels == 1):
            # check if the removal of one level can make the line safe

            if (invalid_diff_pos[0] == 0 or invalid_diff_pos[0] == len(diff_line) - 1):
                # can just delete the first/last number and it'll be valid
                is_safe = True
            else:
                # remove the invalid diff and add to the next diff and check if it is valid
                pos = invalid_diff_pos[0]
                new_diff = diff_line[pos] + diff_line[pos + 1]
                if(is_diff_valid(new_diff, is_increasing)):
                    is_safe = True

        elif (num_invalid_levels == 2):
            # check that the two invalid levels are consecutive
            if (invalid_diff_pos[1] - invalid_diff_pos[0] == 1):
                # if the sum of them is valid then it is fine
                new_diff = diff_line[invalid_diff_pos[0]] + diff_line[invalid_diff_pos[1]]
                if(is_diff_valid(new_diff, is_increasing)):
                    is_safe = True

#        elif (num_invalid_levels == len(diff_line) - 1):
            # check if the removing the first diff makes the rest of the diff line valid
            # the reason all but one show invalid may be because the is_increasing should've been the inverse
#            invalid_level_found = False
#            diff_line = diff_line[1:] # slice the list to remove first element
            
#            for diff in diff_line:
#                valid = is_diff_valid(diff, diff_line[0] > 0)
#                if (valid == False):
#                   invalid_level_found = True

#            if (invalid_level_found == False):
#                is_safe = True

        # else the line is not safe

        #print(is_safe)
        
        if (is_safe):
            num_safe += 1
        else:
            print(lines[line_number])

        line_number += 1

    print(num_safe)
    '''

##########################################
### scripts
# open file
with open('C:\SourceCode\AdventOfCode24\Day2\puzzle_input.txt', 'r') as f:
    lines = f.readlines()

    matrix = []
    for line in lines:
        numbers = line.split()
        num_list = []

        for number in numbers:
            num_list.append((int)(number))
        
        matrix.append(num_list)

unsafe_lines = part_1(matrix)
part_2(unsafe_lines)

print("Total number of safe lines = ", part1_safe + part2_safe)