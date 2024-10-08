#!/usr/bin/python3
"""Module for rotating a 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D Matrix 90 degrees clockwise"""
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(len(matrix)):
        matrix[i].reverse()
