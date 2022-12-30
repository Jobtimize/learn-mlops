from setuptools import setup, find_packages

NAME = "mlops"

setup(
    name=NAME,
    version="0.1.0",
    packages=find_packages(include=[NAME, f"{NAME}.*"]),
)
