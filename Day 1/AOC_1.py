from header import print_header


def main():
    print_header()

    compute_frequency()

    compute_duplicate_frequency()


def compute_frequency():
    f0 = 0
    print("Starting the frequency computation ...")
    with open('input') as input_list:
        for line in input_list:
            f0 += int(line)

    print("Final result is: {}".format(f0))


def compute_duplicate_frequency():
    f0 = 0
    runs = 0
    prev = set()
    prev.add(f0)
    print("Starting the computation of duplicates ...")
    while True:
        runs += 1
        print("Went through the entire list of inputs {} times".format(runs))
        with open('input') as input_list:
            for line in input_list:
                f0 += int(line)
                if f0 in prev:
                    print("Got it! The value is: {}".format(f0))
                    return
                else:
                    prev.add(f0)


if __name__ == '__main__':
    main()
