import pandas as pd
from sklearn.datasets import fetch_california_housing

from mlops import constants

COLUMN_NAMES_MAPPING = {
    "MedInc": "med_inc",
    "HouseAge": "house_age",
    "AveRooms": "avg_rooms",
    "AveBedrms": "avg_bedrooms",
    "Population": "population",
    "AveOccup": "avg_occupation",
    "Latitude": "lat",
    "Longitude": "lon",
    "MedHouseVal": "house_value",
}

FILE_NAME = "california_housing.parquet"


def get_california_housing_data():
    data = _get_data()
    _save_data(data)


def _get_data() -> pd.DataFrame:
    """Get data and transform into pandas dataframe."""
    raw_data = fetch_california_housing()
    formatted_data = pd.DataFrame(raw_data.data, columns=raw_data.feature_names)
    formatted_data[raw_data.target_names[0]] = raw_data.target
    formatted_data = formatted_data.rename(columns=COLUMN_NAMES_MAPPING)
    return formatted_data


def _save_data(data: pd.DataFrame):
    data.to_parquet(constants.BRONZE_LAYER / FILE_NAME)


if __name__ == "__main__":
    get_california_housing_data()
