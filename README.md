# Walmart Sales Prediction Using Machine Learning

## 📌 Project Overview

The **Walmart Sales Prediction** project uses Machine Learning to predict weekly sales based on store information and economic indicators. An XGBoost Regressor is trained on historical Walmart sales data to estimate weekly sales for user-provided inputs.

The project includes data analysis, model training, evaluation, and a web application built using FastAPI and HTML/CSS.

## 🎯 Objectives

* Analyze Walmart sales data to identify sales patterns and trends.
* Explore the relationship between weekly sales and economic indicators.
* Train and evaluate multiple regression models.
* Select an XGBoost Regressor for sales prediction.
* Develop a user-friendly web application for generating predictions.

## 🛠️ Technologies Used

* **Python** – Programming language
* **Pandas & NumPy** – Data manipulation and numerical operations
* **Matplotlib & Seaborn** – Data visualization and exploratory analysis
* **Scikit-learn** – Model evaluation and machine learning utilities
* **XGBoost** – Weekly sales prediction
* **FastAPI** – Backend web framework
* **HTML & CSS** – Frontend interface
* **Pickle** – Saving and loading the trained model
* **Jupyter Notebook** – Data analysis and model development

## 📊 Dataset Description

The project uses a cleaned Walmart sales dataset containing store-level sales information.

Important features include:

| Feature        | Description                                   |
| -------------- | --------------------------------------------- |
| `Store`        | Store identifier                              |
| `Holiday_Flag` | Indicates whether the week includes a holiday |
| `Temperature`  | Temperature recorded for the store            |
| `Fuel_Price`   | Fuel price during the relevant period         |
| `CPI`          | Consumer Price Index                          |
| `Unemployment` | Unemployment rate                             |
| `Weekly_Sales` | Target variable representing weekly sales     |

The `Date` column is removed during model training in the current implementation.

## ⚙️ Machine Learning Workflow

1. Load and inspect the cleaned dataset.
2. Perform exploratory data analysis.
3. Separate the independent features and target variable.
4. Split the data into training and testing sets.
5. Train and compare multiple regression algorithms:

   * Linear Regression
   * Ridge Regression
   * Lasso Regression
   * K-Nearest Neighbors Regressor
   * Decision Tree Regressor
   * Random Forest Regressor
   * XGBoost Regressor
   * AdaBoost Regressor
6. Evaluate model performance using:

   * R² Score
   * Mean Absolute Error (MAE)
   * Mean Squared Error (MSE)
   * Root Mean Squared Error (RMSE)
7. Save the trained XGBoost model as `xgb_model.pkl`.
8. Integrate the saved model into a FastAPI web application.

## 🤖 Model Information

**Selected Model:** XGBoost Regressor

**Problem Type:** Supervised Machine Learning – Regression

**Target Variable:** `Weekly_Sales`

The model predicts a continuous sales value based on the input features provided by the user.

Model performance metrics should be added after confirming the final evaluation results.

## 🌐 Web Application Features

* Clean and responsive dashboard interface.
* Input form for store and economic information.
* Holiday selection.
* Instant prediction through the trained model.
* Display of estimated weekly sales.
* FastAPI-powered prediction endpoint.

## 📁 Project Structure

```text
Walmart_project/
│
├── app/
│   └── main.py
│
├── static/
│   └── index.html
│
├── env/
│
└── walmart_sales_analysis/
    ├── data/
    │   └── Walmart_cleaned.csv
    │
    ├── notebook/
    │   ├── Analysis.ipynb
    │   ├── data_cleaning.ipynb
    │   ├── machine_learning.ipynb
    │   └── xgb_model.pkl
    │
    └── README.md
```

*Note: Adjust the structure above if your actual folders or filenames differ.*

## 🚀 How to Run the Application

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd Walmart_project
```

### 2. Activate Your Python Environment

On Windows PowerShell:

```powershell
.\env\Scripts\Activate.ps1
```

Create or activate an environment appropriate to your own setup if `env` is not included in the repository.

### 3. Install Required Packages

Install the required packages if they are not already installed:

```bash
python -m pip install fastapi uvicorn pandas scikit-learn xgboost python-multipart
```

### 4. Verify the Model Path

Ensure `xgb_model.pkl` is available at the path configured in `app/main.py`.

### 5. Start the FastAPI Server

From the project root directory, run:

```bash
python -m uvicorn app.main:app --reload
```

### 6. Open the Application

Visit:

```text
http://127.0.0.1:8000
```

Enter the required store details and submit the form to view the predicted weekly sales.

## 📈 Evaluation Metrics

The following metrics are used to evaluate regression model performance:

* **R² Score:** Measures how well the model explains variation in the target.
* **MAE:** Measures the average absolute prediction error.
* **MSE:** Measures the average squared prediction error.
* **RMSE:** Measures prediction error on the target's scale.

The final model's actual evaluation scores can be added here once verified.

## 🔮 Future Improvements

* Add sales trend visualizations to the dashboard.
* Improve feature engineering and model tuning.
* Add historical sales comparisons.
* Enhance input validation and error handling.
* Deploy the application to a cloud platform.
* Add model performance summaries to the web interface.

## 👩‍💻 Author

**Muskan Yadav**

Data Analytics and Machine Learning Project

## 📄 Disclaimer

This project is intended for educational and analytical purposes. Predictions are estimates generated by a machine learning model and may differ from actual Walmart sales.
