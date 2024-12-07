
from time import perf_counter
import math
import os

class Solution:
    def __init__(self):
        self.equations = {}
        

    def parse_input(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()

        for line in lines:
            parts = line.split(': ')
            values = parts[1].split(' ')
            nums = []
            for value in values:
                nums.append(int(value))

            # not sure if this situation occurs in the puzzle input...
            if (self.equations.get(int(parts[0])) is not None):
                raise Exception("Scenario where two equations need to result in the same number")

            self.equations[int(parts[0])] = nums


    def part_one(self):
        sum = 0
        for target in self.equations:
            if self.is_equation_valid(target, self.equations.get(target)):
                sum += target   
        return sum


    def is_equation_valid(self, target, nums):
        len_nums = len(nums)
        sum_of_nums = sum(nums)
        product_of_nums = math.prod(nums)
        
        # test if combination of multiplication and addition is needed
        arr = []
        for i in range(len_nums):
            if i == 0:
                arr.append(nums[i])
            else:
                temp = arr.copy()
                arr.clear()
                for val in temp:
                    # the array size keeps increasing with each calculation - each time creating two branches - one for addition one for multiplication
                    arr.append(val + nums[i])
                    arr.append(val * nums[i])

        return target in arr


#######################################################################
solution = Solution()
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'puzzle_input.txt')
solution.parse_input(filename)

start = perf_counter()
answer_part_one = solution.part_one()
print("Part 1 = ", answer_part_one)
end = perf_counter()
print(f"Duration = {end - start}")