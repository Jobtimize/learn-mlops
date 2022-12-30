import pandas as pd
from sklearn.ensemble import RandomForestRegressor

from mlops.logging import logging
from mlops.modeling import util

logger = logging.get(__name__)


def train_model(data: pd.DataFrame):
    logger.info("Init model.")
    model = RandomForestRegressor()
    X, y = _split_features_and_target(data)
    logger.info("Fit model.")
    model.fit(X, y)
    util.save_model(model)


def _split_features_and_target(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Assumes target is last feature"""
    logger.info("Split features and target.")
    y = data.iloc[:, -1]
    X = data.iloc[:, : data.shape[1] - 1]
    return X, y
