#!/usr/bin/env python3

from dataclasses import dataclass

RAW_INPUT = """
        1000
        2000
        3000

        4000

        5000
        6000

        7000
        8000
        9000

        10000
        """

@dataclass
class Elf:
    foods: list[int]

    def calories(self) -> int:
        return sum(self.foods)


def parse(raw: str) -> list[Elf]:
    return [
        Elf([int(x) for x in line.split("\n")])
        for line in raw.strip().split("\n\n")
    ]


if __name__ == '__main__':
    with open("./data/inp_day_1.txt") as f:
        data = parse(f.read())

    print(max(elf.calories() for elf in data))

    # print the calories of first three elves
    print(sum(elf.calories() for elf in sorted(data, key=lambda x: x.calories(), reverse=True)[:3]))
