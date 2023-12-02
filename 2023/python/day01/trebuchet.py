#!/usr/bin/env python3

RAW_INPUT = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""


# RAW DATA
# if __name__ == '__main__':
    # sum = 0
    # for i in RAW_INPUT.strip().split("\n"):
    #     first = None
    #     last = None
    #     for j in i:
    #         if j.isdigit():
    #             last = j
    #             if first is None:
    #                 first = j
    #     sum += int(first + last)

    # print(sum)

if __name__ == '__main__':
    with open ("input_1.txt") as f:
        s = f.read()

    sum = 0
    for i in s.strip().split("\n"):
        first = None
        last = None
        for j in i:
            if j.isdigit():
                last = j
                if first is None:
                    first = j
        sum += int(first + last)
    print(sum)
