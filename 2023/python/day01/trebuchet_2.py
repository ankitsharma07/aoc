mapping = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

if __name__ == '__main__':
    with open ("input_1.txt") as f:
        s = f.read()

    # s = """
    # two1nine
    # eightwothree
    # abcone2threexyz
    # xtwone3four
    # 4nineeightseven2
    # zoneight234
    # 7pqrstsixteen
    # """

    sum = 0
    for i in s.strip().split("\n"):
        first = None
        last = None
        s = ""

        for j in i:
            dig = None
            if j.isdigit():
                dig = j
            else:
                s += j
                for k, v in mapping.items():
                    if s.endswith(k):
                        dig = str(v)    # process as digits
            if dig is not None:
                last = dig
                if first is None:
                    first = dig
        sum += int(first + last)
    print(sum)
