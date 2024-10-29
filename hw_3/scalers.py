import numpy as np
import typing


class MinMaxScaler:
    def fit(self, data: np.ndarray) -> None:
        self.min_ = np.min(data, axis=0)
        self.max_ = np.max(data, axis=0)

    def transform(self, data: np.ndarray) -> np.ndarray:
        if self.min_ is None or self.max_ is None:
            raise RuntimeError("Fit the scaler before transform")
        return (data - self.min_) / (self.max_ - self.min_)


class StandardScaler:
    def fit(self, data: np.ndarray) -> None:
        self.mean_ = np.mean(data, axis=0)
        self.std_ = np.std(data, axis=0)

    def transform(self, data: np.ndarray) -> np.ndarray:
        if self.mean_ is None or self.std_ is None:
            raise RuntimeError("Fit the scaler before transform")
        return (data - self.mean_) / self.std_
