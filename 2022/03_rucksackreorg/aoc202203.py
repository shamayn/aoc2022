"""AoC 3, 2022: rucksackreorg."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input.split('\n')

def part1(data):
    """Solve part 1."""
    priorities = 0

    for row in data:
        c1 = set(row[:int(len(row)/2)])
        c2 = set(row[int(len(row)/2):])
        p = list(c1.intersection(c2))[0]
        priorities += get_priority(p)
    return priorities        

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
def get_priority(p):
    if (p.isupper()):
        return ord(p) - ord("A") + 27
    else:
        return ord(p) - ord("a") + 1

def part2(data):
    """Solve part 2."""
    priorities = 0
    for i in range(0, len(data), 3):
        c = list(set(data[i]) & set(data[i+1]) & set(data[i+2]))[0]
        priorities += get_priority(c)
    return priorities


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
