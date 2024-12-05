#######################################################################
with open('C:\SourceCode\AdventOfCode24\Day5\puzzle_input.txt', 'r') as f:
    lines = f.readlines()

populate_dictionary_complete = False
page_order_dict = {}
sum = 0

for line in lines:
    if populate_dictionary_complete == False:

        if line == "\n":
            populate_dictionary_complete = True
        else:
            # populate the dictionary
            nums = line.split('|')
            num1 = int(nums[0])
            num2 = int(nums[1])

            values = page_order_dict.get(num1)
            if (values is not None):
                values.append(num2)
            else:
                values = [num2]
            
            # update dictionary
            page_order_dict[num1] = values

    else:
        # check which updates are in the correct order
        nums = line.split(',')
        nums_len = len(nums)
        safe = True

        for i in range(nums_len - 1):
            j = i + 1
            while j < nums_len:
                values = page_order_dict.get(int(nums[i]))
                if values is None:
                    safe = False
                    break
 
                if int(nums[j]) not in values:
                    safe = False
                    break
                j += 1
            
            if (safe == False):
                break
        
        # if the whole line is safe, find the middle number
        if (safe):
            middle_index = int((nums_len + 1) / 2)
            sum += int(nums[middle_index - 1])
    
print("Part 1 = ", sum)
        