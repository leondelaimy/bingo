import bingo
import numpy as np

test_1 = "bingo_raw/test_1.txt"
test_2 = "bingo_raw/test_2.txt"

expected_draws = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
expected_part_1_score = 2192
expected_part_2_score = 4512

def test_parse_raw_file_and_return_draws():
    draws, _ = bingo.parse_raw_file(test_1)
    assert type(draws) is list
    assert all(isinstance(draw, int) for draw in draws)
    assert draws == expected_draws

    draws, _ = bingo.parse_raw_file(test_2)
    assert type(draws) is list
    assert all(isinstance(draw, int) for draw in draws)
    assert draws == expected_draws

def test_parse_raw_file_and_return_boards():
    _, boards = bingo.parse_raw_file(test_1)
    assert type(boards) is list
    assert all(isinstance(board, np.ndarray) for board in boards)
    assert all(board.shape == (5,5) for board in boards)

    _, boards = bingo.parse_raw_file(test_2)
    assert type(boards) is list
    assert all(isinstance(board, np.ndarray) for board in boards)
    assert all(board.shape == (5,5) for board in boards)
    
def test_play_bingo_wins_as_expected():
    idx, result = bingo.play(test_1)
    assert idx == 0
    assert result == expected_part_1_score

    idx, result = bingo.play(test_2)
    assert idx == 2
    assert result == expected_part_2_score

