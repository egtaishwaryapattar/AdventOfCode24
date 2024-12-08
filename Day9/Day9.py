
from time import perf_counter
import os

class Solution:
    def __init__(self):
        self.lines = []

    def parse_input(self, filename):
        with open(filename, 'r') as f:
            self.lines = f.readlines()

        
    def part_one(self):
        return 0
        

    def part_two(self):
        return 0


#######################################################################
solution = Solution()
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'test.txt')
solution.parse_input(filename)

start = perf_counter()
answer_part1 = solution.part_one()
print("Part1 = ", answer_part1)
answer_part2 = solution.part_two()
print("Part2 = ", answer_part2)
end = perf_counter()
print(f"Duration = {end - start}")