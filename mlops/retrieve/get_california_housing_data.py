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


def main():
    data = get_data()
    dump_data(data)


def get_data() -> pd.DataFrame:
    raw_data = fetch_california_housing()
    formatted_data = pd.DataFrame(raw_data.data, columns=raw_data.feature_names)
    formatted_data[raw_data.target_names[0]] = raw_data.target
    formatted_data = formatted_data.rename(columns=COLUMN_NAMES_MAPPING)
    return formatted_data


def dump_data(data: pd.DataFrame):
    data.to_parquet(constants.BRONZE_LAYER / FILE_NAME)


if __name__ == "__main__":
    main()
