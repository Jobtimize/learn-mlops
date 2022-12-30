"""
Executable to run the app.

"""

import pandas as pd
import uvicorn
from fastapi import FastAPI

from mlops.logging import logging
from mlops.modeling import util
from mlops.validate.validate import CaliforniaHousing

logging.init()
logger = logging.get(__name__)

app = FastAPI()


@app.get("/")
async def root():
    logger.info("Called root.")
    return {"message": "Hello World"}


@app.post("/predict")
async def predict(california_housing: CaliforniaHousing):
    logger.info("Called predict.")
    model = util.load_model()
    data = pd.DataFrame([california_housing.dict()])
    return model.predict(data)[0]


if __name__ == "__main__":
    uvicorn.run(app)
