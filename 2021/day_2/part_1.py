from dataclasses import dataclass

RAW = """forward 5
down 5
forward 8
up 3
down 8
forward 2
"""

@dataclass
class Command:
    direction: str
    distance: int
    
    @staticmethod
    def from_string(s):
        direction, distance = s.split()
        return Command(direction, int(distance))
    

@dataclass
class Position:
    horizontal: int
    depth: int
    
    def move(self, command):
        if command.direction == 'forward':
            self.horizontal += command.distance
        elif command.direction == 'up':
            self.depth -= command.distance
        elif command.direction == 'down':
            self.depth += command.distance
        else:
            raise ValueError(f'Unknown direction: {command.direction}')
        
COMMANDS = [Command.from_string(s) for s in RAW.splitlines()]

POSITION = Position(0, 0)

for command in COMMANDS:
    POSITION.move(command)
    
assert POSITION.horizontal == 15
assert POSITION.depth == 10

if __name__ == '__main__':
    with open("./../data/in_data_day_2.txt") as f:
        commands = [Command.from_string(s) for s in f.readlines()]
    
    position = Position(0, 0)
    for command in commands:
        position.move(command)
        
    print(position.horizontal * position.depth)
        
    