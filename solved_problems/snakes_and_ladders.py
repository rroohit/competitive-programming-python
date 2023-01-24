from collections import deque
from typing import List


def snakesAndLadders(board: List[List[int]]) -> int:
    length = len(board)
    n = length * length

    board.reverse()

    def cell_to_position(cell):
        r = (cell - 1) // length
        c = (cell - 1) % length

        if r % 2:
            c = length - 1 - c

        return [r, c]

    q = deque()
    q.append([1, 0])  # [cell, moves]
    visit = set()

    while q:
        cell, moves = q.popleft()

        for i in range(1, 7):
            next_cell = cell + i

            r, c = cell_to_position(next_cell)

            if board[r][c] != -1:
                next_cell = board[r][c]

            if next_cell == n:
                return moves + 1

            if next_cell not in visit:
                visit.add(next_cell)
                q.append([next_cell, moves + 1])

    return -1


board_matrix = [[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1],
                [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]

print(snakesAndLadders(board_matrix))
