import pandas as pd
from sklearn.datasets import fetch_california_housing

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


def get_california_housing_data() -> pd.DataFrame:
    raw_data = fetch_california_housing()
    formatted_data = pd.DataFrame(raw_data.data: columns=raw_data.feature_names)
    formatted_data[raw_data.target_names[0]] = data.target
    formatted_data = formatted_data.rename(columns=COLUMN_NAMES_MAPPING)
    return formatted_data


if __name__ == "__main__":
    get_california_housing_data()
