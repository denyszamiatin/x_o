import numpy as np


class Field:
    def __init__(self):
        self.field = np.empty((3, 3), dtype="U1")
        self.field.fill(' ')

    def __str__(self):
        return "\n".join("".join(row) for row in self.field)

    def __getitem__(self, item):
        return self.field[item]

    def __setitem__(self, key, item):
        if self.field[key] != ' ':
            raise ValueError("cell is occupied")
        self.field[key] = item

    def is_draw(self):
        return np.all(self.field != ' ')

    def is_win(self, char):
        for i in range(3):
            if np.all(self.field[i, :] == char):
                return True
        for i in range(3):
            if np.all(self.field[:, i] == char):
                return True
        if np.all(np.diag(self.field) == char):
            return True
        if np.all(np.diag(np.rot90(self.field)) == char):
            return True
        return False

    def copy(self):
        field = Field()
        field.field = self.field.copy()
        return field

