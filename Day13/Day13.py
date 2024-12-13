from time import perf_counter
import os
import re
from sympy import symbols, Eq, solve 

class ClawGameParams:
    def __init__(self, coord_A, coord_B, coord_prize):
        self.A = coord_A
        self.B = coord_B
        self.prize = coord_prize

class Solution:
    def __init__(self):
        self.claw_games = []
    
    def parse_input(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()

        # extract claw game params from the file
        values = []
        for line in lines:
            if line == "\n":
                # create a ClawGameParams
                claw_game = ClawGameParams((values[0], values[1]), (values[2], values[3]), (values[4], values[5]))
                self.claw_games.append(claw_game)
                values.clear()
            else:
                p = re.compile(r'\d+')
                found = p.findall(line)
                for val in found:
                    values.append(int(val))

        # create a ClawGameParams
        claw_game = ClawGameParams((values[0], values[1]), (values[2], values[3]), (values[4], values[5]))
        self.claw_games.append(claw_game)

    
    def part_one(self):
        total_tokens = 0
        for game in self.claw_games:
            total_tokens += self.play_game(game)
        return total_tokens


    def part_two(self):
        total_tokens = 0
        for game in self.claw_games:
            # first modify target
            game.prize = (10000000000000 + game.prize[0], 10000000000000 + game.prize[1])
            total_tokens += self.play_game(game)
        return total_tokens
    

    def play_game(self, game):
        # return the least number of tokens used - always only one token
        tokens = 0
        a,b = symbols('a,b')
        eq1 = Eq(( game.A[0] * a + game.B[0] * b) , game.prize[0])
        eq2 = Eq(( game.A[1] * a + game.B[1] * b) , game.prize[1])

        answer = solve((eq1, eq2), (a,b))
        press_a = answer.get(a)
        press_b = answer.get(b)

        if press_a.denominator == 1:
            if press_b.denominator == 1:
                tokens = press_a.numerator * 3 + press_b.numerator
        return tokens


###################################################################################
solution = Solution()
dir_name = os.path.dirname(__file__)
filename = os.path.join(dir_name, 'puzzle_input.txt')
solution.parse_input(filename)

start = perf_counter()
part1 = solution.part_one()
#part2 = solution.part_two()
end = perf_counter()
print(f"Part 1 = {part1}")
#print(f"Part 2 = {part2}")
print(f"Duration = {end - start}s")