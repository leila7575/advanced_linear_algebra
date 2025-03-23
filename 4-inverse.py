#!/usr/bin/env python3
"""Contains the function determinant, minor, cofactor, adjugate and inverse."""


def determinant(matrix):
    """Calculates the determinant of a matrix."""

    if matrix == [[]]:
        return 1

    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        det = matrix[0][0] * matrix[1][1] - \
            matrix[0][1] * matrix[1][0]
        return det

    det = 0
    number_rows = len(matrix)
    for column in range(number_rows):
        det_matrix = []
        for i in range(1, number_rows):
            row = []
            for j in range(number_rows):
                if j != column:
                    row.append(matrix[i][j])
            det_matrix.append(row)

        sign = 1 if column % 2 == 0 else -1
        det += sign * matrix[0][column] * determinant(det_matrix)
    return det


def minor(matrix):
    """Calculates the minor matrix of a matrix."""
    if (len(matrix) == 0 or not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if len(matrix) == 1:
        return [[1]]

    min_matrix = []
    n = len(matrix)
    for i in range(n):
        min_row = []
        for j in range(n):
            mat = [
                row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i+1:])
            ]
            min_row.append(determinant(mat))
        min_matrix.append(min_row)

    return min_matrix


def cofactor(matrix):
    """Calculates the cofactor matrix of a matrix."""
    if (len(matrix) == 0 or not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if len(matrix) == 1:
        return [[1]]

    cofactor_matrix = []
    n = len(matrix)
    for i in range(n):
        cofactor_row = []
        for j in range(n):
            mat = [
                row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])
            ]
            det = determinant(mat)
            cofactor = ((-1)**(i+j)) * det

            cofactor_row.append(cofactor)
        cofactor_matrix.append(cofactor_row)

    return cofactor_matrix


def adjugate(matrix):
    """Calculates the adjugate matrix of a matrix."""
    if (len(matrix) == 0 or not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if len(matrix) == 1:
        return [[1]]

    n = len(matrix)
    cofactor_matrix = cofactor(matrix)

    adjugate_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            adjugate_matrix[i][j] = cofactor_matrix[j][i]

    return adjugate_matrix


def inverse(matrix):
    """Calculates the inverse of a matrix."""
    if (len(matrix) == 0 or not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)
    det = determinant(matrix)
    if det == 0:
        return None

    adjugate_matrix = adjugate(matrix)
    inverse_matrix = []
    for i in range(n):
        inverse_row = []
        for j in range(n):
            inverse = adjugate_matrix[i][j] / det
            inverse_row.append(inverse)
        inverse_matrix.append(inverse_row)

    return inverse_matrix
