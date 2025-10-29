# 🚗 Car Price Prediction App

**Live Demo:** [Click here to try it on Streamlit →](https://car-price-prediction-fgrpisdf7y98rqhccg3ncv.streamlit.app/)

A **Machine Learning Web App** that predicts car prices based on features like name, company, year, kilometers driven, and fuel type.

Built with:
- 🧠 **Linear Regression (Scikit-learn)**
- 🖥️ **Streamlit** for the web interface
- 📊 **Pandas** and **NumPy** for data handling


Model Details :-
Trained using Linear Regression on quikr_car.csv dataset.
The model was preprocessed using OneHotEncoder and saved as carPricePredictionModel.joblib.

pip install -r requirements.txt
streamlit run app.py
