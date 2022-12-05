"""Tests for AoC 5, 2022: supplystacks."""

# Standard library imports
import pathlib

# Third party imports
import aoc202205
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202205.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202205.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert (example1["initialState"][1][2] == "D" and
            example1["numStacks"] == 3 and
            example1["moves"][1][0] == 3)


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202205.part1(example1) == "CMZ"


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202205.part2(example1) == "MCD"
