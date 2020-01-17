# ----------------------------------------------------------------------
# Name:       homework 3
#
# Purpose:    Implement different functions for matrices
#
# Date:       Spring 2019
# ----------------------------------------------------------------------
"""
Implement different functions for matrices

1.  Count how many times a certain value appears in a matrix
2.  Return a set of adjacent elements of a certain
    coordinate in a matrix
3.  Return a matrix with the values of an image that is blurred
"""
import copy


def count_matrix(matrix, value):
    """Counts how many times a certain value appears in the matrix.

    :param matrix: a nested list of numbers
    :param value: a specific number we count for appearances
    :return: count - how many times the value appears
    """
    count = 0
    for row in matrix:
        for column in row:
            if column == value:
                count = count + 1
    return count


def adjacent(matrix, tuple):
    """Creates a set of adjacent tuples to a tuple in a matrix.

    :param matrix: a nested list of numbers
    :param tuple: a specific tuple in the matrix
    :return: a set of tuples of adjacent tuples
    """
    if not matrix:  # empty matrix
        return None
    # below I am creating tuples of possible adjacent values
    # of the matrix
    tuple_one = (tuple[0] + 1, tuple[1])  # down
    tuple_two = (tuple[0], tuple[1] + 1)  # next to right
    tuple_three = (tuple[0] + 1, tuple[1] + 1)  # diagonal down right
    tuple_four = (tuple[0], tuple[1] - 1)  # next to left
    tuple_five = (tuple[0] - 1, tuple[1])  # up
    tuple_six = (tuple[0] + 1, tuple[1] - 1)  # diagonal down left
    tuple_seven = (tuple[0] - 1, tuple[1] + 1)  # diagonal up right
    tuple_eight = (tuple[0] - 1, tuple[1] - 1)  # diagonal up left
    set_tuple = set()  # create empty set of tuples to add adjacent
    # tuples of the inputted tuple
    # here I am checking to see if each tuple I created is valid to
    # the inputted tuple in the matrix
    if len(matrix) > tuple_one[0]:  # down
        # the if statement under this checks if the element in the
        # matrix is 0 because 0 is seen as false so without this
        # the elements with 0 won't be added to the set
        # the statement next to the "or" checks to see if
        # the element has a value other than 0
        if matrix[tuple_one[0]][tuple_one[1]] == 0 or \
                matrix[tuple_one[0]][tuple_one[1]]:
            set_tuple.add(tuple_one)  # if valid then add to the set
    if len(matrix[0]) > tuple_two[1]:  # next to right
        if matrix[tuple_two[0]][tuple_two[1]] == 0 or \
                matrix[tuple_two[0]][tuple_two[1]]:
            set_tuple.add(tuple_two)
    if len(matrix) > tuple_three[0]:  # diagonal down right
        if len(matrix[0]) > tuple_three[1]:
            if matrix[tuple_three[0]][tuple_three[1]] == 0 or \
                    matrix[tuple_three[0]][tuple_three[1]]:
                set_tuple.add(tuple_three)
    if len(matrix[0]) > tuple_four[1] >= 0:  # next to left
        if matrix[tuple_four[0]][tuple_four[1]] == 0 or \
                matrix[tuple_four[0]][tuple_four[1]]:
            set_tuple.add(tuple_four)
    if len(matrix) > tuple_five[0] >= 0:  # up
        if matrix[tuple_five[0]][tuple_five[1]] == 0 or \
                matrix[tuple_five[0]][tuple_five[1]]:
            set_tuple.add(tuple_five)
    if len(matrix) > tuple_six[0]:  # diagonal down left
        if len(matrix[0]) > tuple_six[1] >= 0:
            if matrix[tuple_six[0]][tuple_six[1]] == 0 or \
                    matrix[tuple_six[0]][tuple_six[1]]:
                set_tuple.add(tuple_six)
    if len(matrix) > tuple_seven[0] >= 0:  # diagonal up right
        if len(matrix[0]) > tuple_seven[1]:
            if matrix[tuple_seven[0]][tuple_seven[1]] == 0 or \
                    matrix[tuple_seven[0]][tuple_seven[1]]:
                set_tuple.add(tuple_seven)
    if len(matrix) > tuple_eight[0] >= 0:  # diagonal up left
        if len(matrix[0]) > tuple_eight[1] >= 0:
            if matrix[tuple_eight[0]][tuple_eight[1]] == 0 or \
                    matrix[tuple_eight[0]][tuple_eight[1]]:
                set_tuple.add(tuple_eight)
    if set_tuple == set():  # if set of tuple is still empty return None
        return None
    else:
        return set_tuple


def blur(matrix):
    """Gets the new values of a blurred image using matrices

    :param matrix: a nested list of numbers
    :return: the new nested list (matrix) that is blurred
    """
    sum = 0
    count = 1
    avg = 0
    blur_matrix = copy.deepcopy(matrix)
    for row in range(0, len(matrix)):
        for column in range(0, len(matrix[0])):
            set_tuple = adjacent(matrix, (row, column))
            sum = matrix[row][column]
            for n in set_tuple:
                sum = sum + matrix[n[0]][n[1]]
                count = count + 1
            avg = round(sum / count)
            blur_matrix[row][column] = avg
            count = 1
    return blur_matrix


def main():
    grid = [[1, 2, 0],
            [4, 0, 5],
            [7, 3, 9],
            [0, 0, 0]]
    print(count_matrix(grid, 6))
    print(count_matrix(grid, 0))
    print(count_matrix(grid, 4))
    print(count_matrix(grid, 9))
    print(count_matrix([[]], 4))
    print(count_matrix([], 4))
    print()
    print(adjacent(grid, (0, 0)))
    print(adjacent(grid, (2, 1)))
    print(adjacent(grid, (3, 1)))
    print(adjacent(grid, (3, 9)))
    print(adjacent([], (0, 0)))
    print()
    image = [[168, 168, 170, 172, 174, 158, 154, 170],
             [172, 126, 109, 86, 72, 72, 95, 129],
             [146, 152, 165, 183, 176, 177, 178, 176],
             [181, 153, 80, 57, 79, 57, 29, 23],
             [29, 34, 19, 28, 38, 39, 15, 26],
             [14, 21, 18, 21, 21, 18, 24, 25]]
    print(adjacent(image, (3, 3)))
    print(blur(image))


if __name__ == "__main__":
    main()
