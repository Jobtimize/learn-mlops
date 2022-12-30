import joblib
from sklearn.ensemble import RandomForestRegressor

from mlops import constants
from mlops.logging import logging

logger = logging.get(__name__)


def save_model(model: RandomForestRegressor):
    logger.info("Save model.")
    joblib.dump(model, constants.MODEL_PATH)


def load_model() -> RandomForestRegressor:
    logger.info("Load model.")
    return joblib.load(constants.MODEL_PATH)
