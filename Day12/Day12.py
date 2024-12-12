from time import perf_counter
import os

class Solution:
    def __init__(self):
        self.num_rows = 0
        self.num_cols = 0
        self.plant_dict = {}    # dictionary where key is letter and value is coord position
        self.plot_dict = {} # dictionary with key = Letter, value = list of list of coordinates (each list representing a unique plot)
        

    def parse_input(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()

        self.add_to_plant_dict(lines)
        self.sort_plants_into_plots()
        
    
    def part_one(self):
        return 0


    def part_two(self):
        return 0


    def add_to_plant_dict(self, lines):
        row_number = 0
        for line in lines:
            col_number = 0
            for c in line:
                if c != "\n":
                    values = self.plant_dict.get(c)
                    if values is None:
                        values = [(row_number, col_number)]
                    else:
                        values.append((row_number, col_number))
                    self.plant_dict[c] = values
                col_number += 1
            row_number += 1
        
        self.num_rows = row_number
        self.num_cols = col_number

    
    def sort_plants_into_plots(self):
        # for each flower coords
        # starts from the first one and make a q
        # search all neighbours and add to plot_dict the new neighbours (remove from old dict), then add to q 
        # go along q and find more neighbours. repeat

        for plant_type in self.plant_dict:
            positions = self.plant_dict.get(plant_type)
            self.plot_dict[plant_type] = []

            while len(positions) > 0:
                coord = positions.pop(0)
                q = [coord]
                plot = [coord]

                while len(q) > 0:
                    curr_pos = q.pop(0)
                    neighbours = self.find_neighbours(curr_pos, positions)

                    if len(neighbours) > 0:
                        q = neighbours + q

                        for neighbour in neighbours:
                            positions.remove(neighbour)
                            plot.append(neighbour)
                        
                        if len(positions) == 0:
                            break
                
                plots = self.plot_dict.get(plant_type)
                if plots is None:
                    plots = [plot]
                else:
                    plots.append(plot)
                self.plot_dict[plant_type] = plots


    def find_neighbours(self, coord, positions):
        directions = [  (coord[0] - 1, coord[1]), # north 
                        (coord[0], coord[1] + 1), # east
                        (coord[0] + 1, coord[1]), # south
                        (coord[0], coord[1] - 1), # west
                        (coord[0] - 1, coord[1] + 1), # NE 
                        (coord[0] - 1, coord[1] - 1), # NW
                        (coord[0] + 1, coord[1] + 1), # SE 
                        (coord[0] + 1, coord[1] - 1)] # SW
        
        neighbours = []
        for new_pos in directions:
            if self.is_in_map(new_pos) and new_pos in positions:
                neighbours.append(new_pos)

        return neighbours


    def is_in_map(self, coord):
        if coord[0] < 0 or coord[0] > self.num_rows - 1:
            return False
        if coord[1] < 0 or coord[1] > self.num_cols - 1:
            return False
        return True
    

###################################################################################
solution = Solution()
dir_name = os.path.dirname(__file__)
filename = os.path.join(dir_name, 'test3.txt')

start = perf_counter()
solution.parse_input(filename)
part1 = solution.part_one()
part2 = solution.part_two()
end = perf_counter()
print(f"Part 1 = {part1}")
print(f"Part 2 = {part2}")
print(f"Duration = {end - start}s")