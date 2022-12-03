"""AoC 1, 2022: caloriecounter."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    cals = []
    for elfcals in puzzle_input.split("\n\n"):
        cal = sum([int(c) for c in elfcals.split("\n")])  
        cals.append(cal)
    return cals

def part1(data):
    """Solve part 1."""
    return max(data)

def part2(data):
    """Solve part 2."""
    data.sort()
    return sum(data[-3:])

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
