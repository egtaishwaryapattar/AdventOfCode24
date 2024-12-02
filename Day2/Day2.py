# open file
with open('C:\SourceCode\AdventOfCode24\Day2\puzzle_input.txt', 'r') as f:
    lines = f.readlines()

num_safe = 0

for line in lines:
    numbers = line.split()
    count = len(numbers)
    index = 0
    is_increasing = False
    is_unsafe = False

    while index < count - 1:
        diff = (int)(numbers[index + 1]) - (int)(numbers[index])

        # check the difference is valid
        if (abs(diff) == 0 or abs(diff) > 3):
            # difference if invalid
            is_unsafe = True
            break
        else:
            # difference if valid
            if (index == 0):
                if (diff > 0):
                    is_increasing = True
            else:
                # ensure the whole line in increasing or decreasing
                if ((is_increasing and diff < 0)
                    or (is_increasing == False and diff > 0)):
                    is_unsafe = True
                    break
        
        # increment index for while loop
        index += 1
    
    # check if line is safe
    if (is_unsafe == False):
        num_safe += 1

# print total
print(num_safe)