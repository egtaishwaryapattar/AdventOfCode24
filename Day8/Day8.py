
from time import perf_counter
from operator import sub
from operator import add
import os

class Solution:
    def __init__(self):
        self.lines = []
        self.total_rows = 0
        self.total_cols = 0
        self.antenna_locations = {}     # key is antenna type, value is list a location coordinates as tuples (x,y)
        self.antinode_locations = []

    def parse_input(self, filename):
        with open(filename, 'r') as f:
            self.lines = f.readlines()

        row = 0
        for line in self.lines:
            line = line.replace("\n", "")

            # find column positions of all antenna in this line
            cols = ([pos for pos, char in enumerate(line) if char != '.'])
            for col in cols:
                self.add_antenna_to_dict(line[col], row, col)
            row += 1
    
        self.total_rows = row
        self.total_cols = len(line) 


    def add_antenna_to_dict(self, antenna, row, col):
        coords = self.antenna_locations.get(antenna)
        if coords is None:
            coords = [(row, col)]
        else:
            coords.append((row, col))
        self.antenna_locations[antenna] = coords


    def part_one(self):
        for antenna in self.antenna_locations:
            self.find_antinodes_for_antenna_type(antenna)
        return len(self.antinode_locations)
        

    def find_antinodes_for_antenna_type(self, antenna):
        locations = self.antenna_locations.get(antenna)
        num_locations = len(locations)

        for i in range(num_locations - 1):
            j = i + 1
            while j < num_locations:
                # find distance between the antenna at i and antenna at j (directin: going from i to j)
                diff = tuple(map(sub, locations[j], locations[i]))

                # find position of the two nodes
                node1 = tuple(map(sub, locations[i], diff))
                node2 = tuple(map(add, locations[j], diff))

                if self.is_in_grid(node1) and (node1 not in self.antinode_locations):
                    self.antinode_locations.append(node1)
                if self.is_in_grid(node2) and (node2 not in self.antinode_locations):
                    self.antinode_locations.append(node2)

                j += 1


    def is_in_grid(self, pos):
        if pos[0] < 0 or pos[0] > self.total_rows - 1:
            return False
        if pos[1] < 0 or pos[1] > self.total_cols - 1:
            return False
        return True


    def print_grid_with_antinodes(self):
        lines = self.lines.copy()
        for antinode in self.antinode_locations:
            row = antinode[0]
            col = antinode[1]
            line = lines[row]
            string_list = list(line)
            string_list[col] = '#'
            lines[row] = "".join(string_list)
        
        for line in lines:
            print(line)


#######################################################################
solution = Solution()
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'puzzle_input.txt')
solution.parse_input(filename)

start = perf_counter()
answer_part_one = solution.part_one()
print("Part 1 = ", answer_part_one)
#solution.print_grid_with_antinodes()
#answer_part_two = solution.part_two()
#print("Part 2 = ", answer_part_two)
end = perf_counter()
print(f"Duration = {end - start}")