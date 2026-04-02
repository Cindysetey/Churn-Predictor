
from pydantic import BaseModel

class CustomerData(BaseModel):
    #Numeric columns
    SeniorCitizen: int        # 0 or 1
    tenure: int               # e.g. 12
    MonthlyCharges: float     # e.g. 65.5
    TotalCharges: float       # e.g. 786.0

    #Binary columns (encoded to 0/1)
    gender: str               # "Male" or "Female"
    Partner: str              # "Yes" or "No"
    Dependents: str           # "Yes" or "No"
    PhoneService: str         # "Yes" or "No"
    PaperlessBilling: str     # "Yes" or "No"

    #Multi-category columns (one-hot encoded)
    MultipleLines: str        # "Yes", "No", "No phone service"
    InternetService: str      # "DSL", "Fiber optic", "No"
    OnlineSecurity: str       # "Yes", "No", "No internet service"
    OnlineBackup: str         # "Yes", "No", "No internet service"
    DeviceProtection: str     # "Yes", "No", "No internet service"
    TechSupport: str          # "Yes", "No", "No internet service"
    StreamingTV: str          # "Yes", "No", "No internet service"
    StreamingMovies: str      # "Yes", "No", "No internet service"
    Contract: str             # "Month-to-month", "One year", "Two year"
    PaymentMethod: str        # "Electronic check", "Mailed check",
                              # "Bank transfer (automatic)", "Credit card (automatic)"
