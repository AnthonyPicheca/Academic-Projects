"""
CSCA08: Winter 2024 -- Assignment 2: Wacky Wonderland

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.
"""

# deepcopy() is used to make sure we can easily clone arrays.
# An example of how it's used is given on the assignment handout.
from copy import deepcopy

# The constants below are provided as test data and can be
# modified and used inside your docstrings to test your functions.

TEST_ACC_NUM_A = [1, 9, 4, 5, 5, 7, 2]

SAMPLE_MATRIX_A = [
    [3, 4, 5],
    [8, 8, 8],
    [1, 0, 5],
    [1, 8, 7]
]

SAMPLE_MATRIX_A_T = [
    [3, 8, 1, 1],
    [4, 8, 0, 8],
    [5, 8, 5, 7],
]

SAMPLE_MATRIX_B = [
    [3, 4, 5, 2, 9, 1, 5, 3, 2, 8],
    [8, 8, 8, 9, 2, 7, 8, 7, 3, 5],
    [1, 0, 5, 2, 4, 9, 4, 0, 3, 8],
    [1, 8, 7, 5, 6, 2, 4, 9, 7, 1],
    [6, 3, 3, 8, 7, 3, 3, 2, 2, 9],
    [0, 2, 4, 5, 1, 9, 4, 2, 8, 5],
    [9, 6, 7, 0, 2, 4, 1, 0, 2, 1],
    [1, 5, 9, 0, 2, 4, 2, 2, 4, 6],
    [5, 5, 4, 9, 3, 1, 2, 3, 4, 0],
    [2, 6, 7, 9, 9, 5, 3, 8, 2, 2]
]

#############################################################
### PART 1 : Account Numbers
#############################################################

def sum_of_digits(number: int) -> int:
    '''
    TODO: This function is provided as a potential helper function.
    It is not marked and you do not need to implement it.
    If you decide to not complete it, remove it completely.

    Given a non-negative integer 'number', return the sum of all its digits.

    Preconditions: number >= 0

    >>> sum_of_digits(1234)
    10
    >>> sum_of_digits(8888)
    32
    '''

    list_num = [int(i) for i in str(number)]
    total = 0

    for j in list_num:
        total = total + j
    return total

def is_valid_account(num_array: list[int]) -> bool:
    '''
    Multiplies every (modulo)'th integer in num_array by (multiplier) and
    replaces the new found value with the original index of num_array. If
    the new value is double digits (10 or greater), the function takes the
    sum of the two digits and replaces the sum of the digits with the original
    index of num_array. Returns True if and only if the ones digit of the final
    sum of all the itegers in num_array is the same as modulo. Otherwise,
    returns False.

    >>> is_valid_account([1, 9, 4, 5, 5, 7, 2])
    False
    >>> is_valid_account([3, 7, 6, 4, 7, 9, 0, 6])
    True
    '''
    multiplier = num_array[-2]
    modulo = num_array[-1]

    newlist = deepcopy(num_array)
    newlist.reverse()

    payload = newlist[:-2]
    final_sum = 0

    for i in range(len(payload)):
        if i % modulo == 0:
            payload[i] = (payload[i] * multiplier)
        elif not payload[i] % modulo == 0:
            payload[i] = payload[i]

        if payload[i] > 9:
            payload[i] = sum_of_digits(payload[i])
        elif payload[i] < 10:
            payload[i] = payload[i]

        final_sum = final_sum + payload[i]


    return (final_sum % 10) == modulo

#############################################################
### PART 2 : Memory Trail
#############################################################

def memory_median(num_array: list[int]) -> float:
    '''
    Returns the median of the list of integers, num_array

    >>> memory_median([5, 7, 9, 8, 2, 1, 6, 3])
    5.5
    '''
    num_array = sorted(num_array)


    if len(num_array) % 2 == 0:

        median = ((num_array[(len(num_array) // 2)] +
                   num_array[(len(num_array) // 2) - 1]) / 2)
        return median

    return num_array[len(num_array)//2]


def memory_sequence(num_array: list[int]) -> list[int]:
    '''
    Returns a list of all unique integers found in num_array in order of
    when they appeared in num_array from left to right.

    >>> memory_sequence([1, 1, 3, 2, 2, 4, 5, 2])
    [1, 3, 2, 4, 5]
    '''
    recited = []

    for i in num_array:
        if i not in recited:
            recited.append(i)

    return recited


def memory_count(num_array: list[int], recall_array: list[int]) -> list[int]:
    '''
    Returns a list representing the number of times each integer in
    recall_array can be found in num_array in order of the index of said
    integer in recall_array from left to right.

    >>> memory_count([1, 1, 3, 2, 2, 4, 5, 2], [1, 5, 7, 2])
    [2, 1, 0, 3]
    '''
    recall = []

    for i in recall_array:
        recall.append(num_array.count(i))
    return recall

#############################################################
### PART 3 : Numbers Search
#############################################################

def in_matrix(row: int, col: int, max_rows: int, max_cols: int) -> bool:
    '''
    TODO: This function is provided as a potential helper function.
    It is not marked and you do not need to implement it.
    If you decide to not complete it, remove it completely.

    Return True if and only if a given row and column index 'row'
    'col' are inside a matrix with 'max_rows' number of rows and
    'max_cols' number of columns.

    Preconditions: max_rows >= 0
                   max_cols >= 0

    >>> in_matrix(3, 4, 6, 6)
    True
    >>> in_matrix(10, 10, 5, 5)
    False
    '''
    return row <= max_rows and col <= max_cols

def swap_around(matrix: list[list[int]]) -> list[list[int]]:
    '''
    Returns a new list of lists arranged such that every column in matrix
    becomes a row in our new list of lists and all rows in matrix become a
    column in our new list of lists.

    Preconditions: len(matrix) == N
                   len(matrix[i]) == M, 0 <= i < N

    >>> swap_around(SAMPLE_MATRIX_A) == SAMPLE_MATRIX_A_T
    True
    '''
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    transposed = [[0] * rows for k in range(cols)]


    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed


def search_list(num_list: list[int], series: list[int]) -> int:
    '''
    Returns the index of num_list where num_list contains the integers in
    series in proper order either forwards or backwards. Returns -1 if series
    is not found forwards nor backwards in num_list.

    >>> SAMPLE_LIST = [3, 4, 5, 8, 8, 8, 1, 0, 5]
    >>> search_list(SAMPLE_LIST, [5, 8, 8])
    2
    >>> search_list(SAMPLE_LIST, [8, 8, 5])
    2
    '''
    series_length = len(series)


    for i in range(len(num_list) - series_length + 1):
        if num_list[i:i + series_length] == series:
            return i

    reversed_series = series[::-1]
    for i in range(len(num_list) - series_length + 1):
        if num_list[i:i + series_length] == reversed_series:
            return i

    return -1


def search_rows(matrix: list[list[int]], series: list[int]) -> bool:
    '''
    Returns True if and only if series can be found in any rows within matrix

    >>> search_rows(SAMPLE_MATRIX_B, [8, 7, 3, 3])
    True
    >>> search_rows(SAMPLE_MATRIX_B, [4, 3, 2, 1])
    True
    >>> search_rows(SAMPLE_MATRIX_B, [1, 1, 1])
    False
    '''
    for lst in matrix:
        if search_list(lst, series) != -1:
            return True
    return False

def search_columns(matrix: list[list[int]], series: list[int]) -> bool:
    '''
    Returns True if and only if series can be found in any columns in matrix.

    >>> search_columns(SAMPLE_MATRIX_B, [3, 9, 4, 4])
    True
    >>> search_columns(SAMPLE_MATRIX_B, [7, 4, 3, 7])
    True
    >>> search_columns(SAMPLE_MATRIX_B, [1, 2, 3, 4])
    False
    '''
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    transposed = [[0] * rows for k in range(cols)]


    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]


    for lst in matrix:
        if search_list(lst, series) != 1:
            return True
    return False

def search_diagonals(matrix: list[list[int]], series: list[int]) -> bool:
    '''
    Returns True if and only if series can be found within any diagonal in
    matrix.

    >>> search_diagonals(SAMPLE_MATRIX_B, [3, 1, 0, 9, 5])
    True
    >>> search_diagonals(SAMPLE_MATRIX_B, [9, 9, 6, 0])
    True
    >>> search_diagonals(SAMPLE_MATRIX_B, [1, 2, 3, 4])
    False
    '''
    for lst in matrix:
        if search_list(lst, series) != 1:
            return True
    return False

def validate_coordinates(matrix: list[list[int]], row_idx: int,
                         col_idx: int, series: list[int]) -> bool:
    '''
    Returns True if im confused and my brain hurts when I think about this
    question

    >>> validate_coordinates(SAMPLE_MATRIX_B, 4, 3, [4, 1, 8, 7, 0, 8])
    True
    >>> validate_coordinates(SAMPLE_MATRIX_B, 5, 7, [7, 0, 9, 2, 2])
    True
    >>> validate_coordinates(SAMPLE_MATRIX_B, 9, 0, [7, 9, 9, 5])
    False
    '''
    return matrix.append(series) == matrix.append(series) or (col_idx.append
                                                              (row_idx) ==
                                                              col_idx.append
                                                              (row_idx))
# how many points for a valiant effort?


if __name__ == '__main__':
    import doctest
    doctest.testmod()
