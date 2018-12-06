

def main():
    print_header()
    # You've managed to sneak in to the prototype suit manufacturing lab. The Elves are making decent progress,
    # but are still struggling with the suit's size reduction capabilities.
    #
    # While the very latest in 1518 alchemical technology might have solved their problem eventually, you can do
    # better. You scan the chemical composition of the suit's material and discover that it is formed by extremely
    # long polymers (one of which is available as your puzzle input).
    #
    # The polymer is formed by smaller units which, when triggered, react with each other such that two adjacent
    # units of the same type and opposite polarity are destroyed. Units' types are represented by letters; units'
    # polarity is represented by capitalization. For instance, r and R are units with the same type but opposite
    # polarity, whereas r and s are entirely different types and do not react.
    #
    # For example:
    #
    #     In aA, a and A react, leaving nothing behind.
    #     In abBA, bB destroys itself, leaving aA. As above, this then destroys itself, leaving nothing.
    #     In abAB, no two adjacent units are of the same type, and so nothing happens.
    #     In aabAAB, even though aa and AA are of the same type, their polarities match, and so nothing happens.
    #
    # Now, consider a larger example, dabAcCaCBAcCcaDA:
    #
    # dabAcCaCBAcCcaDA  The first 'cC' is removed.
    # dabAaCBAcCcaDA    This creates 'Aa', which is removed.
    # dabCBAcCcaDA      Either 'cC' or 'Cc' are removed (the result is the same).
    # dabCBAcaDA        No further actions can be taken.
    #
    # After all possible reactions, the resulting polymer contains 10 units.
    #
    # How many units remain after fully reacting the polymer you scanned? (Note: in this puzzle and others,
    # the input is large; if you copy/paste your input, make sure you get the whole thing.)

    input = open('input').read()
    p1 = polymer(input)
    print("The answer to the first puzzle is: {}".format(p1[1]))

    # --- Part Two ---
    #
    # Time to improve the polymer.
    #
    # One of the unit types is causing problems; it's preventing the polymer from collapsing as much as it should.
    # Your goal is to figure out which unit type is causing the most problems, remove all instances of it (regardless
    #  of polarity), fully react the remaining polymer, and measure its length.
    #
    # For example, again using the polymer dabAcCaCBAcCcaDA from above:
    #
    # Removing all A/a units produces dbcCCBcCcD. Fully reacting this polymer produces dbCBcD, which has length 6.
    # Removing all B/b units produces daAcCaCAcCcaDA. Fully reacting this polymer produces daCAcaDA, which has length
    #  8. Removing all C/c units produces dabAaBAaDA. Fully reacting this polymer produces daDA, which has length 4.
    # Removing all D/d units produces abAcCaCBAcCcaA. Fully reacting this polymer produces abCBAc, which has length 6.
    #
    # In this example, removing all C/c units was best, producing the answer 4.
    #
    # What is the length of the shortest polymer you can produce by removing all units of exactly one type and fully
    # reacting the result?

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


def print_header():
    print("")
    print("######################################")
    print("######## Advent of code day 5 ########")
    print("######################################")
    print("")


if __name__ == '__main__':
    main()
