from time import perf_counter
import os
import re
import math

class Robot:
    def __init__(self, pos, velocity):
        # (x,y) where x is num steps to right, y is num steps down
        self.pos = pos
        self.velocity = velocity

class Solution:
    def __init__(self):
        self.robots = []
        self.quadrants = {}

    
    def parse_input(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()

        for line in lines:
            # one robot per line
            p = re.compile(r'-?\d+')
            vals = p.findall(line)

            robot = Robot( (int(vals[0]), int(vals[1])) , (int(vals[2]), int(vals[3])) )
            self.robots.append(robot)

    
    def part_one(self, width, height):
        iterations = 100
        quadrant_horizontal_boundary = (height - 1) / 2
        quadrant_vertical_boundary = (width - 1) / 2

        for robot in self.robots:
            # for each robot, determine where it'll be after the number of iterations
            x = robot.pos[0] + (iterations * robot.velocity[0])
            x = x % width
            y = robot.pos[1] + iterations * robot.velocity[1]
            y = y % height

            # determine which quadrant that the new pos belongs to
            quadrant = 0
            if x < quadrant_vertical_boundary and y < quadrant_horizontal_boundary:
                quadrant = 1
            elif x > quadrant_vertical_boundary and y < quadrant_horizontal_boundary:
                quadrant = 2
            elif x < quadrant_vertical_boundary and y > quadrant_horizontal_boundary:
                quadrant = 3
            elif x > quadrant_vertical_boundary and y > quadrant_horizontal_boundary:
                quadrant = 4
                
            if quadrant != 0:
                self.quadrants[quadrant] = self.quadrants.get(quadrant, 0) + 1

        values = self.quadrants.values()
        return math.prod(values)


    def part_two(self):
        return 0


###################################################################################
solution = Solution()
dir_name = os.path.dirname(__file__)
filename = os.path.join(dir_name, 'puzzle_input.txt')
solution.parse_input(filename)

# test grid is (11, 7). puzzle_input is (101, 103)
width = 101
height = 103

start = perf_counter()
part1 = solution.part_one(width, height)
part2 = solution.part_two()
end = perf_counter()
print(f"Part 1 = {part1}")
print(f"Part 2 = {part2}")         
print(f"Duration = {end - start}s")