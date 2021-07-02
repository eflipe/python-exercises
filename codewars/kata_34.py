# https://www.codewars.com/kata/5f5802bf4c2cc4001a6f859e/train/python

def grid_index(grid, indexes):
    flat_grid = []
    output_string = ''

    for letters in grid:
        for letter in letters:
            flat_grid.append(letter)

    for num in indexes:
        output_string += flat_grid[num - 1]

    return output_string


if __name__ == '__main__':
    grid = [['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']]
    grid_2 = [['h', 'e', 'l', 'l'], ['o', 'c', 'o', 'd'],
              ['e', 'w', 'a', 'r'], ['r', 'i', 'o', 'r']]
    indexes_2 = [5, 7, 9, 3, 6, 6, 8, 8, 16, 13]
    indexes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    output = grid_index(grid_2, indexes_2)  # myexample
    print(output)
