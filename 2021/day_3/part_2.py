from typing import List


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

def oxygen_generator_rating(numbers: List[str]) -> str:
    m = len(numbers[0])
    
    for i in range(m):
        zeros = 0
        ones = 0
        
        for num in numbers:
            if num[i] == "0":
                zeros += 1
            else:
                ones += 1
        
        if ones >= zeros:
            numbers = [n for n in numbers if n[i] == "1"]
        else:
            numbers = [n for n in numbers if n[i] == "0"]
            
        if len(numbers) == 1:
            return numbers[0]
        
    raise ValueError("No solution found")


def co2_scrubber_rating(numbers: List[str]) -> str:
    m = len(numbers[0])
    
    for i in range(m):
        zeros = 0
        ones = 0
        
        for num in numbers:
            if num[i] == "0":
                zeros += 1
            else:
                ones += 1
        
        if ones >= zeros:
            numbers = [n for n in numbers if n[i] == "0"]
        else:
            numbers = [n for n in numbers if n[i] == "1"]
            
        if len(numbers) == 1:
            return numbers[0]
        
    raise ValueError("No solution found")


def life_support_rating(numbers : List[str]) -> str:
    """Compute the oxygen generator rating and co2 scrubber rating,
    converts them to base 10, and return their product
    """
    return int(oxygen_generator_rating(numbers), 2) * int(co2_scrubber_rating(numbers), 2)



if __name__ == "__main__":
    # assert oxygen_generator_rating(INPUT) == "10111"
    # assert co2_scrubber_rating(INPUT) == "01010"
    # assert life_support_rating(INPUT) == 230

    with open("./../data/in_data_day_3.txt") as f:
        numbers = f.read().splitlines()

    print(life_support_rating(numbers))
