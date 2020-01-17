# dictionary exercise in class
from math import sqrt
temperature = {"San Jose": 92, "Mountain View": 89, "San Francisco": 75,
               "Fremont": 91}
description = {city: "hot" if temperature[city] >= 90 else "ok" for city in
               temperature}
print(description)

prices = {"apples": 2.25, "oranges": 1.59, "pears": 1.75}
cheap_fruits = {fruit: prices[fruit] for fruit in prices if prices[fruit]
                < 2.00}
print(cheap_fruits)

address_book = {"Anna": "555-1234", "Bryan": "555-1111", "Chris": "555-2222",
                "Dan": "555-3333"}
swap_address_book = {address_book[name]: name for name in address_book}
print(swap_address_book)

new_squares = (x ** 2 for x in range(1000))
print(new_squares)

points = {(1, 3), (3, 0), (2, 1), (0, 3), (4, 0), (1, 2), (3, 3), (2, 2)}
max_distance = max(sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1])
                   ** 2) for point1 in points for point2 in points)
print(max_distance)

first, *middle, last = 'Python'
print(first)
print(middle)
print(last)

first, *rest = prices
print(first)
print(rest)

colors = {'blue', 'green', 'yellow', 'red'}
first, * rest = colors
print(first)
print(rest)


def volume(height, length, width):
    return height * length * width


measurements = (6, 4, 2)
print(volume(*measurements))


def adjacent(nested_list, a_coordinate):
    """
    return the set of coordinates of all neighbors of a_coordinate in
           nested_list
    :param nested_list: (list of lists) a two dimensional grid
    :param a_coordinate: (a tuple of two numbers)
           a tuple of row index and column index of  a cell in the grid
    :return: (set) a set of coordinates of row and column indexes of
              neighbors of the cell in grid
    """
    row, col = a_coordinate
    neighbors = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                neighbors.add((row + i, col + j))
    if not nested_list:
        return None
    elif row < 0 or row >= len(nested_list) or col < 0 \
            or col >= len(nested_list[0]):
        return None
    else:
        return {index for index in neighbors if 0 <= index[0] <
                len(nested_list) and 0 <= index[1] < len(nested_list[0])}


# use adjacent function from HW3
def islands(grid, ):
    return


# do depth first search
def explore(grid, position, visited):
    count = 0
    for row, col in adjacent(grid, position):
        if (row, col) not in visited:
            visited.add((row, col))
        if grid[row][col]:
            count += 1
            visited = explore(grid, (row, col), visited)
    return visited

# finish this after reading slides
