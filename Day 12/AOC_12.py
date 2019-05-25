from header import print_header


def main():
    print_header()

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


if __name__ == '__main__':
    main()
