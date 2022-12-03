"""Tests for AoC 3, 2022: rucksackreorg."""

# Standard library imports
import pathlib

# Third party imports
import aoc202203
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202203.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202203.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert len(example1) == 6 and example1[5] == "CrZsJsPPZsGzwwsLwLmpwMDw"

def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202203.part1(example1) == 157


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202203.part2(example1) == 70

