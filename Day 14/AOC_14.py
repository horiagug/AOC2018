# CONSTANTS
from header import print_header

INPUT = 513401


def main():
    print_header()
    print("Answer to part 1 is: {}".format(solve(INPUT, True)))
    print("Answer to part 2 is: {}".format(solve(INPUT)))


def solve(INPUT, part1=False):
    input_list = []
    scores = [3, 7]
    elf1_index = 0
    elf2_index = 1
    for i in str(INPUT):
        input_list.append(int(i))

    while True:
        # compute the score of the new recipe add it to list of scores
        new_recipe = scores[elf1_index] + scores[elf2_index]
        if new_recipe < 10:
            scores.append(new_recipe)
        elif new_recipe >= 10:
            scores.append(int(new_recipe/10))
            scores.append(new_recipe % 10)

        # compute new indices
        new_index = 1 + scores[elf1_index]
        if new_index > len(scores) - 1:
            elf1_index = (elf1_index + (new_index % len(scores))) % len(scores)
        else:
            elf1_index = (elf1_index + new_index) % len(scores)

        new_index = 1 + scores[elf2_index]
        if new_index > len(scores) - 1:
            elf2_index = (elf2_index + (new_index % len(scores))) % len(scores)
        else:
            elf2_index = (elf2_index + new_index) % len(scores)

        if part1:
            if INPUT + 10 < len(scores):
                result = ''
                for i in range(1, 11):
                    result += str((scores[INPUT - 1 + i]))
                return result

        found1 = False
        found2 = False

        # Check last scores
        for i in range(len(input_list)):
            if input_list[i] == scores[len(scores) - len(input_list) + i]:
                found1 = True
            else:
                found1 = False
                break

        # Check up to second to last scores
        for i in range(len(input_list)):
            if input_list[i] == scores[len(scores) - len(input_list) + i - 1]:
                found2 = True
            else:
                found2 = False
                break

        if found1:
            return len(scores) - len(input_list)
        if found2:
            return len(scores) - len(input_list) - 1


if __name__ == '__main__':
    main()
