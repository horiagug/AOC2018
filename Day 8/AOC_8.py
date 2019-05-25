from header import print_header


def main():
    print_header()

    l = get_data()
    answers = recurse(iter(l))
    print("The answer to part 1 is: {} and to part 2 is : {}".format(answers[0], answers[1]))


def get_data():
    # Store the data in an array
    with open('input') as f:
        data = list(map(int, f.read().split(' ')))
    return data


def recurse(data, sum1=0, sum2=0):
    # Get the number of children and metadata entries
    children_num = next(data)
    metadata_num = next(data)

    # List of child node metadata values
    children = []

    for child in range(children_num):
        sum1, childsum = recurse(data, sum1)
        children.append(childsum)

    for i in range(metadata_num):
        m = next(data)
        sum1 += m
        if children_num == 0:
            sum2 += m
        elif 0 < m <= children_num:
            sum2 += children[m-1]

    return sum1, sum2


if __name__ == '__main__':
    main()
