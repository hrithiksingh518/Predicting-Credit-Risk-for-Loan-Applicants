from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load("model/best_model_stacking_knn_gb.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = {
            'Age': int(request.form['age']),
            'Sex': request.form['sex'],
            'Job': int(request.form['job']),
            'Housing': request.form['housing'],
            'Saving accounts': request.form['savings'],
            'Checking account': request.form['checking'],
            'Credit amount': int(request.form['credit']),
            'Duration': int(request.form['duration']),
            'Purpose': request.form['purpose']
        }

        input_df = pd.DataFrame([data])
        prediction = model.predict(input_df)[0]
        risk = "Good Risk" if prediction == 1 else "Bad Risk"
        return render_template('index.html', prediction_text=f'Loan Status: {risk}')

if __name__ == '__main__':
    app.run(debug=True)
