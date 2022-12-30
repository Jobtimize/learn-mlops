from fastapi import FastAPI, Request

from mlops.modeling import predict

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/predict_request")
async def predict_request(request: Request):
    return predict.predict_request(request)
