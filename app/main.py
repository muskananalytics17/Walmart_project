
from pathlib import Path
import pickle

import pandas as pd
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Walmart Sales Prediction")

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = (
    BASE_DIR
    / "walmart_sales_analysis"
    / "notebook"
    / "xgb_model.pkl"
)

HTML_PATH = BASE_DIR / "app" / "static" / "index.html"

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

FEATURES = list(
    getattr(
        model,
        "feature_names_in_",
        [
            "Store",
            "Holiday_Flag",
            "Temperature",
            "Fuel_Price",
            "CPI",
            "Unemployment",
        ],
    )
)

app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "app" / "static")),
    name="static",
)


@app.get("/", response_class=HTMLResponse)
def home():
    return HTML_PATH.read_text(encoding="utf-8")


@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request):
    form = await request.form()

    values = {
        "Store": int(form["Store"]),
        "Holiday_Flag": int(form["Holiday_Flag"]),
        "Temperature": float(form["Temperature"]),
        "Fuel_Price": float(form["Fuel_Price"]),
        "CPI": float(form["CPI"]),
        "Unemployment": float(form["Unemployment"]),
    }

    if values["Store"] < 1 or values["Holiday_Flag"] not in (0, 1):
        return HTMLResponse("Invalid Store or Holiday value.", status_code=400)

    input_data = pd.DataFrame(
        [[values[name] for name in FEATURES]],
        columns=FEATURES,
    )

    prediction = float(model.predict(input_data)[0])

    page = HTML_PATH.read_text(encoding="utf-8")

    page = page.replace(
        "{{RESULT}}",
        f"${prediction:,.2f}",
    )

    return HTMLResponse(page)