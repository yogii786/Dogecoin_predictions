import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.style.use('seaborn-whitegrid')


import streamlit as st
st.title("Future price prediction model")
df = st.text_input("Let's predict the Future prices")

if df == "Dogecoin":
    data = pd.read_csv("dogecoin.csv")
    print(data.head())
    data.dropna()
    from autots import AutoTS
    model = AutoTS(forecast_length=10, frequency='infer', ensemble='simple', drop_data_older_than_periods=200)
    model = model.fit(data, date_col="Date", value_col="Close", id_col=None)
    prediction = model.predict()
    forecast = prediction.forecast
    st.write(forecast)