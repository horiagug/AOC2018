from collections import defaultdict
from functools import reduce

from header import print_header


def main():
    print_header()

    print("Answer to part one: {}".format(assembly_steps(1)))


    print("Answer to part two: {}".format(assembly_steps(5)))


def available_work(IDs, closes):
    a = []
    for ID in IDs:
        if not closes[ID]:
            a.append(ID)
    return a


def assembly_steps(workers):
    with open('input') as f:
        lines = f.readlines()

    steps = []
    for line in lines:
        x = line.split("must")[0][-2:-1]
        y = line.split("can")[0][-2:-1]
        steps.append((x, y))

    # Figure out what Node opens and closes another
    opens = defaultdict(list)
    closes = defaultdict(list)

    for s in steps:
        opens[s[0]].append(s[1])
        closes[s[1]].append(s[0])

    # Get all the IDs involved and sort them
    alpha = set(reduce(lambda a, b: a+b, steps))
    IDs = list(alpha)
    IDs.sort()
    IDs = ''.join(IDs)

    # Go through all the IDs and check if the Node is open, if so remove the nodes it closes
    result = ''
    work_in_progress = {}

    for sec in range(9999999):

        # Manage Tasks and workers:
        for task in work_in_progress:
            if work_in_progress[task] == 1:
                work_in_progress[task] -= 1
                workers += 1
                result += task
                for clean in opens[task]:
                    closes[clean].remove(task)

            elif work_in_progress[task] > 0:
                work_in_progress[task] -= 1

        aw = sorted(available_work(IDs, closes))

        # Assign workers stuff to do
        for ID in aw:
            if ID not in work_in_progress and workers > 0:
                    work_in_progress[ID] = ord(ID) - 64 + 60
                    workers -= 1
                    IDs = IDs.replace(ID, "")

        # Check if there is no more work and nothing in progress
        if len(aw) == 0 and sum(work_in_progress.values()) == 0:
            return sec, result


if __name__ == '__main__':
    main()
