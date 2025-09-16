# Sales Forecasting App 📊

A full-stack machine learning application for product demand forecasting built with React frontend and Python FastAPI backend.

## 🚀 Features

- **Predictive Analytics**: Machine learning model for sales forecasting
- **Interactive Dashboard**: Beautiful React-based user interface
- **RESTful API**: FastAPI backend with comprehensive endpoints
- **Data Visualization**: Interactive charts and performance metrics
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## 🏗️ Project Structure
sales-forecasting-app/
├── backend/ # Python FastAPI Backend
│ ├── app/ # Main application
│ │ ├── core/ # Core functionality
│ │ ├── models/ # ML models
│ │ ├── schemas/ # Pydantic schemas
│ │ ├── init.py
│ │ └── main.py # FastAPI application
│ ├── requirements.txt # Python dependencies
│ └── Readme.md # Backend documentation
├── frontend/ # React Frontend
│ ├── src/
│ │ ├── components/ # React components
│ │ │ ├── PredictionForm.jsx
│ │ │ ├── ResultDisplay.jsx
│ │ │ └── HistoryChart.jsx
│ │ ├── assets/ # Static assets
│ │ ├── App.jsx # Main App component
│ │ └── main.jsx # Application entry point
│ ├── package.json # Node.js dependencies
│ └── vite.config.js # Vite configuration
└── README.md # This file

text

## ⚙️ Installation & Setup

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
Frontend Setup
bash
cd frontend
npm install
npm run dev
🎯 Usage
Start the backend server (runs on http://localhost:8000)

Start the frontend development server (runs on http://localhost:5173)

Open your browser and navigate to the frontend URL

Input your data and get sales predictions instantly

📊 API Endpoints
POST /api/predict - Get sales predictions

GET /api/history - Retrieve prediction history

GET /api/health - Check API status

🛠️ Technologies Used
Backend
Python 🐍

FastAPI ⚡

Scikit-learn 🤖

Pandas 📈

NumPy 🔢

Frontend
React ⚛️

Vite 🚀

Tailwind CSS 🎨

Recharts 📊

Axios 🔄

🤝 Contributing
Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request
