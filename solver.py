import itertools


combination_choices = []

for i in range(10):
    # thing = '\u2588' * (i + 0) + ' ' * (9 - i - 0)
    thing = '#' * (i + 0) + ' ' * (9 - i - 0)
    # print(len(thing), repr(thing))
    combinations = [''.join(i) for i in set(list(itertools.permutations(thing, 9)))]
    # print(i, combinations)

    combination_choices.append(combinations)


# print(combination_choices)


class Cell:
    def __init__(self, number, x, y):
        self.choices = combination_choices[number][:]
        self.number = number
        self.x = x
        self.y = y

    @classmethod
    def from_choices(cls, choices, x, y):
        new = cls(0, x, y)
        new.choices = choices
        return new

    def compare(self, other):
        dx = other.x - self.x
        dy = other.y - self.y

        # print(f'comparing ({self.x}, {self.y}), ({other.x}, {other.y})')
        # print('comparing', self.choices, other.choices)
        # print('boo', dx, dy)
        # print('boo 1', self, other)

        new_choices = []
        for choice in self.choices:
            for choice2 in other.choices:
                # print('checking pairs', choice, choice2)
                choice_choice2_works = True
                for index in range(9):
                    # index2 = index + dx * 1 + dy * 3
                    #
                    x = index % 3
                    y = int(index / 3)

                    x2 = x - dx
                    y2 = y - dy

                    index2 = x2 + y2 * 3

                    # print(index, dx, dy, x, y, x2, y2)
                    # print(f'index_pairs ({index}, {index2}) c1({x} {y}) c2({x2} {y2})')

                    if x2 < 0 or y2 < 0 or x2 >= 3 or y2 >= 3:
                        continue

                    # print('www')
                    # print('www', x, y)
                    # print('asdf', index, index2)
                    # print('ffff', choice[index], choice2[index2])
                    if choice[index] != choice2[index2]:
                        # print('does not work')
                        choice_choice2_works = False
                #
                if choice_choice2_works:
                    # print('boobobo', choice_choice2_works)
                    new_choices.append(choice)
                    break

        # print('boo 2', self.choices, new_choices)
        if len(new_choices) == 0:
            print('INVALID STATE:')
            print(self.choices, self.x, self.y)
            print(other.choices, other.x, other.y)
            print(':INVALID STATE')
            raise Exception()
        # print('boo 2', len(self.choices), len(new_choices))
        # from pdb import set_trace; set_trace()

        # print('doneee', len(self.choices), len(new_choices))
        # print('doneee', self.choices)
        # print('doneee', new_choices)

        # new_choices = [
        #     choice
        #     for choice, works in zip(self.choices, mask)
        #     if works
        # ]
        self.choices = new_choices

    def mask(self):
        return [
            list(set([c[i] for c in self.choices]))[0]
            if
            len(set([c[i] for c in self.choices])) == 1
            else
            '?'
            for i in range(9)
        ]

    def known_count(self):
        return sum([
            len(set([c[i] for c in self.choices])) == 1 for i in range(9)
        ])

    def __repr__(self):
        return f'<Cell number={self.number} x={self.x} y={self.y} choices={len(self.choices)} known={self.known_count()}>'


class Map:
    def __init__(self):
        self.map = [
            # '     ',
            # ' 52  ',
            # '     ',
            # '7   5',
            # ' 4   ',
            # '  014',

            # '   5 7 '
            # '54 56  ',
            # '     8 ',
            # '  3    ',
            # '   5   ',
            # '4 6  7 ',
            # ' 2   66',
            # '  1  5 ',

            # '    ',
            # ' 41 ',
            # '    ',

            '0 000000000000000000000000000000 0',
            '0                                0',
            '0        1 3 2       4      0 0  0',
            '0  0  0     4   4 3    5  0      0',
            '0    1 4  4 5 6 1 0 0 355    0   0',
            '0     4     35 2     113 5    0  0',
            '0 0  4 42 0 2 3  0   3  3   0    0',
            '0                1024     5   0  0',
            '0 1   2       66 2    3   4      0',
            '0 3 6 1  0 0        33  0 4  0   0',
            '0   52        25     4 1 1    0  0',
            '0  7             7 3 6           0',
            '0 6  24  2 0 2          5 5  0 0 0',
            '0     5 7 3     4  6  78    0    0',
            '0  54 56      42  464   6  0     0',
            '0       8  6   2   6 56 5    0 0 0',
            '0 5  3        3 6 8 8   63       0',
            '0     5    1   77      9   0  0  0',
            '0  4 6  7  4  76      78  1  0   0',
            '0   2   66   8  3 3 35 6   2 2   0',
            '0    1  5        3 3  5   1   2  0',
            '0 0   4     7  2 4       23   43 0',
            '0    1  7 35 4     34  53  7 7 5 0',
            '0          2  2 6 5   7  4       0',
            '0 0    7  4 343   6  7  0   6 75 0',
            '0    2  77       24 55       6   0',
            '0 0     9  4   5  45     146 55  0',
            '0       77    3   5   44 3 76    0',
            '0 0 0 14    52 46 4   35  6 67 3 0',
            '0          4         123     8   0',
            '0         5  8 86  4  2    4  3  0',
            '0  0  0  6   8   3     42 1 5    0',
            '0 0 0  0  6 4 7   5        5     0',
            '0           5  4     357    3 0  0',
            '0          566  014  2    5      0',
            '0 0  0  0 1  6  01  4 2 54     0 0',
            '0     0    3       5  14 3  0    0',
            '0 0      00 3 4 6   4   3      0 0',
            '0    0          8    11   0 0    0',
            '0       0  3   5  55  3 4        0',
            '0  0      0  5 5  6 65  31  0  0 0',
            '0    0  0  1 4 3 3   4 3  0      0',
            '0                                0',
            '0000000000000000000000000000000000',

            # '  9   0  0  0',
            # ' 78  1  0   0',
            # '5 6   2 2   0',
            # ' 5   1   2  0',
            # '    23   43 0',
            # '  53  7 7 5 0',
            # ' 7  4       0',
            # '7  0   6 75 0',
            # '5       6   0',
            # '    146 55  0',
            # ' 44 3 76    0',
            # ' 35  6 67 3 0',
            # '123     8   0',
            # ' 2    4  3  0',
            # '  42 1 5    0',
            # '      5     0',
            # '357    3 0  0',
            # '2    5      0',
            # ' 2 54     0 0',
            # ' 14 3  0    0',
            # '   3      0 0',
            # '11   0 0    0',
            # ' 3 4        0',
            # '5  31  0  0 0',
            # '4 3  0      0',
        ]

        options = []
        self.cells = []
        for y, row in enumerate(self.map):
            option_row = []
            for x, cell in enumerate(row):
                if cell == ' ':
                    option_row.append(None)
                else:
                    number = int(cell)
                    c = Cell(number, x, y)
                    self.cells.append(c)
                    option_row.append(c)
            options.append(option_row)

        self.options = options

    def print(self):
        output = [
            ['?'] * len(self.map[0])
            for i in range(len(self.map))
        ]

        for y, row in enumerate(self.options):
            for x, cell in enumerate(row):
                if cell is None:
                    continue

                mask = cell.mask()

                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if y + dy < 0 or y + dy >= len(self.map):
                            continue
                        if x + dx < 0 or x + dx >= len(self.map[0]):
                            continue
                        cur_val = output[y + dy][x + dx]
                        mask_val = mask[
                            (dx + 1) * 1 +
                            (dy + 1) * 3
                        ]

                        # if cur_val != '?' and mask_val != '?' and cur_val != mask_val:
                        #     print('')
                        #     print('err', x, y, repr(cur_val), '!=', repr(mask_val))
                        #     print('')
                        #     raise Exception()
                        # print(cur_val, mask_val)
                        if mask_val != '?':
                            output[y + dy][x + dx] = mask_val
                # from pdb import set_trace; set_trace()
                # print(x, y, mask)

        print('')
        print('printing map:')
        for l in output:
            print(''.join(l))


    def solve(self):
        for r in range(20):
            print('round', r)
            for y, row in enumerate(self.options):
                for x, cell in enumerate(row):
                    if cell is None:
                        # print('skipping')
                        continue

                    # print(r, cell, cell.mask())

                    for xd, yd in [
                        (-2, -2),
                        (-1, -2),
                        (0, -2),
                        (1, -2),
                        (2, -2),

                        (-2, -1),
                        (-1, -1),
                        (0, -1),
                        (1, -1),
                        (2, -1),

                        (-2, 0),
                        (-1, 0),
                        (1, 0),
                        (2, 0),

                        (-2, 1),
                        (-1, 1),
                        (0, 1),
                        (1, 1),
                        (2, 1),

                        (-2, 2),
                        (-1, 2),
                        (0, 2),
                        (1, 2),
                        (2, 2),
                    ]:
                        x2 = x + xd
                        y2 = y + yd
                        if x2 < 0 or y2 < 0:
                            continue
                        try:
                            cell2 = self.options[y2][x2]
                        except IndexError:
                            # print('  skipping 1')
                            continue
                        if cell2 is None:
                            # print('  skipping 2')
                            continue

                        # print('analyzing', cell, cell2)
                        assert cell.x == x
                        assert cell.y == y
                        assert cell2.x == x2
                        assert cell2.y == y2

                        # self.print()
                        # print('bobobob', x, y, r)
                        # print('bobobob', cell)
                        # print('bobobob', cell2)
                        # if (
                        #     x == 3 and
                        #     y == 2 and
                        #     cell2.x == 2 and
                        #     cell2.y == 3
                        # ):
                        #     self.print()
                        #     from pdb import set_trace; set_trace()
                        #     cell.compare(cell2)
                        #     cell2.compare(cell)
                        #     self.print()
                        #     # from pdb import set_trace; set_trace()
                        cell.compare(cell2)
                        cell2.compare(cell)
                        # self.print()
            self.print()



# c1 = Cell.from_choices(
#     ['---#--#--', '#--#-----', '---#---#-', '#-----#--', '------##-', '----#-#--', '#---#----', '#------#-', '---##----'],
#     3,
#     2,
# )
# c2 = Cell.from_choices(
#     ['------#--', '-------#-', '--#------', '#--------', '---#-----', '-#-------', '----#----', '-----#---', '--------#'],
#     2,
#     3,
# )
#
# c1.compare(c2)
# c2.compare(c1)
# print(c1.x, c1.y, c1.choices)
# print(c2.x, c2.y, c2.choices)
# print(c1.mask())
# print(c2.mask())


# c1 = Cell.from_choices(
#     ['---------'], 3, 0,
#     # ['---------'], 5, 1
#     # ['---------'], 3, 0
# )
# c2 = Cell.from_choices(
#     ['##-------', '#---#----', '#----#---'], 3, 2,
#     # ['----#--#-', '----#---#', '---#----#', '---#-#---', '---#---#-', '----#-#--', '---#--#--', '----##---'], 3, 2
#     # ['#---#----', '#------#-', '#--#-----'], 3, 2
# )
# c1.compare(c2)
# print(c1.choices)
# print(c2.choices)

# c2.compare(c1)
# print(c1.choices)
# print(c2.choices)

my_map = Map()
my_map.solve()
my_map.print()

# print(my_map.cells[0])
# print(''.join(my_map.cells[0].mask()))
# print(my_map.cells[3])
# print(''.join(my_map.cells[3].mask()))
# print(my_map.cells[6])
# print(''.join(my_map.cells[6].mask()))
#
# print(my_map.cells[0].choices, my_map.cells[0].x, my_map.cells[0].y)
# print(my_map.cells[6].choices, my_map.cells[6].x, my_map.cells[6].y)
#
# my_map.cells[0].compare(my_map.cells[6])
# my_map.cells[6].compare(my_map.cells[1])




