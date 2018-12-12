

def main():
    print_header()

    rules = dict()
    initial_state = '##.#.####..#####..#.....##....#.#######..#.#...........#......##...##.#...####..##.#..##.....#..####'
    with open('input') as f:
        for line in f.readlines():
            line = line.strip('\n')
            a = list()
            res = line.split('=>')
            for c in res[0]:
                a.append(1 if c == '#' else 0)
            rules[(a[0], a[1], a[2], a[3], a[4])] = 1 if res[1][1:] == '#' else 0

    state = set()
    index = 0
    for c in initial_state:
        if c == '#':
            state.add(index)
            index += 1
        else:
            index +=1

    for i in range (1, 21):
        new_state = set()
        for index in range(min(state), max(state)+1):
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
        state = new_state

    print(sum(state))












def print_header():
    print("")
    print("######################################")
    print("####### Advent of code day 11 ########")
    print("######################################")
    print("")


if __name__ == '__main__':
    main()
