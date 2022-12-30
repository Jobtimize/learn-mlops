import pandas as pd
from sklearn.ensemble import RandomForestRegressor

from mlops.modeling import util


def train_model(data: pd.DataFrame):
    model = RandomForestRegressor()
    X, y = _split_features_and_target(data)
    model.fit(X, y)
    util.save_model(model)


def _split_features_and_target(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Assumes target is last feature"""
    y = data.iloc[:, -1]
    X = data.iloc[:, : data.shape[1] - 1]
    return X, y
