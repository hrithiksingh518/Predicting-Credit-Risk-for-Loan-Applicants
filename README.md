#  German Credit Risk Predictor

A web-based application that predicts **loan risk** (Good or Bad) based on a user's financial and personal information. This tool is built using **Flask** and a **stacked machine learning model** trained on the German Credit Risk dataset.

##  Features

-  User-friendly form interface
-  Machine Learning backend using stacked KNN + Gradient Boosting
-  Instant prediction of loan applicant's credit risk

##  Tech Stack

- **Frontend:** HTML, CSS (Jinja templates)
- **Backend:** Flask (Python)
- **Modeling:** scikit-learn, joblib, pandas
- **Deployment Ready:** Localhost (Flask) with potential for cloud deployment

##  Project Structure

## Input Features

The following fields are required to assess credit risk:

- **Age** (numeric)
- **Sex** (male/female)
- **Job** (categorical: 0–3)
- **Housing** (own/rent/free)
- **Saving accounts** (little/moderate/quite rich/rich)
- **Checking account** (little/moderate/rich)
- **Credit amount** (numeric)
- **Duration (months)** (numeric)
- **Purpose** (e.g., car, education, business, vacation, etc.)

##  About the Model

The prediction is powered by an ensemble machine learning model:

- **K-Nearest Neighbors (KNN)**
- **Gradient Boosting Classifier**

These were stacked and trained using historical German credit data, and saved as `best_model_stacking_knn_gb.pkl`.

##  Sample Prediction

Try inputs like:

- Age: 35
- Sex : Male
- Job: 2
- Housing: own
- saving account : moderate
- checking account : Rich
- Credit amount: 2000  
- Duration: 24 months  
- Purpose: Business

And get predictions such as: -Loan Status: Bad Risk

## Output of the Project 

<img width="1208" alt="Screenshot 2025-04-25 at 11 21 23 PM" src="https://github.com/user-attachments/assets/26c7a930-5fec-4003-87bc-2db2ccaa4d1d" />








