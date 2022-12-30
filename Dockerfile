FROM python:3.11-slim

ADD setup.py/ /app/setup.py
ADD requirements.txt/ app/requirements.txt
ADD mlops/ /app/mlops/
ADD scripts/ /app/scripts/

WORKDIR /app

RUN pip install -r requirements.txt \
    && pip install . \
    && sh scripts/setup_dirs.sh \
    && python scripts/train_model.py

CMD uvicorn mlops.app:app
