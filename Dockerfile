FROM python:3.11-slim

ADD setup.py/ /app/setup.py
ADD mlops/ /app/mlops/
ADD scripts/ /app/scripts/
ADD requirements.txt/ app/requirements.txt

WORKDIR /app

RUN sh scripts/_setup_and_run_full_app.sh
