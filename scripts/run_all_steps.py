from mlops.modeling.train import train_model
from mlops.retrieve.get_data import get_california_housing_data


def main():
    data = get_california_housing_data()
    train_model(data)


if __name__ == "__main__":
    main()