from time import perf_counter
import os

class Solution:
    def __init__(self):
        self.arr = []

    
    def parse_input(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
            line = lines[0]
            self.arr = line.split(' ')

    
    def part_one(self):
        for i in range(25):
            temp_arr = []
            for val in self.arr:
                if val == '0':
                    temp_arr.append('1')
                elif len(val) % 2 == 0:
                    #split string in two and append each half
                    half = int(len(val)/2)
                    first_num = int(val[:half])
                    second_num = int(val[half:])
                    temp_arr.append(str(first_num))
                    temp_arr.append(str(second_num))
                else:
                    new_val = int(val) * 2024
                    temp_arr.append(str(new_val))
            
            self.arr = temp_arr

        return len(self.arr)

    def part_two(self):
        return 0
    


###################################################################################
solution = Solution()
dir_name = os.path.dirname(__file__)
filename = os.path.join(dir_name, 'puzzle_input.txt')
solution.parse_input(filename)

start = perf_counter()
part1 = solution.part_one()
part2 = solution.part_two()
end = perf_counter()
print(f"Part 1 = {part1}")
print(f"Part 2 = {part2}")
print(f"Duration = {end - start}s")