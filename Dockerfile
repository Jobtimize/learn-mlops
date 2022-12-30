FROM python:3.11

ADD setup.py/ /app/setup.py
ADD requirements.txt/ app/requirements.txt
ADD mlops/ /app/mlops/
ADD scripts/ /app/scripts/
ADD data/input/ /app/data/input/

WORKDIR /app

RUN pip install -r requirements.txt \
    && pip install . \
    && sh scripts/setup_dirs.sh \
    && python scripts/train_model.py

EXPOSE 8000

CMD uvicorn mlops.app:app --host 0.0.0.0 --port 8000
