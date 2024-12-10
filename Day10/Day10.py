
from time import perf_counter
import os

class Solution:
    def __init__(self):
        self.grid = []
        self.trailheads = []
        self.num_rows = 0
        self.num_cols = 0

    def parse_input(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        
        row_number = 0
        for line in lines:
            row = []
            col_number = 0
            for c in line:
                if c != '\n':
                    row.append(int(c))
                    if c == '0':
                        self.trailheads.append((row_number, col_number))
                col_number += 1

            self.grid.append(row)
            row_number += 1
        
        self.num_rows = row_number
        self.num_cols = col_number
        
        
    def part_one(self):
        sum_of_trailhead_score = 0
        for trailhead in self.trailheads:
            score = self.breath_first_search(trailhead)
            sum_of_trailhead_score += score
        return sum_of_trailhead_score
        

    def part_two(self):
        return 0
    

    def breath_first_search(self, trailhead):
        q = [trailhead]
        end_positions_found = []

        while len(q) > 0:
            # pop off the coordinate at the front of the queue and get value at the coordinate position
            coord = q.pop(0)
            search_value = self.grid[coord[0]][coord[1]] + 1

            # only searching for values between 0 - 9
            if search_value <= 9:
                found_pos = self.search_around(coord, search_value)
                if (len(found_pos) > 0):
                    if search_value == 9:
                        # once 9 (the end position) is found. Check if this is a new end position that has been found
                        for pos in found_pos:
                            if pos not in end_positions_found:
                                end_positions_found.append(pos)
                    else:
                        # add new found positions to front of array
                        q = found_pos + q
        
        return len(end_positions_found)

    def search_around(self, curr_pos, search_value):
        # search north, east, south, west from current position to find the search value
        directions = [(curr_pos[0] - 1, curr_pos[1]), # north 
                      (curr_pos[0], curr_pos[1] + 1), # east
                      (curr_pos[0] + 1, curr_pos[1]), # south
                      (curr_pos[0], curr_pos[1] - 1)] # west
        found_pos = [] # array of positions where search value is found

        for new_pos in directions:
            if self.is_in_map(new_pos) and self.grid[new_pos[0]][new_pos[1]] == search_value:
                found_pos.append(new_pos)
        
        return found_pos


    def is_in_map(self, coord):
        if coord[0] < 0 or coord[0] > self.num_rows - 1:
            return False
        if coord[1] < 0 or coord[1] > self.num_cols - 1:
            return False
        return True


#######################################################################
solution = Solution()
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'puzzle_input.txt')
solution.parse_input(filename)

start = perf_counter()
answer_part1 = solution.part_one()
print("Part1 = ", answer_part1)
#answer_part2 = solution.part_two()
#print("Part2 = ", answer_part2) 
end = perf_counter()
print(f"Duration = {end - start}")