# TASK:
# (1) A person should implement the class
# (2) Another person should document the code and type hint the methods.

# NOTE: You can decide the implementation details


class Grid:
    def __init__(self): ...

    def set_cell(self, i, j): ...

    def clear_cell(self, i, j): ...

    def clear_board(self): ...

    @property
    def is_empty(self): ...

    @property
    def is_filled(self): ...

    @property
    def grid(self): ...

    @property
    def row_count(self): ...

    @property
    def column_count(self): ...
