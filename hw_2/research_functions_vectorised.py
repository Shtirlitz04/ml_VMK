import numpy as np


def are_multisets_equal(x: np.ndarray, y: np.ndarray) -> bool:
    return np.array_equal(np.sort(x), np.sort(y))


def max_prod_mod_3(x: np.ndarray) -> int:
    mask = x % 3 == 0
    pr = x[:-1] * x[1:]
    ans = pr[(mask[:-1] | mask[1:])]
    return ans.max() if ans.size > 0 else -1


def convert_image(image: np.ndarray, weights: np.ndarray) -> np.ndarray:
    return np.dot(image, weights)


def rle_scalar(x: np.ndarray, y: np.ndarray) -> int:
    x_new = np.repeat(x[:, 0], x[:, 1]) 
    y_new = np.repeat(y[:, 0], y[:, 1]) 
    if len(x_new) != len(y_new):
        return -1
    pr = np.dot(x_new, y_new)
    return pr


def cosine_distance(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    norm_X = np.linalg.norm(X, axis=1, keepdims=True)
    norm_Y = np.linalg.norm(Y, axis=1, keepdims=True)
    cos_sim = np.dot(X, Y.T)
    cos_sim = np.where(norm_X == 0, np.nan, cos_sim)
    zn = norm_X * norm_Y.T
    zn = np.where(norm_X == 0, np.nan, zn)
    cos_sim /= zn
    cos_sim = np.nan_to_num(cos_sim, nan=1)
    return cos_sim
