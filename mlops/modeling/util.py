import joblib
from singleton_decorator import singleton
from sklearn.ensemble import RandomForestRegressor

from mlops import constants
from mlops.logging import logging

logger = logging.get(__name__)


def save_model(model: RandomForestRegressor):
    logger.info("Save model.")
    joblib.dump(model, constants.MODEL_PATH)


@singleton
def load_model() -> RandomForestRegressor:
    """This function is cached to enable that the model is only loaded the first time the predict
    endpoint is called after the application has been started. Thereafter it will automatically
    use the loaded model."""
    logger.info("Load model.")
    return joblib.load(constants.MODEL_PATH)
