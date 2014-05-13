"""
Finds a "zigzag" path through a table that represents the highest sum.
E.g.,

    15 + 12 + 7 + 9 = 43

    1   9  3  4
    5   6  7  8
    9  10 11 12
    13 14 15 16

You must start at a cell in the top-row, and move down-left or down-right through each row until the bottom.
Take the sum of the traversed elements.  Find the highest possible sum.
"""


def find_zig_zag(table):
    """
    :param table: an array of rows in the table
    :return: the value of the highest zig-zag
    """
    if not len(table):
        return None

    current_sum = list(table[0])
    for next_row in table[1:]:
        next_row = list(next_row)  # making copy
        for x in range(len(next_row)):
            up_left = current_sum[x-1] if x > 0 else 0
            up_right = current_sum[x+1] if x+1 < len(current_sum) else 0
            next_row[x] = next_row[x] + max(up_left, up_right)
        current_sum = next_row

    return max(current_sum)


def find_zig_zag2(table):
    """
    Version that prints the path through the table
    :param table: an array of rows in the table
    :return: the value of the highest zig-zag
    """
    if not len(table):
        return None

    # creating a table of (value, idx) where idx is the index of the better parent
    matrix = [[(v, None) for v in table[0]]]

    for row in table[1:]:
        next_row = list()
        for x in range(len(row)):
            up_left = matrix[-1][x-1][0] if x > 0 else 0
            up_right = matrix[-1][x+1][0] if x+1 < len(matrix[-1]) else 0
            if up_left > up_right:
                next_row.append((row[x] + up_left, x - 1))
            else:
                next_row.append((row[x] + up_right, x + 1))

        matrix.append(next_row)

    path = list()
    column = max(range(len(matrix[-1])), key=lambda x: matrix[-1][x][0])
    for row in range(len(matrix) - 1, -1, -1):
        value, column = table[row][column], matrix[row][column][1]
        path.append(value)

    return list(reversed(path))

if __name__ == "__main__":

    print find_zig_zag([
        [1, 9, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ])

    print find_zig_zag2([
        [1, 9, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ])