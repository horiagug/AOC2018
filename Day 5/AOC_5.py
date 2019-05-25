from header import print_header


def main():
    print_header()
    input = open('input').read()
    p1 = polymer(input)
    print("The answer to the first puzzle is: {}".format(p1[1]))

    p2 = biggest_reaction(p1[0])
    print("The answer to the second part of the puzzle is: {}".format(p2))


def react(a, b):
    # If characters are different
    if a.lower() != b.lower():
        return False

    # If first is lower and second is upper
    elif a.islower() and not b.islower():
        return True
    # If first is upper and second is lower
    elif not a.islower() and b.islower():
        return True

    # If both are the same
    return False


def snip(input, a):
    input = input[:a] + "" + input[a+1:]
    input = input[:a] + "" + input[a+1:]
    return input


def scan_for_reaction(input):
    for c in range(len(input) - 1):
        if react(input[c], input[c+1]):
            return True, c

    return False, 0


def polymer(input):
    while True:
        result = scan_for_reaction(input)
        if result[0]:
            input = snip(input, result[1])
        elif not result[0]:
            return input, len(input)


def biggest_reaction(input):
    smallest_polymer = 50000
    for n in range (65, 91):
        ch = chr(n)
        size = polymer(input.replace(ch.lower(), "").replace(ch.upper(), ""))[1]

        if size < smallest_polymer:
            smallest_polymer = size
    return smallest_polymer


if __name__ == '__main__':
    main()
