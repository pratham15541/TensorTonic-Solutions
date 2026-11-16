import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    rows = len(A)
    cols = len(A[0])
    res = [[0] * rows for _ in range(cols)]
    for r in range(rows):
        for c in range(cols):
            res[c][r] = A[r][c]
    return np.asarray(res)
