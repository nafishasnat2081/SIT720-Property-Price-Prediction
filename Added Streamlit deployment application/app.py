
import streamlit as st
import pandas as pd
import joblib


# Load trained model

model = joblib.load("property_price_model.pkl")


st.title("Property Sale Price Prediction")

st.write(
    "Enter property information to estimate the expected sale price."
)


market_region = st.selectbox(
    "Market Region",
    [
        "Surry Hills",
        "Campbelltown",
        "Greater Parramatta"
    ]
)


property_type = st.selectbox(
    "Property Type",
    [
        "Apartment",
        "House",
        "Unit",
        "Terrace",
        "Duplex/semi-detached"
    ]
)


bedrooms = st.number_input(
    "Bedrooms",
    min_value=0,
    value=2
)


bathrooms = st.number_input(
    "Bathrooms",
    min_value=0,
    value=1
)


car_spaces = st.number_input(
    "Car Spaces",
    min_value=0,
    value=1
)


building_size_sqm = st.number_input(
    "Building Size (sqm)",
    min_value=0.0,
    value=100.0
)


sale_month = st.number_input(
    "Sale Month",
    min_value=1,
    max_value=12,
    value=9
)


sale_year = st.number_input(
    "Sale Year",
    value=2026
)


total_rooms = bedrooms + bathrooms


price_per_sqm = st.number_input(
    "Price per sqm",
    min_value=0.0,
    value=10000.0
)



if st.button("Predict Sale Price"):

    input_data = pd.DataFrame({

        "market_region":[market_region],
        "property_type":[property_type],
        "bedrooms":[bedrooms],
        "bathrooms":[bathrooms],
        "car_spaces":[car_spaces],
        "building_size_sqm":[building_size_sqm],
        "sale_month":[sale_month],
        "sale_year":[sale_year],
        "total_rooms":[total_rooms],
        "price_per_sqm":[price_per_sqm]

    })


    prediction = model.predict(input_data)


    st.success(
        f"Predicted Sale Price: AUD {prediction[0]:,.2f}"
    )
