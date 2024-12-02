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
    line_number = 0

    for line in lines:
        numbers = line.split()
        index = 0
        count = len(numbers)

        while index < count - 1:
            diff = (int)(numbers[index + 1]) - (int)(numbers[index])
            diff_matrix[line_number][index] = (diff)
            index +=1

    # go through each line and identify which are safe and if the unsafe ones can be made safe
    num_safe = 0

    print(num_safe)

##########################################
### scripts
# open file
with open('C:\SourceCode\AdventOfCode24\Day2\\test.txt', 'r') as f:
    lines = f.readlines()

part_1(lines)