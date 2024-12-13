from time import perf_counter
import os
import re
import math

class ClawGameParams:
    def __init__(self, coord_A, coord_B, coord_prize):
        self.A = coord_A
        self.B = coord_B
        self.prize = coord_prize

class AttemptNumber:
    def __init__(self):
        self.num_attempts = 0
        self.buttonA_pressed = 0
        self.buttonB_pressed = 0
        self.coordinate = (0,0)
        self.tokens_used = 0

    def copy(self, attempt):
        self.num_attempts = attempt.num_attempts
        self.buttonA_pressed = attempt.buttonA_pressed
        self.buttonB_pressed = attempt.buttonB_pressed
        self.coordinate = attempt.coordinate
        self.tokens_used = attempt.tokens_used

    def make_move(self, a, b, dist):
        # a or b should be 0 or 1
        # moving A = 1 token
        # moving B = 3 tokens
        self.num_attempts += 1
        self.buttonA_pressed += a
        self.buttonB_pressed += b
        self.coordinate = (self.coordinate[0] + dist[0], self.coordinate[1] + dist[1])
        self.tokens_used += a + 3 * b

        return self.coordinate


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
        return 0


    def part_two(self):
        return 0
    

    def play_game(self, game):
        # return the least number of tokens used - there could be more than 1 way of using tokens to get the answer
        prize_reached = []
        moves = [AttemptNumber()]

        while len(moves) > 0:
            temp_moves = []
            for move in moves:
                # For each move, create one new move where A is added, and one new move where B is added
                move_a = AttemptNumber()
                move_a.copy(move)
                new_coord = move_a.make_move(1, 0, game.A)
                if new_coord[0] < game.prize[0] and new_coord[1] < game.prize[1]:
                    temp_moves.append(move_a)
                elif new_coord[0] == game.prize[0] and new_coord[1] == game.prize[1]:
                    prize_reached.append(move_a)
                # else if target is exceeded, discard

                move_b = AttemptNumber()
                move_b.copy(move)
                new_coord = move_b.make_move(0, 1, game.B)
                if new_coord[0] < game.prize[0] and new_coord[1] < game.prize[1]:
                    temp_moves.append(move_b)
                elif new_coord[0] == game.prize[0] and new_coord[1] == game.prize[1]:
                    prize_reached.append(move_b)
                # else if target is exceeded, discard
                
            moves = temp_moves.copy()

        if len(prize_reached) == 0:
            return 0

        # find the min tokens used to reach prize
        min_tokens = math.inf
        for prize in prize_reached:
            if prize.tokens_used < min_tokens:
                min_tokens = prize.tokens_used

                



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