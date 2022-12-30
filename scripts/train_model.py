"""
Get sample data and train and save the model.

"""

from mlops.modeling import train
from mlops.retrieve import get_data


def main():
    data = get_data.get_california_housing_data()
    train.train_model(data)


if __name__ == "__main__":
    main()
