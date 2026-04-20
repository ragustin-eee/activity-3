from typing import List, Any

class Grid:
    def __init__(self, rows: int = 5, cols: int = 5):
        self._rows = rows
        self._cols = cols
        # Initialize with empty strings or dots for visual clarity
        self._grid = [[" " for _ in range(cols)] for _ in range(rows)]

    def set_cell(self, i: int, j: int, value: Any) -> None:
        if 0 <= i < self._rows and 0 <= j < self._cols:
            self._grid[i][j] = value

    def clear_cell(self, i: int, j: int) -> None:
        self.set_cell(i, j, " ")

    def clear_board(self) -> None:
        self._grid = [[" " for _ in range(self._cols)] for _ in range(self._rows)]

    @property
    def is_empty(self) -> bool:
        return all(cell == " " for row in self._grid for cell in row)

    @property
    def grid(self) -> List[List[Any]]:
        return self._grid

    @property
    def row_count(self) -> int:
        return self._rows

    @property
    def column_count(self) -> int:
        return self._cols