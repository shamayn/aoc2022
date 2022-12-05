"""AoC 5, 2022: supplystacks."""

# Standard library imports
import pathlib
import sys
import copy


def parse_data(puzzle_input):
    """Parse input."""
    lines = puzzle_input.splitlines()
    i = 0
    initialState = []
    while (lines[i][1] != "1"):
        initialState.append(lines[i])
        i += 1
    numbers = lines[i].strip()
    numStacks = int(numbers[len(numbers) - 1])
    moves = lines[i+2:]
    return { "initialState": parseInitialState(initialState, numStacks), 
            "numStacks": numStacks,
            "moves": parseMoves(moves)}
    
def parseInitialState(rawstate, numStacks):
    stacks = [[] for i in range(numStacks)]

    for j in range(len(rawstate)-1, -1, -1):
        # [Z] [M] [P] [Q]
        #  1   5   9   13 => x starts from 1 and increments by 4
        x = 1
        while x < len(rawstate[j]):
            if rawstate[j][x] != " ":
                stackToUpdate = int((x - 1)/4)
                stacks[stackToUpdate].append(rawstate[j][x])
            x += 4
    return stacks

# format each row into an array of [move, from, to]
def parseMoves(rawmoves):
    moves = []
    for i in range(len(rawmoves)):
        moves.append([])
        for item in rawmoves[i].split(" "):
            if item.isdecimal():
                moves[i].append(int(item))
    return moves
    
def part1(data):
    """Solve part 1."""
    state = copy.deepcopy(data["initialState"])                  
    moves = data["moves"]

    for m in moves:
        for i in range(m[0]): # number to move
            popout = state[m[1]-1].pop()
            state[m[2]-1].append(popout)
        
    result = ""

    return ''.join([result + x.pop() for x in state])

def part2(data):
    """Solve part 2."""
    state = copy.deepcopy(data["initialState"])                      
    moves = data["moves"]
    for m in moves:
        popout = []
        for i in range(m[0]): # number to move
            popped = state[m[1]-1].pop()
            popout.append(popped)
        popout.reverse()
        state[m[2]-1] += popout
        
    result = ""
    return ''.join([result + x.pop() for x in state])   

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
