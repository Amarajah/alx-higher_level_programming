#!/usr/bin/python3
"""
Function that multiplies 2 matrices by using the module NumPy.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Uses matmul NumPy function to perform matrix multiplication.
    If matrice dimension are not compatible,a ValueError is thrown.

    """
    try:
        return np.matmul(m_a, m_b)
    except ValueError as a:
        raise ValueError('The matrices cannot be multiplied because
        their dimensions are incompatible') from a
