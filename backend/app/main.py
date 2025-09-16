# # app/main.py

# import pickle
# from fastapi import FastAPI, HTTPException
# from pathlib import Path


import pickle
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware # Import the CORS middleware
from pathlib import Path
import os

from app.schemas.prediction import PredictionInput, PredictionOutput
from app.core.preprocessing import preprocess_input

# Initialize FastAPI app
app = FastAPI(
    title="Sales Prediction API",
    description="An API to predict item outlet sales based on input features.",
    version="1.0.0"
)

# --- Add CORS Middleware ---
# This is the new section that fixes the CORS error.
# It allows your frontend (running on localhost:5173) to communicate with this backend.

# List of allowed origins (your frontend's URL)
# For production, you would replace "*" or the localhost URLs with your actual frontend domain.
origins = [
    "http://localhost:5174" , "http://localhost:5173",
    "http://localhost:3000", # Common port for Create React App
    "http://localhost:8080",
    "*" # Allows all origins, useful for development but be more specific in production
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods (GET, POST, etc.)
    allow_headers=["*"], # Allows all headers
)


# --- Model Loading ---
model_path = Path(__file__).parent / "models/sales_prediction_model.pkl"

if not model_path.exists():
    raise FileNotFoundError(f"Model file not found at {model_path}. Please ensure it's in the app/models/ directory.")

try:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    print("Model loaded successfully.")
except Exception as e:
    raise RuntimeError(f"Failed to load the model. Error: {e}")


# --- API Endpoints ---
@app.get("/", tags=["General"])
def read_root():
    """A simple endpoint to check if the API is running."""
    return {"message": "Welcome to the Sales Prediction API!"}


@app.post("/predict", response_model=PredictionOutput, tags=["Prediction"])
def predict_sales(payload: PredictionInput):
    """
    Predicts the item outlet sales based on input features.
    """
    try:
        processed_data = preprocess_input(payload)
        prediction = model.predict(processed_data)
        sales_prediction = float(prediction[0])
        return {"prediction": sales_prediction}

    except KeyError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid categorical value provided: {e}. Please check the input data."
        )
    except Exception as e:
        print(f"An error occurred during prediction: {e}")
        raise HTTPException(
            status_code=500,
            detail="An internal server error occurred. Please try again later."
        )
