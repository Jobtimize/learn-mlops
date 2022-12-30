import pandas as pd
import uvicorn
from fastapi import FastAPI, Request

from mlops.modeling import util

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/predict")
async def predict(request: Request):
    model = util.load_model()
    data = await request.json()
    data = pd.DataFrame([data])
    return model.predict(data)[0]


if __name__ == "__main__":
    uvicorn.run(app)
