with open('C:\SourceCode\AdventOfCode24\Day3\puzzle_input.txt', 'r') as f:
    lines = f.readlines()

multiplication_sum = 0

for line in lines:
    segments = line.split('mul(')

    for segment in segments:
        close_bracket_index = segment.find(')')
        if (close_bracket_index != -1):
            # found a close bracket - ensure that the contents within the substring are valid
            # no spaces, just two numbers separated by comma : mul(X,Y)
            sub_str = segment[0:close_bracket_index]

            if (sub_str.find(' ') == -1):
                values = sub_str.split(',')
                if (len(values) == 2 and values[0].isdigit() and values[1].isdigit()):
                    multiplication_sum += int(values[0]) * int(values[1])

print("Sum = ", multiplication_sum)