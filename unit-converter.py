

import streamlit as st
import pandas as pd

# Custom CSS to style the app
def local_css():
    st.markdown("""
    <style>
    .main {
        padding: 20px;
    }
    .stSelectbox {
        margin-bottom: 20px;
    }
    .converter-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }
    .title {
        color: #1f1f1f;
        text-align: center;
        margin-bottom: 30px;
    }
    .result {
        background-color: #f0f2f5;
        padding: 20px;
        border-radius: 5px;
        margin-top: 20px;
        text-align: center;
        font-size: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Conversion functions
def temperature_convert(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    
    # Convert to Celsius first
    if from_unit == "Fahrenheit":
        celsius = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        celsius = value - 273.15
    else:
        celsius = value
    
    # Convert from Celsius to target unit
    if to_unit == "Fahrenheit":
        return (celsius * 9/5) + 32
    elif to_unit == "Kelvin":
        return celsius + 273.15
    return celsius

def length_convert(value, from_unit, to_unit):
    # Conversion to meters as base unit
    length_to_meters = {
        "Millimeters": 0.001,
        "Centimeters": 0.01,
        "Meters": 1,
        "Kilometers": 1000,
        "Inches": 0.0254,
        "Feet": 0.3048,
        "Yards": 0.9144,
        "Miles": 1609.34
    }
    
    # Convert to meters first, then to target unit
    meters = value * length_to_meters[from_unit]
    return meters / length_to_meters[to_unit]

def weight_convert(value, from_unit, to_unit):
    # Conversion to grams as base unit
    weight_to_grams = {
        "Milligrams": 0.001,
        "Grams": 1,
        "Kilograms": 1000,
        "Ounces": 28.3495,
        "Pounds": 453.592
    }
    
    # Convert to grams first, then to target unit
    grams = value * weight_to_grams[from_unit]
    return grams / weight_to_grams[to_unit]

def main():
    local_css()
    
    st.markdown("<h1 class='title'>Unit Converter</h1>", unsafe_allow_html=True)
    
    # Create container for converter
    # with st.container():
    #     st.markdown("<div class='converter-box'>", unsafe_allow_html=True)
        
        # Conversion type selector
    conversion_type = st.selectbox(
            "Select Conversion Type",
            ["Temperature", "Length", "Weight"]
        )
        
        # Define units for each conversion type
    units = {
            "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
            "Length": ["Millimeters", "Centimeters", "Meters", "Kilometers", 
                      "Inches", "Feet", "Yards", "Miles"],
            "Weight": ["Milligrams", "Grams", "Kilograms", "Ounces", "Pounds"]
        }
        
        # Create two columns for input and output
    col1, col2 = st.columns(2)
        
    with col1:
            from_unit = st.selectbox("From", units[conversion_type])
            value = st.number_input("Enter Value", value=0.0)
            
    with col2:
            to_unit = st.selectbox("To", units[conversion_type])
        
        # Perform conversion
    if st.button("Convert"):
            result = 0
            if conversion_type == "Temperature":
                result = temperature_convert(value, from_unit, to_unit)
            elif conversion_type == "Length":
                result = length_convert(value, from_unit, to_unit)
            elif conversion_type == "Weight":
                result = weight_convert(value, from_unit, to_unit)
            
            # Display result
            st.markdown(
                f"<div class='result'>{value} {from_unit} = {result:.4f} {to_unit}</div>",
                unsafe_allow_html=True
            )
        
    st.markdown("</div>", unsafe_allow_html=True)

    # Add footer
st.markdown("""
    <div style='text-align: center; color: #666; padding: 20px;'>
        Create with ❤️ by NISHA
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()