from typing import List
from copy import deepcopy


def get_part_of_array(X):
    Y = []
    for i in range(0, len(X), 4):
        row = X[i]
        Y.append([row[j] for j in range(120, 500, 5)])
    return Y 

            
    """
    X - двумерный массив вещественных чисел размера n x m. Гарантируется что m >= 500
    Вернуть: двумерный массив, состоящий из каждого 4го элемента по оси размерности n 
    и c 120 по 500 c шагом 5 по оси размерности m
    """


def sum_non_neg_diag(X):
    s = 0
    f = False
    for i in range(min(len(X), len(X[0]))):
            if X[i][i] >= 0:
                s += X[i][i]
                f = True
    if not f:
        return -1
    return s
    """
    Вернуть  сумму неотрицательных элементов на диагонали прямоугольной матрицы X. 
    Если неотрицательных элементов на диагонали нет, то вернуть -1
    """

def replace_values(X):
    Y = deepcopy(X)
    for j in range(len(Y[0])):
        s = 0
        n = len(Y)
        for i in range(len(Y)):
            s += Y[i][j]
        sr = s / n
        n1 = sr * 1.5
        n2 = sr * 1/4
        for i in range(len(Y)):
            if Y[i][j]>n1 or Y[i][j]<n2:
                Y[i][j] = -1
    return Y
    """
    X - двумерный массив вещественных чисел размера n x m.
    По каждому столбцу нужно почитать среднее значение M.
    В каждом столбце отдельно заменить: значения, которые < 0.25M или > 1.5M на -1
    Вернуть: двумерный массив, копию от X, с измененными значениями по правилу выше
    """
