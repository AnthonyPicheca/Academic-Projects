"""CSCA08: Fall 2025 -- Assignment 2: Phrase Encryption

Starter code.

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2022 Dominik Luszczynski,
Jacqueline Smith, David Liu, and Anya Tafliovich

"""

import random
import hashlib
from copy import deepcopy
from typing import TypeVar

from constants import (ALL_CONSONANTS,
                       ALL_VOWELS,
                       TESTING,
                       VOWEL_VALUE,
                       CONSONANT_VALUE)

###############################################################
# The following matrices are given as examples to use
# in doctests
###############################################################

BINARY_3X3 = [[1, 1, 1], [1, 0, 0], [1, 1, 1]]

BINARY_3X4 = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1]]

S_MATRIX = [["a", "a", "a"], ["a", "b", "b"], ["a", "a", "a"]]

S_MATRIX_UNIQUE = [["a", "b", "c"], ["x", "y", "z"]]

A_ENCRYPTED = [
    ["{", "x", "n", "c", "h", "e", "{", "{", "q", "e", "i"],
    ["t", "i", "f", "b", "f", "e", "v", "y", "{", "o", "l"],
    ["n", "e", "p", "e", "v", "l", "d", "j", "o", "r", "d"],
    ["t", "s", "f", "n", "o", "b", "o", "f", "e", "g", "r"],
    ["o", "s", "b", "b", "p", "p", "f", "j", "w", "r", "w"],
    ["n", "h", "{", "c", "s", "s", "x", "k", "m", "h", "x"],
    ["i", "i", "c", "d", "i", "o", "i", "k", "d", "w", "e"],
    ["h", "h", "z", "o", "c", "{", "o", "e", "h", "{", "u"],
    ["h", "w", "n", "z", "s", "g", "h", "w", "d", "r", "{"],
]

A_DECRYPTED = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

A_FLIPPED = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

A_HASH = "4c713750846571d7000c821f5f320f8103181e005792cf37aa8adef94d29c5c9"

###############################################################

# The following type is used to specify that a list
# can contain either all int or all str
Element = TypeVar("Element", int, str)

###############################################################

# NOTE: Please replace the 'pass' line with your implementation
#       of the function.


# We provided a full docstring for this function as an example
# on using the matrices above.
def is_valid_matrix(matrix: list[list[Element]]) -> bool:
    """Return True if and only if the nested list
    matrix is a valid matrix. A matrix is valid
    if and only if it is rectangular (same number of
    columns for every row).

    >>> is_valid_matrix([])
    True
    >>> is_valid_matrix(BINARY_3X3)
    True
    >>> is_valid_matrix([[1, 0], [1], [1, 0]])
    False
    """
    if matrix == []:
        return True

    ncols = len(matrix[0])
    for row in matrix:
        if len(row) != ncols:
            return False
    return True


def combine_rows(
    matrix1: list[list[Element]], matrix2: list[list[Element]]
) -> None:
    """

    Mutates? YES

    >>> EMPTY = []
    >>> combine_rows(EMPTY, [])
    >>> EMPTY
    []
    >>> BINARY_3X3_COPY = deepcopy(BINARY_3X3)
    >>> combine_rows(BINARY_3X3_COPY, [[1], [1], [1]])
    >>> BINARY_3X3_COPY
    [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1]]
    >>> BINARY_3X3_COPY = deepcopy(BINARY_3X3)
    >>> combine_rows(BINARY_3X3_COPY, BINARY_3X4)
    >>> BINARY_3X3_COPY
    [[1, 1, 1, 0, 1, 1, 1], [1, 0, 0, 1, 0, 1, 1], [1, 1, 1, 1, 1, 0, 1]]
    """

    if not is_valid_matrix(matrix1) or not is_valid_matrix(matrix2):
        return None

    if len(matrix1) != len(matrix2):
        return None

    for i in range(len(matrix1)):
        matrix1[i].extend(matrix2[i])

    return None


def invert_binary_values(matrix: list[list[int]]) -> None:
    """Flip all 0s to 1s and 1s to 0s in matrix.

    Mutates the given binary matrix in place.

    Precondition: matrix must be rectangular and binary


    >>> m = [[1, 0, 1], [0, 1, 0]]
    >>> invert_binary_values(m)
    >>> m
    [[0, 1, 0], [1, 0, 1]]
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0


def convert_binary_to_str(matrix: list[list[int]]) -> None:
    """Convert a binary matrix into characters 'V' and 'C'.

    Mutates the given matrix in place.

    Preconditions:
        - matrix is a valid rectangular matrix containing only 0s and 1s

    >>> m = [[1, 0, 1]]
    >>> convert_binary_to_str(m)
    >>> m
    [['a', 'b', 'a']]
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = get_random_char(matrix[i][j])


def convert_str_to_binary(matrix: list[list[str]]) -> None:
    """Convert letters in matrix to binary: vowels → 1, consonants → 0.

    Mutates? YES

    Preconditions:
        - matrix is a valid rectangular list of single-character strings
        - constants ALL_VOWELS, ALL_CONSONANTS, VOWEL_VALUE, and
        CONSONANT_VALUE are defined

    >>> m = [['a', 'c', 'a']]
    >>> convert_str_to_binary(m)
    >>> m
    [[1, 0, 1]]
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            ch = matrix[i][j]
            if ch in ALL_VOWELS:
                matrix[i][j] = VOWEL_VALUE
            else:
                matrix[i][j] = CONSONANT_VALUE


def encrypt_or_decrypt(matrix: list[list[str]],
                       key: int,
                       encrypt: bool) -> None:
    """Encrypt or decrypt the matrix in place using a shift cipher.

    Each character's Unicode value is shifted by key (added if encrypting,
    subtracted if decrypting).

    Preconditions:
        - matrix is a rectangular list of single-character strings
        - key is an integer >= 0

    >>> m = [['a', 'c', 'a']]
    >>> encrypt_or_decrypt(m, 1, True)
    >>> m
    [['b', 'd', 'b']]
    >>> encrypt_or_decrypt(m, 1, False)
    >>> m
    [['a', 'c', 'a']]
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            ch = matrix[i][j]
            if encrypt:
                matrix[i][j] = chr(ord(ch) + key)
            else:
                matrix[i][j] = chr(ord(ch) - key)


def rotate_matrix(matrix: list[list[Element]]) -> list[list[Element]]:
    """Return a new matrix rotated 90° clockwise if valid; otherwise,
    return it unmodified.

    Does not mutate the original matrix.

    Preconditions:
        - matrix is a list of lists (possibly empty)

    >>> rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    >>> rotate_matrix([[1, 2, 3, 4]])
    [[1], [2], [3], [4]]
    """
    if matrix == []:
        return []

    nrows = len(matrix)
    ncols = len(matrix[0])
    for row in matrix:
        if len(row) != ncols:
            return matrix

    rotated = [[None for _ in range(nrows)] for _ in range(ncols)]

    for i in range(nrows):
        for j in range(ncols):
            rotated[j][nrows - 1 - i] = matrix[i][j]

    return rotated


def flip_matrix(
    matrix: list[list[Element]], horizontal: bool
) -> list[list[Element]]:
    """Return a new matrix flipped horizontally or vertically.

    If horizontal is True, flip along the horizontal axis (top ↔ bottom).
    If False, flip along the vertical axis (left ↔ right).
    If matrix is invalid, return the unmodified matrix.

    Preconditions:
        - matrix is a valid list of lists (possibly empty)

    >>> flip_matrix([[1, 2], [3, 4]], True)
    [[3, 4], [1, 2]]
    >>> flip_matrix([[1, 2], [3, 4]], False)
    [[2, 1], [4, 3]]
    >>> flip_matrix([[1], [2], [3], [4]], True)
    [[4], [3], [2], [1]]
    >>> flip_matrix([[1], [2], [3], [4]], False)
    [[1], [2], [3], [4]]
    """
    if matrix == []:
        return []

    if not all(len(row) == len(matrix[0]) for row in matrix):
        return matrix  # invalid → return unmodified

    if horizontal:
        return matrix[::-1]

    return [row[::-1] for row in matrix]


# We provide the docstring in this function as an example of
# testing a function that returns a float, in addition to
# showing how the solve_mystery_phrase uses the secret string
# which is the hash (unique) of the clean matrix.
def solve_mystery_phrase(
    encrypted_matrix: list[list[str]], target_hash: str, max_key_value: int
) -> list[list[int]]:
    """Return the decrypted binary matrix (list[list[int]])
    of encrypted_matrix that matches the given target_hash
    (this is done by checking check_secret_message(your_matrix, target_hash)),
    where the max_key_value is the maximum key value for the shift encryption.
    If no valid key produces the correct hash, return an empty list ([]).

    To decrypt the matrix, you will need to:
        Check all possible combinations of:
            - Key shifts from 0 to max_key_value
            - 0 to 3 rotations (4 rotations would give us
                the original matrix - 360 degrees)
            - No flip, horizontal flip, vertical flip or both.

        For each combination:
            - Convert the character matrix (str) into a binary matrix (int)
            - Call check_secret_message(your_matrix, target_hash)
                where your_matrix is the matrix produced after
                performing some combination of a key shift,
                rotation and/or flip.

    Please read the example provided in the Assignment handout.

    Precondition: matrix only contains string characters

    Mutates? NO

    Note it is recommended to use deepcopy in this function.
    For example:
        encrypted_matrix_copy = deepcopy(encrypted_matrix)

    >>> solve_mystery_phrase(A_ENCRYPTED, A_HASH, 20) == A_DECRYPTED
    True
    >>> solve_mystery_phrase(A_ENCRYPTED, 'not-a-hash', 20)
    []
    """
    for key in range(max_key_value + 1):
        decrypted_chars = deepcopy(encrypted_matrix)

        encrypt_or_decrypt(decrypted_chars, key, encrypt=False)

        convert_str_to_binary(decrypted_chars)

        for rot in range(4):
            if rot == 0:
                rotated = deepcopy(decrypted_chars)
            else:
                rotated = rotate_matrix(rotated)

            variants = []
            variants.append(rotated)
            variants.append(flip_matrix(rotated, True))
            variants.append(flip_matrix(rotated, False))
            variants.append(flip_matrix(flip_matrix(rotated, True), False))

            for candidate in variants:
                if check_secret_message(candidate, target_hash):
                    return candidate
    return []

# =========================================================
# Helper functions


def get_random_char(character: int) -> str:
    """Return a random string given character, if
    the binary value is a binary integer, otherwise return character.
    If TESTING is True (which is true when running this file),
    then 1 is assigned as 'a' and everything else
    is assigned 'b' so we ensure that all docstring tests
    are do not depend on randomness.

    >>> get_random_char(0)
    'b'
    >>> get_random_char(1)
    'a'
    >>> get_random_char(2)
    2
    >>> get_random_char('a')
    'a'
    """

    if character not in [0, 1]:
        return character
    if character:
        if not TESTING:
            random_index = random.randint(0, len(ALL_VOWELS) - 1)
        else:
            random_index = 0
        return ALL_VOWELS[random_index]
    if not TESTING:
        random_index = random.randint(0, len(ALL_CONSONANTS) - 1)
    else:
        random_index = 0
    return ALL_CONSONANTS[random_index]


def check_secret_message(matrix: list[list[Element]],
                         target_hash: str) -> bool:
    """Return True if and only if the hash value of
    matrix matches target_hash

    >>> check_secret_message(A_ENCRYPTED, A_HASH)
    False
    >>> check_secret_message(A_DECRYPTED, A_HASH)
    True
    """

    matrix_str = str(matrix)
    return hashlib.sha256(matrix_str.encode()).hexdigest() == target_hash


# ==========================================================


if __name__ == "__main__":
    TESTING = True
    import doctest
    doctest.testmod()
