import streamlit as st
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt

# Function to preprocess input data
def preprocess_input(input_data):
    # Replace null values in 'Price' column with the mean
    input_data['Price'].fillna(input_data['Price'].mean(), inplace=True)

    # Replace 'cochiin' with 'cochin' in the 'Location' column
    input_data['Location'] = input_data['Location'].replace('COCHIIN', 'COCHIN')

    # Apply ordinal encoding to the 'Location' column
    location_order = {'CHENNAI': 1, 'COCHIN': 2, 'DELHI': 3, 'GANGTOK': 4, 'Missing': 5}
    input_data['Location_encoded'] = input_data['Location'].map(location_order)

    # Convert 'Month&Year' to datetime format
    input_data['Month&Year'] = pd.to_datetime(input_data['Month&Year'], format='%b-%y')

    # Drop unnecessary columns
    input_data.drop(['Location', 'Grade'], axis=1, inplace=True)

    return input_data

# Function to calculate MAPE
def mean_absolute_percentage_error(y_true, y_pred): 
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    y_true = y_true + 1e-8  # Avoid division by zero
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

# Function to forecast spice prices using Moving Average model
def forecast_spice(data, spice):
    spice_data = data[data['Spices'] == spice].set_index('Month&Year')
    
    # Ensure there is enough data for training and testing
    if len(spice_data) <= 12:
        st.error(f"Not enough data to forecast prices for {spice}. Need more than 12 months of data.")
        return None, None, None

    train = spice_data[:-12]
    test = spice_data[-12:]

    # Check if the training set is empty
    if train.empty:
        st.error(f"No training data available for {spice}. Check your dataset.")
        return None, None, None

    try:
        model = ARIMA(train['Price'], order=(0,0,1))  # MA model
        model_fit = model.fit()
        predictions = model_fit.predict(start=len(train), end=len(train) + len(test) - 1)
        rmse = sqrt(mean_squared_error(test['Price'], predictions))
        mape = mean_absolute_percentage_error(test['Price'], predictions)
        return rmse, mape, predictions
    except ValueError as e:
        st.error(f"An error occurred while fitting the model for {spice}: {e}")
        return None, None, None


# Streamlit app
def main():
    st.title("Spice Price Prediction App")

    uploaded_file = st.file_uploader("Choose a EXCEL file", type="xlsx")
    if uploaded_file is not None:
        input_data = pd.read_excel(uploaded_file)
        preprocessed_data = preprocess_input(input_data)
        spices = preprocessed_data['Spices'].unique()

        results = {}
        for spice in spices:
            rmse, mape, predictions = forecast_spice(preprocessed_data, spice)
            results[spice] = {
                'RMSE': rmse,
                'MAPE': mape,
                'Predictions': predictions
            }

        # Display the predictions and accuracy metrics
        for spice, result in results.items():
            st.write(f"### Spice: {spice}")
            st.write(f"**RMSE:** {result['RMSE']:.2f}")
            st.write(f"**MAPE:** {result['MAPE']:.2f}%")
            st.write("**Predictions:**")
            st.write(result['Predictions'])

            # Visualize the predictions
            st.write("**Prediction Visualization:**")
            plt.figure(figsize=(10, 5))
            plt.plot(result['Predictions'])
            plt.title(f'Predicted Prices for {spice}')
            plt.xlabel('Month & Year')
            plt.ylabel('Price')
            st.pyplot(plt)

if __name__ == "__main__":
    main()

