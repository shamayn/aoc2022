"""AoC 4, 2022: campcleanup."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [ row.split(",") for row in puzzle_input.split("\n") ]

def containsRange(r1, r2):
    range1 = [int(x) for x in r1.split("-")]
    range2 = [int(x) for x in r2.split("-")]
    if max(range1) >= max(range2) and min(range1) <= min(range2):
        return True
    return False

def part1(data):
    """Solve part 1."""
    countContains = 0
    for row in data:
        if containsRange(row[0], row[1]) or containsRange(row[1], row[0]):
            print("found", row)
            countContains += 1
            
    return countContains

def overlapsRange(r1, r2):
    range1 = [int(x) for x in r1.split("-")]
    range2 = [int(x) for x in r2.split("-")]
    if ((min(range2) >= min(range1) and 
        min(range2) <= max(range1)) or 
        (max(range2) >= min(range1) and 
         max(range2) <= max(range1))):
        return True
    return False

def part2(data):
    """Solve part 2."""
    countOverlap = 0
    for row in data:
        if overlapsRange(row[0], row[1]) or overlapsRange(row[1], row[0]):
            print("found", row)
            countOverlap += 1
            
    return countOverlap

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
