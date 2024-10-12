from collections import Counter
from typing import List


def are_multisets_equal(x: List[int], y: List[int]) -> bool:
    x.sort()
    y.sort()
    if x == y:
        return True
    else:
        return False

def max_prod_mod_3(x: List[int]) -> int:
    pr_max = -1
    for i in range(1, len(x)):
        pr = x[i] * x[i-1]
        if pr>pr_max and pr % 3 == 0:
            pr_max = pr
    return pr_max

def convert_image(image: List[List[List[float]]], weights: List[float]) -> List[List[float]]:
    height, width = len(image), len(image[0])
    channels = len(weights)
    result = [[0.0] * width for _ in range(height)]
    for i in range(height):
        for j in range(width):
            for k in range(channels):
                result[i][j] += image[i][j][k] * weights[k]
    return result


def rle_scalar(x: List[List[int]], y:  List[List[int]]) -> int:
    decoded_x = []
    for value, count in x:
        decoded_x.extend([value] * count)
    decoded_y = []
    for value, count in y:
        decoded_y.extend([value] * count)
    if len(decoded_x) != len(decoded_y):
        return -1
    pr = sum(a * b for a, b in zip(decoded_x, decoded_y))
    return pr

def cosine_distance(X: List[List[float]], Y: List[List[float]]) -> List[List[float]]:
    distance = [[0] * len(Y) for _ in range(len(X))]  
    for i, x in enumerate(X):
        for j, y in enumerate(Y):
            dot_pr = sum(a * b for a, b in zip(x, y))
            
            norm_x = sum(a ** 2 for a in x) ** 0.5
            norm_y = sum(b ** 2 for b in y) ** 0.5
            
            if norm_x == 0 or norm_y == 0:
                distance[i][j] = 1.0
            else:
                distance[i][j] = (dot_pr / (norm_x * norm_y))
                
    return distance

