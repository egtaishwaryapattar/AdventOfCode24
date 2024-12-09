
from time import perf_counter
import os

class Solution:
    def __init__(self):
        self.blocks = {}    # key = the index, value = value stored at that index position

    def parse_input(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
            
        # the input is only one line  
        disk_map = lines[0]
        self.get_blocks(disk_map)
        
    def part_one(self):
        self.compact_files()
        return self.calculate_checksum()
        

    def part_two(self):
        return 0
    

    def get_blocks(self, disk_map):
        # translate the disk map into the individual blocks
        disk_map_index = 0
        block_index = 0
        block_value = 0     # value to fill in the block

        while disk_map_index < len(disk_map):
            if disk_map_index % 2 == 0:
                value = block_value
                block_value += 1
            else:                   # modulo returns 1
                value = '.'
            
            for i in range(int(disk_map[disk_map_index])):
                self.blocks[block_index] = value
                block_index += 1

            disk_map_index += 1


    def compact_files(self):
        forward_index = 0
        reverse_index = len(self.blocks) - 1

        while forward_index < reverse_index:
            if self.blocks.get(forward_index) == '.':
                
                # find end value
                found_value = False
                while found_value == False:
                    end_value = self.blocks.get(reverse_index)
                    if end_value != '.':
                        found_value = True
                    else:
                        reverse_index -= 1
                        if reverse_index <= forward_index:
                            break
                
                if found_value:
                    # swap '.' and end value
                    self.blocks[forward_index] = end_value
                    self.blocks[reverse_index] = '.'
                    reverse_index -= 1

            forward_index += 1


    def calculate_checksum(self):
        checksum = 0

        for i in range(len(self.blocks)):
            value = self.blocks.get(i)
            if value == '.':
                break
            else:
                checksum += value * i

        return checksum


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