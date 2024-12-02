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

def part_1(lines):
    num_safe = 0

    for line in lines:
        numbers = line.split()
        count = len(numbers)
        index = 0
        is_increasing = False
        is_unsafe = False

        while index < count - 1:
            diff = (int)(numbers[index + 1]) - (int)(numbers[index])

            if (index == 0):
                if (diff > 0):
                    is_increasing = True

            valid = is_diff_valid(diff, is_increasing)
            if (valid == False):
                is_unsafe = True
                break

            # increment index for while loop
            index += 1
        
        # check if line is safe
        if (is_unsafe == False):
            num_safe += 1

    # print total
    print(num_safe)

def part_2(lines):

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

    # go through each line and identify which are safe and if the unsafe ones can be made safe
    num_safe = 0
    for diff_line in diff_matrix:
        num_invalid_levels = 0
        invalid_diff_pos = 0
        index = 0
        is_increasing = diff_line[0] > 0

        # check validity
        for diff in diff_line:
            valid = is_diff_valid(diff, is_increasing)
            if (valid == False):
                num_invalid_levels += 1
                invalid_diff_pos = index

            index += 1

        # handle invalid cases
        if (num_invalid_levels == 0):
            num_safe += 1

        elif (num_invalid_levels == 1):
            # check if the removal of one level can make the line safe

            if (invalid_diff_pos == 0 or invalid_diff_pos == len(diff_line) - 1):
                # can just delete the first/last number and it'll be valid
                num_safe += 1
            else:
                # remove the invalid diff and add to the next diff and check if it is valid
                new_diff = diff_line[invalid_diff_pos] + diff_line[invalid_diff_pos + 1]
                if(is_diff_valid(new_diff, diff_line[0] > 0)):
                    num_safe += 1

        elif (num_invalid_levels == len(diff_line) - 1):
            # check if the removing the first diff makes the rest of the diff line valid
            # the reason all but one show invalid may be because the is_increasing should've been the inverse
            invalid_level_found = False
            diff_line = diff_line[1:] # slice the list to remove first element
            
            for diff in diff_line:
                valid = is_diff_valid(diff, is_increasing)
                if (valid == False):
                   invalid_level_found = True

            if (invalid_level_found == False):
                num_safe += 1

        # else the line is not safe

    print(num_safe)

##########################################
### scripts
# open file
with open('C:\SourceCode\AdventOfCode24\Day2\custom_tests.txt', 'r') as f:
    lines = f.readlines()

part_2(lines)