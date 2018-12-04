
def main():
    print_header()

    # PART 1:
    # The columns are Date, which shows the month-day portion of the relevant day;
    # ID, which shows the guard on duty that day; and Minute, which shows the minutes
    # during which the guard was asleep within the midnight hour.
    # (The Minute column's header shows the minute's ten's digit in the first row and
    # the one's digit in the second row.) Awake is shown as ., and asleep is shown as #.

    # Note that guards count as asleep on the minute they fall asleep, and they count as
    # awake on the minute they wake up. For example, because Guard #10 wakes up at 00:25
    # on 1518-11-01, minute 25 is marked as awake.

    # If you can figure out the guard most likely to be asleep at a specific time, you might
    # be able to trick that guard into working tonight so you can have the best chance of sneaking in.
    # You have two strategies for choosing the best guard/minute combination.

    # Strategy 1: Find the guard that has the most minutes asleep. What minute does that guard spend asleep the most?

    # In the example above, Guard #10 spent the most minutes asleep, a total of 50 minutes
    # (20+25+5), while Guard #99 only slept for a total of 30 minutes (10+10+10).
    # Guard #10 was asleep most during minute 24 (on two days, whereas any other minute
    # the guard was asleep was only seen on one day).

    # While this example listed the entries in chronological order, your entries are in the order
    # you found them. You'll need to organize them before they can be analyzed.

    # What is the ID of the guard you chose multiplied by the minute you chose?
    # (In the above example, the answer would be 10 * 24 = 240.)

    # PART 2:

    # Strategy 2: Of all guards, which guard is most frequently asleep on the same minute?

    # In the example above, Guard #99 spent minute 45 asleep more than any other guard or minute - three times in
    # total. (In all other cases, any guard spent any minute asleep at most twice.)

    # What is the ID of the guard you chose multiplied by the minute you chose? (In the above example, the answer
    # would be 99 * 45 = 4455.)

    input_lines = open('input').read().splitlines()

    input_lines.sort()

    solution(input_lines)


def print_header():
    print("")
    print("######################################")
    print("######## Advent of code day 4 ########")
    print("######################################")
    print("")


def solution(input_lines):
    records = dict()
    guard = None

    for line in input_lines:
        action = line.split('] ')[1]
        time = int(line.split(':')[1][:2])
        if action.startswith('Guard'):
            guard = int(action.split(' ')[1][1:])
            if guard not in records:
                records[guard] = [[0]*60, 0]
        elif action.startswith('falls'):
            records[guard][1] = time
        elif action.startswith('wakes'):
            for i in range(records[guard][1], time):
                records[guard][0][i] += 1

    # part 1
    guard1 = max(records, key=lambda k: sum(records[k][0]))
    minute1 = records[guard1][0].index(max(records[guard1][0]))

    print("Solution to first part is: {}".format(guard1*minute1))

    # part 2
    guard2 = max(records, key= lambda k: max(records[k][0]))
    minute2 = records[guard2][0].index(max(records[guard2][0]))

    print("Solution to second part is: {}".format(guard2*minute2))


if __name__ == '__main__':
    main()
