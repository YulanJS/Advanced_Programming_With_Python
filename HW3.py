"""
There are three functions in this program.

count_matrix: count the number of occurrence of value in a list
adjacent: return a set of indexes of neighbors of a cell in a
nested list
blur: return a blurred image of original image
"""


def count_matrix(a_list, value):
    """
    count the number of occurrence of value in a_list
    :param a_list: (list) a matrix
    :param value: (number) a number may or may not in the matrix
    :return: (number) the number of occurrence of value in the matrix
    """
    if not a_list:
        return 0
    else:
        return sum(row.count(value) if row else 0 for row in a_list)


def adjacent(grid, a_coordinate):
    """
    return the set of coordinates of all neighbors of a_coordinate in
           nested_list
    :param grid: (list of lists) a two dimensional grid
    :param a_coordinate: (a tuple of two numbers)
           a tuple of row index and column index of  a cell in the grid
    :return: (set) a set of coordinates of row and column indexes of
              neighbors of the cell in grid
    """
    row, col = a_coordinate
    neighbors = {(row + i, col + j) for i in range(-1, 2) for j in range(-1, 2)
                 if i != 0 or j != 0}
    if not grid:
        return None
    elif row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return None
    else:
        return {(row, col) for (row, col) in neighbors if 0 <= row <
                len(grid) and 0 <= col < len(grid[0])}


def blur(grid):
    """
    Blur an image represented by a nested list. Each cell in the blurred
     image should be an average of intensities of itself and all its
     neighbors in the original image.
    :param grid: (list of lists) representing a grayscale image
    :return: (list of lists) a blurred image of nested_list
    """
    if not grid:
        return grid
    blurred_image = [[0] * len(grid[0]) for _ in range(len(grid))]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            neighbor_indexes = adjacent(grid, (row, col))
            neighbor_sum = sum(grid[neighbor_row][neighbor_col]
                               for (neighbor_row, neighbor_col)
                               in neighbor_indexes)
            blurred_image[row][col] = round((grid[row][col] + neighbor_sum)
                                            / (len(neighbor_indexes) + 1))
    return blurred_image


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
    print(adjacent(grid, (8, 9)))
    print(adjacent([], (0, 0)))
    print()
    image = [[168, 168, 170, 172, 174, 158, 154, 170],
             [172, 126, 109, 86,  72,  72,  95,  129],
             [146, 152, 165, 183, 176, 177, 178, 176],
             [181, 153, 80,  57,  79,  57,  29,  23],
             [29,  34,  19,  28,  38,  39,  15,  26],
             [14,  21,  18,  21,  21,  18,  24,  25]]
    print(blur(image))


if __name__ == "__main__":
    main()
