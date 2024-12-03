def part1():
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

    print("Part 1 Sum = ", multiplication_sum)

def part2():
    multiplication_sum = 0
    do = True

    for line in lines:
        segments = line.split('mul(')

        for segment in segments:
            if (do):
                close_bracket_index = segment.find(')')
                if (close_bracket_index != -1):
                    # found a close bracket - ensure that the contents within the substring are valid
                    # no spaces, just two numbers separated by comma : mul(X,Y)
                    sub_str = segment[0:close_bracket_index]

                    if (sub_str.find(' ') == -1):
                        values = sub_str.split(',')
                        if (len(values) == 2 and values[0].isdigit() and values[1].isdigit()):
                            multiplication_sum += int(values[0]) * int(values[1])

                # search for a don't to see if next segment is disabled
                if (segment.find('don\'t()') != -1):
                    do = False
            else:
                # don't handle multiplications. Look for 'do' to see if it re-enabled
                if (segment.find('do()') != -1):
                    do = True

    print("Part 2 Sum = ", multiplication_sum)

#########################################################################################
with open('C:\SourceCode\AdventOfCode24\Day3\puzzle_input.txt', 'r') as f:
    lines = f.readlines()
part1()
part2()