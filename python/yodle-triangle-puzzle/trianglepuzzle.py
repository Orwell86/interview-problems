"""
Solves the Yodle triangle puzzle, e.g.:

By starting at the top of the triangle and moving to adjacent numbers on the row below, the maximum total from top to bottom is 27.

        5
      9  6
    4   6  8
  0   7  1   5

I.e. 5 + 9 + 6 + 7 = 27.
"""
import sys


def find_triangle_path(values):
    """
    :param values: an array of integers conforming to a triangle shape.  i.e., [1 2 3 4 5 6 7] would be a triangle with three levels.
    :return: the sequence of values forming the highest total; e.g. [1 3 7] for the input [1 2 3 4 5 6 7]
    """
    if not len(values):
        return []

    if len(values) == 1:
        return values

    # keeps the interrim sums of the triangle
    temp_sums = [None for _ in xrange(len(values))]

    # initialize the root
    temp_sums[0] = values[0]

    def _right_parent_index(index, level):
        """Helper function to calculate the right parent index"""
        return index - level

    def _left_parent_index(index, level):
        """Helper function to calculate the left parent index"""
        return index - level - 1

    for level in xrange(1, sys.maxint):
        # these are the bounds of the level within the array
        level_start = level * (level + 1) / 2
        level_end = level_start + level

        assert level_end < len(values), 'Input is not validly formed'

        # level_start and level_end only have a single path to choose
        temp_sums[level_start] = values[level_start] + temp_sums[_right_parent_index(level_start, level)]
        temp_sums[level_end] = values[level_end] + temp_sums[_left_parent_index(level_end, level)]

        # nodes between level_start and level_end are based on either the left or right parent
        for index in xrange(level_start + 1, level_end):
            left_parent_index = _left_parent_index(index, level)
            right_parent_index = _right_parent_index(index, level)
            high_parent_index = left_parent_index if temp_sums[left_parent_index] >= temp_sums[right_parent_index] else right_parent_index
            temp_sums[index] = values[index] + temp_sums[high_parent_index]

        # if we are on the last level, determine which leaf has the highest path, and unwind
        if level_end + 1 == len(values):
            # find the leaf with the highest sum
            return max([temp_sums[x] for x in xrange(level_start, level_end + 1)])

if __name__ == "__main__":

    tests = [
        ([5, 9, 6, 4, 6, 8, 0, 7, 1, 5], 27),
        ([1, 2, 3], 4),
        ([1, 2, 3, 7, 6, 5], 10)]

    for values, expected in tests:
        result = find_triangle_path(values)
        print "%s -> %s" % (values, result)
        assert result == expected, 'Expected sum for %s is %s but got %s' % (values, expected, result)
