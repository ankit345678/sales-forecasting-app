
# Sales Forecasting ML Project

A full-stack machine learning application for predicting product demand using XGBoost, served with a FastAPI backend and a modern web frontend.

## 🚀 Tech Stack

- **Backend:** Python, FastAPI
- **Machine Learning:** XGBoost, Scikit-learn, Pandas, NumPy
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Local development setup (Ready for production deployment)

## 📁 Project Structure
Final_year/
├── backend/
│ ├── app/ # Python application code (FastAPI routes)
│ ├── requirements.txt # Python dependencies list
│ └── .gitignore # Files to exclude from version control
├── frontend/
│ ├── index.html # Main frontend page
│ ├── style.css # Styling for the frontend
│ └── script.js # JavaScript for API calls and interactivity
└── README.md # This project overview file

text

## ⚡ Setup & Installation

1.  **Clone the repository**
    ```bash
    git clone <your-repository-url>
    cd Final_year
    ```

2.  **Backend Setup**
    ```bash
    cd backend
    pip install -r requirements.txt
    uvicorn app.main:app --reload
    ```
    The API server will run at `http://localhost:8000`

3.  **Frontend Setup**
    ```bash
    cd ../frontend
    # Open index.html in a web browser or use a local server
    ```
    The frontend will communicate with the backend API to display predictions.

## 📊 Key Features

- Demand forecasting using machine learning
- RESTful API architecture
- Interactive web interface
- Model performance visualization (R² score: 0.609, MAE: 739.74)

## 🔌 API Endpoints

- `POST /predict` - Accepts input data and returns demand forecasts
- Automatic interactive API documentation at `/docs` when server is running


