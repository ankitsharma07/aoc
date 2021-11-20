#!/usr/bin/env python3

from __future__ import annotations
from collections import Counter, defaultdict, namedtuple, deque
from itertools import permutations, combinations, product, chain
from functools import lru_cache
from typing import Dict, Tuple, Set, List, Iterator, Optional, Union

import operator
import math
import ast
import sys
import re


class Utility:
    def data(self, day: int, parser=str, sep="\n") -> list:
        """Split the day's input sections separated by `sep` and apply `parser` to each"""
        sections = open(f"data/2020/input{day}.txt").read().rstrip().split(sep)
        return [parser(section) for section in sections]

    def do(self, day, *answers) -> Dict[int, int]:
        """E.g., do(3) returns {1: day3_1(in3), 2: day3_2(in3)}. Verifies `answers` if given."""
        g = globals()
        got = []

        for part in (1, 2):
            fname = f"day{day}_{part}"
            if fname in g:
                got.append(g[fname](g[f"in{day}"]))

                if len(answers) >= part:
                    assert (
                        got[-1] == answers[part - 1]
                    ), f"{fname}(in{day}) got {got[-1]}; expected {answers[part - 1]}"
        return got

    def quantify(self, iterable, pred=bool) -> int:
        """Count the number of items in iterable for which pred is true"""
        return sum(1 for item in iterable if pred(item))

    def first(self, iterable, default=None) -> object:
        """Return the first item in the iterable or default"""
        return next(iter(iterable), default)

    def rest(self, sequence) -> object:
        return sequence[1:]
