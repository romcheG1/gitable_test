dict = {1:['   1  ',
           '  11  ',
           '   1  ',
           '   1  ',
           '   1  ',
           '   1  ',
           '  111 '],
        2:['  222 ',
           ' 2  2 ',
           ' 2  2 ',
           '   2  ',
           '  2   ',
           ' 2    ',
           ' 22222'],
        3:['  333 ',
           ' 3   3',
           '     3',
           '   33 ',
           '     3',
           ' 3   3',
           '  333 '],
        4:['   4  ',
           '  44  ',
           ' 4 4  ',
           '4  4  ',
           '444444',
           '   4  ',
           '   4  '],
        5:['  5555',
           '  5   ',
           '  5   ',
           '  555 ',
           '     5',
           ' 5   5',
           '  555 '],
        6:['  666 ',
           ' 6    ',
           '6     ',
           ' 6666 ',
           '6    6',
           '6    6',
           ' 6666 '],
        7:['777777',
           '    7 ',
           '    7 ',
           '   7  ',
           '   7  ',
           '   7  ',
           '   7  '],
        8:[' 8888 ',
           '8    8',
           '8    8',
           ' 8888 ',
           '8    8',
           '8    8',
           ' 8888 '],
        9:['  999 ',
           ' 9   9',
           ' 9   9',
           '  9999',
           '    9 ',
           '   9  ',
           '  9   '],
        0:['  000  ',
           ' 0   0 ',
           '0     0',
           '0     0',
           '0     0',
           ' 0   0 ',
           '  000  ']}


def print_digit_row(digit, row):
    return dict[digit][row]


line = input()
for j in range(7):
    temp_str = ''
    for dig in line:
        temp_str += print_digit_row(int(dig), j) + ' '
    print(temp_str)

