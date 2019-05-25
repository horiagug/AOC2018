from collections import defaultdict

from header import print_header


def main():
    print_header()

    # Input is: 452 players; last marble is worth 71250 points
    print("Answer to part 1 is: {}".format(marbles(452, 71250)))

    # Input is: 452 players; last marble is worth 7125000 points
    print("Answer to part 2 is: {}".format(marbles(452, 7125000)))


class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


# Handling normal marbles
def normal_marble(pos, new):
    new.next = pos.next
    new.prev = pos
    pos.next = new
    new.next.prev = new


# Handling deleting a marble
def delete_marble(marble):
    marble.next.prev = marble.prev
    marble.prev.next = marble.next


# Computing the score
def marbles(players, max_marble):

    start = Node(0)
    start.next = start
    start.prev = start

    current = start

    player = 0
    score = defaultdict(int)

    for i in range(1, max_marble):
        new_marble = Node(i)
        # 23 Marble
        if i % 23 == 0:
            # Add score
            score[player] += i

            # Go back 6 steps
            for j in range(6):
                current = current.prev

            # Add score, delete previous marble
            score[player] += current.prev.value
            delete_marble(current.prev)

        # Normal Marble
        else:
            normal_marble(current.next, new_marble)
            current = new_marble

        player = (player + 1) % players

    return max(score.values())


if __name__ == '__main__':
    main()
