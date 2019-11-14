def opposite_char(char):
    return 'O' if char == 'X' else 'X'


class Bot:
    def __init__(self, char):
        self.char = char

    def move(self, field):
        free_cells = [(x, y) for x in range(3) for y in range(3) if field[x, y] == ' ']
        for x, y in free_cells:
            test_field = field.copy()
            test_field[x, y] = self.char
            if test_field.is_win(self.char):
                return x, y
        for x, y in free_cells:
            test_field = field.copy()
            test_field[x, y] = opposite_char(self.char)
            if test_field.is_win(opposite_char(self.char)):
                return x, y
        if (1, 1) in free_cells:
            return (1, 1)
        for pos in [(0, 0), (0, 2), (2, 0), (2, 2)]:
            if pos in free_cells:
                return pos
        return free_cells[0]
