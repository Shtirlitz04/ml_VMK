import numpy as np
import typing
from collections import defaultdict


def kfold_split(num_objects: int,
                num_folds: int) -> list[tuple[np.ndarray, np.ndarray]]:
    indices = np.arange(num_objects)
    fold_size = num_objects // num_folds
    folds = []

    for i in range(num_folds):
        start = i * fold_size
        end = start + fold_size if i < num_folds - 1 else num_objects
        val_indices = indices[start:end]
        train_indices = np.concatenate((indices[:start], indices[end:]))
        folds.append((train_indices, val_indices))

    return folds


def knn_cv_score(X: np.ndarray, y: np.ndarray, parameters: dict[str, list],
                 score_function: callable,
                 folds: list[tuple[np.ndarray, np.ndarray]],
                 knn_class: object) -> dict[str, float]:
    scores = defaultdict(list)

    for n_neighbors, metric, weight, (normalizer, normalizer_name) in (
            (n_neighbors, metric, weight, (normalizer, normalizer_name))
            for n_neighbors in parameters['n_neighbors']
            for metric in parameters['metrics']
            for weight in parameters['weights']
            for normalizer, normalizer_name in parameters['normalizers']):

        fold_scores = []

        for train_indices, val_indices in folds:
            X_train = X[train_indices]
            y_train = y[train_indices]
            X_val = X[val_indices]
            if normalizer:
                normalizer.fit(X_train)
                X_train = normalizer.transform(X_train)
                X_val = normalizer.transform(X_val)

            knn_model = knn_class(n_neighbors=n_neighbors, metric=metric, weights=weight)
            knn_model.fit(X_train, y_train)
            y_pred = knn_model.predict(X_val)

            fold_score = score_function(y[val_indices], y_pred)
            fold_scores.append(fold_score)

        mean_score = np.mean(fold_scores)
        key = (normalizer_name, n_neighbors, metric, weight)
        scores[key].append(mean_score)

    return {key: np.mean(score) for key, score in scores.items()}
