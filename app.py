import streamlit as st
import joblib
import numpy as np
import pandas as pd
import sys

# 'sys', let's our code talk to python interpretor.

st.set_page_config(page_title="Car Price Predictor", layout="centered")

# Load model safety

try:
    model = joblib.load("carPricePredictionModel.joblib")
except Exception as e:
    st.error("Failed to laod model. See console for details.")
    print("Model load error: ", e, file=sys.stderr)
    # Optional : Show sklearn version for debugging

    try:
        import sklearn

        print("Sklearn version: ", sklearn.__version__, file=sys.stderr)
    except Exception:
        pass
    st.stop()

st.title("Car Price Predictor")

# Inputs
name = st.text_input("Car Name (eg i20)")
company = st.text_input("Company (eg. Hyundai)")
year = st.number_input("Year", min_value=1990, max_value=2025, value=2017)
kms_driven = st.text_input("Kms Driven (numbers only eg. 40000)", value="40000")
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])

# Helper to clean kms input


def clean_kms(kms_str):
    if kms_str is None:
        return np.nam
    # remove commas and non-digit characters
    cleaned = "".join(ch for ch in str(kms_str) if ch.isdigit())
    return int(cleaned) if cleaned != "" else np.nan


if st.button("Predict Price"):
    # Validate & preprocess input like training
    kms_val = clean_kms(kms_driven)
    if pd.isna(kms_val):
        st.warning("Please enter a valid numeric value for Kms Driven")
    elif not name or not company:
        st.warning("Please fill Car Name and Company")
    else:
        input_df = pd.DataFrame(
            [[name.strip(), company.strip(), year, kms_val, fuel_type]],
            columns=["name", "company", "year", "kms_driven", "fuel_type"],
        )

        # Predcit with error handling
        try:
            price = model.predict(input_df)
            pred_val = float(price[0])
            st.success(f"Predicted Price : Rs{int(pred_val):,}")
        except Exception as e:
            st.error("Prediction failed. ")
            print("Prediction Error", e, file=sys.stderr)
