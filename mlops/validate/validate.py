from pydantic import BaseModel


class CaliforniaHousing(BaseModel):
    med_inc: float
    house_age: float
    avg_rooms: float
    avg_bedrooms: float
    population: float
    avg_occupation: float
    lat: float
    lon: float
