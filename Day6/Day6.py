from time import perf_counter

class Solution:
    def __init__(self):
        self.obstacles = []
        self.distinct_pos = []
        self.num_rows = 0
        self.num_cols = 0
        self.pos = (0,0)


    def parse_input(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()

        # go through the input file and identify obstacles and current pos
        row = 0

        for line in lines:
            for col in range(len(line)):
                if line[col] == '#':
                    self.obstacles.append((row, col))
                elif line[col] == '^':
                    self.pos = (row, col)
                    self.distinct_pos.append((row, col))
            row += 1

        self.num_rows = row
        self.num_cols = len(line)


    def part_one(self):
        in_map = True
        dir = 'u'   # directions can be 'u', 'd, 'l', 'r'
        next_pos = (0,0)
        next_dir = ''

        while (in_map):
            # determine next action - rotate 90 degrees or take a step forward
            if dir == 'u':
                next_pos = (self.pos[0] - 1, self.pos[1])
                next_dir = 'r'
            elif dir == 'r':
                next_pos = (self.pos[0], self.pos[1] + 1)
                next_dir = 'd'
            elif dir == 'd':
                next_pos = (self.pos[0] + 1, self.pos[1])
                next_dir = 'l'
            elif dir == 'l':
                next_pos = (self.pos[0], self.pos[1] - 1)
                next_dir = 'u'

            if self.is_out_of_map(next_pos):
                in_map = False
            elif next_pos in self.obstacles:
                dir = next_dir
            else:
                self.pos = next_pos
                if (next_pos in self.distinct_pos) == False:
                    self.distinct_pos.append(next_pos)

        return len(self.distinct_pos)


    def is_out_of_map(self, pos):
        if pos[0] < 0 or pos[0] > self.num_rows - 1:
            return True
        if pos[1] < 0 or pos[1] > self.num_cols - 1:
            return True
        return False

#######################################################################
start = perf_counter()
solution = Solution()
solution.parse_input('C:\SourceCode\AdventOfCode24\Day6\puzzle_input.txt')
answer_part_one = solution.part_one()
end = perf_counter()

print(f"Part 1 duration = {end - start}")
print("Part 1 = ", answer_part_one)