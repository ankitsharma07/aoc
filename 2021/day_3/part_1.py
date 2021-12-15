#!/usr/bin/env python3
from typing import List
from collections import Counter

RAW = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

INPUT = RAW.splitlines()  # results in strings


def gamma_rate(nums: List[str]) -> str:
    """Calculate the most common bit for the binary number.

    :param nums: list of binary numbers in string format
    :returns: most common 1's bit

    """
    m = len(nums[0])
    counts = [Counter(num[i] for num in nums) for i in range(m)]

    return "".join(counter.most_common(1)[0][0] for counter in counts)


def epsilon_rate(nums: List[str]) -> str:
    """Calculate the least common bit for the given binary number.

    :param nums: list of binary numbers in string format
    :returns: least common bit

    """
    gr = gamma_rate(nums)
    return "".join("1" if i == "0" else "0" for i in gr)


def power_consumption(nums: List[str]) -> str:
    """Calculate the power consumed by the submarine. Product of gamma rate and epsilon rate.

    :param nums: list of binary numbers in str format
    :returns: prodcut in base 10

    """
    return int(gamma_rate(nums), 2) * int(epsilon_rate(nums), 2)


if __name__ == "__main__":
    # assert gamma_rate(INPUT) == "10110"
    # assert epsilon_rate(INPUT) == "01001"
    # assert power_consumption(INPUT) == 198
    with open("./../data/in_data_day_3.txt") as f:
        numbers = f.read().splitlines()

    print(power_consumption(numbers))
