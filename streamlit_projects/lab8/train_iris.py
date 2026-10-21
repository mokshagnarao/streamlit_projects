from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import streamlit as st
import joblib
import numpy as np

# Load Iris dataset
X, y = load_iris(return_X_y=True)

# Train Random Forest model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

# Load model
model = joblib.load("model.pkl")

# Flower classes
classes = ["Setosa", "Versicolor", "Virginica"]

# Streamlit UI
st.title("Iris Flower Prediction")

with st.form("prediction_form"):
    sl = st.slider("Sepal Length", 4.0, 8.0, 5.1)
    sw = st.slider("Sepal Width", 2.0, 4.5, 3.5)
    pl = st.slider("Petal Length", 1.0, 7.0, 1.4)
    pw = st.slider("Petal Width", 0.1, 2.5, 0.2)

    submit = st.form_submit_button("Predict")

if submit:
    features = np.array([[sl, sw, pl, pw]])

    pred = model.predict(features)[0]
    proba = model.predict_proba(features)[0]

    st.success(f"Prediction: **{classes[pred]}**")
    st.metric("Confidence", f"{max(proba) * 100:.1f}%")