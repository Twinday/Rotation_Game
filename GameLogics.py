import random as rnd
import static as s

class Level:
    def __init__(self):
        self.lup = (0, 0)
        self.width = 2
        self.height = 2
        self.matrix = list()
        self.GameWidth = 6
        self.GameHeight = 6
        self.score = 0

    def create_level(self):
        self.matrix.clear()
        for i in range(self.GameHeight):
            row = []
            for j in range(self.GameWidth):
                row.append(self._random_block())
            self.matrix.append(row)
        self._good_situation()
        self.score = 0

    def _random_block(self):
        return rnd.randint(1, 8)
        pass

    def move_border(self, side):
        map = {
            'up': (self.lup[0] - 1, self.lup[1]),
            'down': (self.lup[0] + 1, self.lup[1]),
            'left': (self.lup[0], self.lup[1] - 1),
            'right': (self.lup[0], self.lup[1] + 1)
        }

        if side == 'up':
            if self.lup[0] > 0:
                self.lup = map[side]
        if side == 'down':
            if self.lup[0] + self.height - 1 < len(self.matrix) - 1:
                self.lup = map[side]
        if side == 'left':
            if self.lup[1] > 0:
                self.lup = map[side]
        if side == 'right':
            if self.lup[1] + self.width - 1 < len(self.matrix[0]) - 1:
                self.lup = map[side]

    def _rotate_border(self):
        a = list()
        for i in range(self.lup[0], self.lup[0] + self.height):
            row = list()
            for j in range(self.lup[1], self.lup[1] + self.width):
                row.append(self.matrix[i][j])
            a.append(row)
        b = tuple(zip(*a[::-1]))
        i2 = 0
        j2 = 0
        for i1 in range(self.lup[0], self.lup[0] + self.height):
            for j1 in range(self.lup[1], self.lup[1] + self.height):
                self.matrix[i1][j1] = b[i2][j2]
                j2 += 1
            i2 += 1
            j2 = 0

    def _delete_4_more_same_blocks(self):
        flag = []
        flag.append(False)
        new_matrix = s.matrix_neigbor(self.matrix)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if new_matrix[i][j] > 2:
                    self.score += 100
                    self.matrix[i][j] = 0
                    flag.append(True)

        if flag[-1]:
            return True
        else:
            return False

    def _check_empty_block_in_middle(self, column):
        indexes = []
        for row in range(len(self.matrix)):
            if self.matrix[row][column] == 0:
                indexes.append(row)

        if len(indexes) > 0:
            return (True, indexes)
        else:
            return (False, indexes)

    def _shift(self, lst, steps):
        if steps < 0:
            steps = abs(steps)
            for i in range(steps):
                lst.append(lst.pop(0))
        else:
            for i in range(steps):
                lst.insert(0, lst.pop())

    def _shift_empty_blocks(self, column, indexes):
        for i in indexes:
            a = []
            for row in range(i + 1):
                a.append(self.matrix[row][column])
            self._shift(a, 1)
            for k in range(i + 1):
                self.matrix[k][column] = a[k]

    def _check_empty_block_in_middle_in_all_columns(self):
        for col in range(len(self.matrix[0])):
            flag = self._check_empty_block_in_middle(col)
            if flag[0]:
                self._shift_empty_blocks(col, flag[1])

    def update(self):
        self._rotate_border()
        self._good_situation()
        """self._delete_4_more_same_blocks()
        self._check_empty_block_in_middle_in_all_columns()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == 0:
                    self.matrix[i][j] = self._random_block()"""

        pass

    def _good_situation(self):
        flag = self._delete_4_more_same_blocks()
        self._check_empty_block_in_middle_in_all_columns()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == 0:
                    self.matrix[i][j] = self._random_block()

        while self._delete_4_more_same_blocks():
            self._check_empty_block_in_middle_in_all_columns()
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    if self.matrix[i][j] == 0:
                        self.matrix[i][j] = self._random_block()
        pass

    def getGameWidth(self):
        return self.GameWidth

    def getGameHeight(self):
        return self.GameHeight

    def __getitem__(self, key):
        return self.matrix[key[0]][key[1]]

    def getRect(self):
        return (self.lup, self.width, self.height)

    def get_score(self):
        return self.score
