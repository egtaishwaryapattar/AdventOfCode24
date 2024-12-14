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
            x = ( robot.pos[0] + (iterations * robot.velocity[0]) ) % width
            y = ( robot.pos[1] + iterations * robot.velocity[1] ) % height

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


    def part_two(self, width, height, start_val):
        # hate vague requirements - attempt of a vague solution
        # I assume that a xmas tree would be centred. So down the vertical centre there would be *a lot* of robots
        vert_center = (width - 1) / 2

        # initialise a grid
        empty_grid = []
        for i in range(height):
            row = ''
            for j in range(width):
                row = row + ' '
            empty_grid.append(row)

        # for each second, check if there is a cluster down the center
        for i in range(start_val, 100000):
            on_vertical_center = []

            # find robot's positions at time i
            for robot in self.robots:
                if i == start_val:
                    # get the robots in the position we want them to start in
                    x = ( robot.pos[0] + start_val * robot.velocity[0] ) % width
                    y = ( robot.pos[1] + start_val * robot.velocity[1] ) % height
                    robot.pos = (x,y)

                else:
                    # robot moves to its next position
                    x = ( robot.pos[0] + robot.velocity[0] ) % width
                    y = ( robot.pos[1] + robot.velocity[1] ) % height
                    robot.pos = (x,y)

                    if robot.pos[0] == vert_center:
                        # just keep y value as we know the x value
                        on_vertical_center.append(robot.pos[1])

            # at time i, assess whether there are enough points down the vertical centre and draw to see if it resembles a tree
            # there are 500 guards, and the grid is 103 in height, so spanning a half of the height sound reasonable?
            if len(on_vertical_center) > height / 2:
                has_point = self.find_xmas_tree_point(on_vertical_center, vert_center, empty_grid.copy())
                if has_point:
                    print(f"Num seconds = {i}")
                    break

        return i


    def find_xmas_tree_point(self, robots_on_vert_center, grid):
        # determine if the xmas tree has a point and no values robots above it or to the side of it
        # minimum value on vertical centre line is a potential point
        y = min(robots_on_vert_center)

        is_point = True
        for robot in self.robots:
            steps_across = robot.pos[0]
            steps_down = robot.pos[1]

            grid[steps_down][steps_across] = '*'

            if steps_down <= y:
                is_point = False
                break

        if is_point:
            print(grid)

        return is_point


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
part2 = solution.part_two(width, height, 0)
end = perf_counter()
print(f"Part 1 = {part1}")
print(f"Part 2 = {part2}")         
print(f"Duration = {end - start}s")