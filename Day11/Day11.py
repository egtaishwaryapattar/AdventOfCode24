from time import perf_counter
import os

class Solution:
    def __init__(self):
        self.lines = []

    
    def parse_input(self, filename):
        with open(filename, 'r') as f:
            self.lines = f.readlines()

        # TODO:

    
    def part_one(self):
        return 0
    

    def part_two(self):
        return 0
    


###################################################################################
solution = Solution()
dir_name = os.path.dirname(__file__)
filename = os.path.join(dir_name, 'test.txt')
solution.parse_input(filename)

start = perf_counter()
part1 = solution.part_one()
part2 = solution.part_two()
end = perf_counter()
print(f"Part 1 = {part1}")
print(f"Part 2 = {part2}")
print(f"Duration = {end - start}s")