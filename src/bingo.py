import numpy as np
from itertools import product

def parse_raw_file(file_path: str) -> tuple:
    """
    Parse raw bingo txt file

    draws   Numbers drawn   list(int)
    boards  Playing cards   list(np.ndarray)
    """
    with open(file_path) as fp:
        draws, *boards = fp.read().split("\n\n")
        draws = [int(n) for n in draws.split(",")]
        boards = [np.array([int(n) for n in board.split()]).reshape(5,5) for board in boards]

        return draws, boards

def play(file_path: str) -> tuple:
    """
    Convert board 5x5 matrix into masked array &
    marking the matching drawn values until
    row or column is complete

    idx     Index of winning card   int
    result  Unmarked * last draw    int
    """

    draws, boards = parse_raw_file(file_path)

    for draw, (idx, board) in product(draws, enumerate([np.ma.masked_array(board) for board in boards])):
        board.mask |= board.data == draw
        print(board)

        if np.any(board.mask.sum(0) == 5) or np.any(board.mask.sum(1) == 5):
                result = board.sum()*draw
                break
    
    print(f"Winning board idx: {idx}")
    print("Score", result)
    print("\n")
    return idx, result

    
if __name__ == "__main__":
    play("bingo_raw/test_1.txt")
    play("bingo_raw/test_2.txt")

    
    