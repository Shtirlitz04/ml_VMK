import numpy as np


def get_part_of_array(X: np.ndarray) -> np.ndarray:
    return X[::4, 120:500:5]


def sum_non_neg_diag(X: np.ndarray):
    s = np.diag(X)[np.diag(X)>=0]
    return np.sum(s) if s.size>0 else -1

def replace_values(X: np.ndarray) -> np.ndarray:
    Y = X.copy()
    sr = np.mean(Y, axis = 0)
    n1 = sr * 1.5
    n2 = sr * 0.25
    Y[(X < n2) | (X > n1)] = -1
    return Y
