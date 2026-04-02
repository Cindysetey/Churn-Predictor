
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from schema import CustomerData
import joblib, pandas as pd, traceback

app = FastAPI(title="Customer Churn Predictor")
app.mount("/static", StaticFiles(directory="static"), name="static")

model = joblib.load("model/churn_model.pkl")
feature_columns = joblib.load("model/feature_columns.pkl")

binary_cols = ['gender','Partner','Dependents','PhoneService','PaperlessBilling']
binary_map  = {"Female":0,"Male":1,"No":0,"Yes":1}
multi_cols  = ['MultipleLines','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies',
               'Contract','PaymentMethod']

@app.get("/")
def root():
    return FileResponse("static/index.html")

@app.post("/predict")
def predict_churn(data: CustomerData):
    try:
        df = pd.DataFrame([data.dict()])
        for col in binary_cols:
            df[col] = df[col].map(binary_map)
        df = pd.get_dummies(df, columns=multi_cols, drop_first=True)
        df = df.astype({col:'int' for col in df.select_dtypes('bool').columns})
        df = df.reindex(columns=feature_columns, fill_value=0)
        prediction  = model.predict(df)[0]
        probability = model.predict_proba(df)[0][1]
        return {"churn_prediction":int(prediction),
                "label":"Will Churn" if prediction==1 else "Will Stay",
                "churn_probability":round(float(probability),4)}
    except Exception as e:
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))
