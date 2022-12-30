import joblib
from sklearn.ensemble import RandomForestRegressor

from mlops import constants


def save_model(model: RandomForestRegressor):
    joblib.dump(model, constants.MODEL_PATH)


def load_model() -> RandomForestRegressor:
    return joblib.load(constants.MODEL_PATH)
