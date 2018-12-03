def main():
    print_header()

    # After feeling like you've been falling for a few minutes,
    # you look at the device's tiny screen.
    # "Error: Device must be calibrated before first use.
    # Frequency drift detected. Cannot maintain destination lock."
    # Below the message, the device shows a sequence of changes in
    # frequency (your puzzle input). A value like +6 means the current
    # frequency increases by 6;  a value like -3 means the current
    # frequency decreases by 3.
    # Starting with a frequency of zero, what is the resulting frequency
    # after all of the changes in frequency have been applied?
    compute_frequency()

    # You notice that the device repeats the same frequency change list over and over.
    # To calibrate the device, you need to find the first frequency it reaches twice.
    # Note that your device might need to repeat its list of frequency
    # changes many times before a duplicate frequency is found, and that
    # duplicates might be found while in the middle of processing the list.
    compute_duplicate_frequency()


def print_header():
    print("")
    print("######################################")
    print("######## Advent of code day 1 ########")
    print("######################################")
    print("")


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
                    print("Gottem! The value is: {}".format(f0))
                    return
                else:
                    prev.add(f0)


if __name__ == '__main__':
    main()
