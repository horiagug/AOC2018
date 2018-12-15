

def main():
    print_header()

    # The year 518 is significantly more underground than your history books implied. Either that, or you've arrived
    # in a vast cavern network under the North Pole.
    #
    # After exploring a little, you discover a long tunnel that contains a row of small pots as far as you can see to
    #  your left and right. A few of them contain plants - someone is trying to grow things in these
    # geothermally-heated caves.
    #
    # The pots are numbered, with 0 in front of you. To the left, the pots are numbered -1, -2, -3, and so on; to the
    #  right, 1, 2, 3.... Your puzzle input contains a list of pots from 0 to the right and whether they do (#) or do
    #  not (.) currently contain a plant, the initial state. (No other pots currently contain plants.) For example,
    # an initial state of #..##.... indicates that pots 0, 3, and 4 currently contain plants.
    #
    # Your puzzle input also contains some notes you find on a nearby table: someone has been trying to figure out
    # how these plants spread to nearby pots. Based on the notes, for each generation of plants, a given pot has or
    # does not have a plant based on whether that pot (and the two pots on either side of it) had a plant in the last
    #  generation. These are written as LLCRR => N, where L are pots to the left, C is the current pot being
    # considered, R are the pots to the right, and N is whether the current pot will have a plant in the next
    # generation. For example:
    #
    # A note like ..#.. => . means that a pot that contains a plant but with no plants within two pots of it will not
    #  have a plant in it during the next generation. A note like ##.## => . means that an empty pot with two plants
    # on each side of it will remain empty in the next generation. A note like .##.# => # means that a pot has a
    # plant in a given generation if, in the previous generation, there were plants in that pot, the one immediately
    # to the left, and the one two pots to the right, but not in the ones immediately to the right and two to the left.
    #
    # It's not clear what these plants are for, but you're sure it's important, so you'd like to make sure the
    # current configuration of plants is sustainable by determining what will happen after 20 generations.
    #
    # For example, given the following input:
    #
    # initial state: #..#.#..##......###...###
    #
    # ...## => #
    # ..#.. => #
    # .#... => #
    # .#.#. => #
    # .#.## => #
    # .##.. => #
    # .#### => #
    # #.#.# => #
    # #.### => #
    # ##.#. => #
    # ##.## => #
    # ###.. => #
    # ###.# => #
    # ####. => #
    #
    # For brevity, in this example, only the combinations which do produce a plant are listed. (Your input includes
    # all possible combinations.) Then, the next 20 generations will look like this:
    #
    #                  1         2         3
    #        0         0         0         0
    #  0: ...#..#.#..##......###...###...........
    #  1: ...#...#....#.....#..#..#..#...........
    #  2: ...##..##...##....#..#..#..##..........
    #  3: ..#.#...#..#.#....#..#..#...#..........
    #  4: ...#.#..#...#.#...#..#..##..##.........
    #  5: ....#...##...#.#..#..#...#...#.........
    #  6: ....##.#.#....#...#..##..##..##........
    #  7: ...#..###.#...##..#...#...#...#........
    #  8: ...#....##.#.#.#..##..##..##..##.......
    #  9: ...##..#..#####....#...#...#...#.......
    # 10: ..#.#..#...#.##....##..##..##..##......
    # 11: ...#...##...#.#...#.#...#...#...#......
    # 12: ...##.#.#....#.#...#.#..##..##..##.....
    # 13: ..#..###.#....#.#...#....#...#...#.....
    # 14: ..#....##.#....#.#..##...##..##..##....
    # 15: ..##..#..#.#....#....#..#.#...#...#....
    # 16: .#.#..#...#.#...##...#...#.#..##..##...
    # 17: ..#...##...#.#.#.#...##...#....#...#...
    # 18: ..##.#.#....#####.#.#.#...##...##..##..
    # 19: .#..###.#..#.#.#######.#.#.#..#.#...#..
    # 20: .#....##....#####...#######....#.#..##.
    #
    # The generation is shown along the left, where 0 is the initial state. The pot numbers are shown along the top,
    # where 0 labels the center pot, negative-numbered pots extend to the left, and positive pots extend toward the
    # right. Remember, the initial state begins at pot 0, which is not the leftmost pot used in this example.
    #
    # After one generation, only seven plants remain. The one in pot 0 matched the rule looking for ..#..,
    # the one in pot 4 matched the rule looking for .#.#., pot 9 matched .##.., and so on.
    #
    # In this example, after 20 generations, the pots shown as # contain plants, the furthest left of which is pot
    # -2, and the furthest right of which is pot 34. Adding up all the numbers of plant-containing pots after the
    # 20th generation produces 325.

    # --- Part Two ---
    #
    # You realize that 20 generations aren't enough. After all, these plants will need to last another 1500 years to
    # even reach your timeline, not to mention your future.
    #
    # After fifty billion (50000000000) generations, what is the sum of the numbers of all pots which contain a plant?

    rules = get_rules()
    print("Answer to first part is: {}".format(compute(rules, 20)[0]))

    # [0] = sum at pattern, [1] number of points [2]index
    part2 = compute(rules, 50000000000)

    print("Answer to second part is: {}".format(((50000000000 - part2[2]) * part2[1]) + part2[0]))


def get_rules():
    rules = dict()
    with open('input') as f:
        for line in f.readlines():
            line = line.strip('\n')
            a = list()
            res = line.split('=>')
            for c in res[0]:
                a.append(1 if c == '#' else 0)
            rules[(a[0], a[1], a[2], a[3], a[4])] = 1 if res[1][1:] == '#' else 0
    return rules


def compute(rules, generations):
    initial_state = '##.#.####..#####..#.....##....#.#######..#.#...........#......##...##.#...####..##.#..##.....#..####'
    state = set()
    index = 0
    for c in initial_state:
        if c == '#':
            state.add(index)
            index += 1
        else:
            index +=1

    old_string = 'start'

    for i in range(1, generations + 1):
        string = ''
        new_state = set()
        for index in range(min(state) - 2, max(state)+3):
            for rule in rules:
                is_respected = False
                for x in range(5):
                    # if the rule's value is 1 and the position index is in state
                    if rule[x] == 1 and index + x - 2 in state:
                        is_respected = True
                    # if the rule's value is 0 and the position index is not in state
                    elif rule[x] == 0 and index + x - 2 not in state:
                        is_respected = True
                    else:
                        is_respected = False

                    # No point in verifying all the rule's conditions if one is already not met
                    if not is_respected:
                        break

                if is_respected:
                    if rules.get(rule) == 1:
                        new_state.add(index)
                    break

        for j in range(min(new_state), max(new_state) + 1):
            if j in new_state: string += '#'
            else: string += '.'

        if old_string == string:
            print('Pattern detected at: {}'.format(i))
            return sum(new_state), len(new_state), i

        old_string = string

        state = new_state
    return sum(state), len(state), 0


def print_header():
    print("")
    print("######################################")
    print("####### Advent of code day 12 ########")
    print("######################################")
    print("")


if __name__ == '__main__':
    main()
