import pickle
import numpy as np
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, conlist


app = FastAPI(title="Predicting iris")
class iris(BaseModel):
    batches: List[conlist(item_type=float, min_items=4, max_items=4)]


@app.on_event("startup")
def load_clf():
    # Load classifier from pickle file
    with open("../app/model.pkl", "rb") as file:
        global clf
        clf = pickle.load(file)


@app.get("/")
def home():
    return "Congratulations! Your API is working as expected. This new version allows for batching. Now head over to http://localhost:81/docs"


@app.post("/predict")
def predict(iris: iris):
    batches = iris.batches
    np_batches = np.array(batches)
    pred = clf.predict(np_batches).tolist()
    return {"Prediction": pred}
