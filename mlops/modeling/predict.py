import pandas as pd
from fastapi import Request

from mlops.modeling import util


async def predict_request(request: Request) -> float:
    model = util.load_model()
    data = await request.json()
    data = pd.DataFrame([data])
    return model.predict(data)[0]
