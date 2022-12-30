FROM python:3.11-slim

ADD setup.py/ /app/setup.py
ADD mlops/ /app/mlops/
ADD scripts/ /app/scripts/
ADD requirements.txt/ app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt \
    && pip install -e . \
    && sh scripts/setup_dirs.sh \
    && python scripts/train_model.py
