"""AoC 2, 2022: rockpaperscissors."""

# Standard library imports
import pathlib
import sys

# points for outcome - win 6, draw 3, lose 0
# points for choice - rock 1, paper 2, scissors 3
# precedence - rock > scissors, scissors > paper, paper > rock 


points_for_choice = {
    "rock" : 1,
    "paper" : 2,
    "scissors" : 3,
}

win_rules = {
    "rock" : "scissors",
    "scissors" : "paper",
    "paper" : "rock",
}

lose_rules = {
    "rock" : "paper",
    "scissors" : "rock",
    "paper" : "scissors",
}
part1_map_of_moves = {
        "A" : "rock",
        "B" : "paper",
        "C" : "scissors",
        "X" : "rock",
        "Y" : "paper",
        "Z" : "scissors",
}

def parse_data(puzzle_input):
    """Parse input."""
    return [row.split(' ') for row in puzzle_input.split('\n')]

def calculate_score(game):
    outcome = 0
    if (game[0] == game[1]):
        outcome = 3
    elif (win_rules[game[1]] == game[0]):
        # it's a win
        outcome = 6
    else:
        outcome = 0
    return outcome + points_for_choice[game[1]]
 
   
def part1(data):
    """Solve part 1."""
    games = [[ part1_map_of_moves[p1], part1_map_of_moves[p2]] for [p1, p2] in data]
    score = 0
    for game in games:
        score += calculate_score(game)
    return score


# X lose, Y draw, Z win
def part2(data):
    """Solve part 2."""
    games = [[ part1_map_of_moves[p1], p2] for [p1, p2] in data]

    score = 0
    for p1, outcome in games:
        if (outcome == "Y"): # draw
            score += calculate_score([p1, p1])
        elif (outcome == "X"): # lose
            score += calculate_score([p1, win_rules[p1]])
        elif (outcome == "Z"): # win
            score += calculate_score([p1, lose_rules[p1]])
    return score


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
