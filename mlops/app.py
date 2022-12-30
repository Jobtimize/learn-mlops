import pandas as pd
import uvicorn
from fastapi import FastAPI, Request

from mlops.logging import logging
from mlops.modeling import util

logging.init()
logger = logging.get(__name__)

app = FastAPI()


@app.get("/")
async def root():
    logger.info("Called root.")
    return {"message": "Hello World"}


@app.post("/predict")
async def predict(request: Request):
    logger.info("Called predict.")
    model = util.load_model()
    data = await request.json()
    data = pd.DataFrame([data])
    return model.predict(data)[0]


if __name__ == "__main__":
    uvicorn.run(app)
