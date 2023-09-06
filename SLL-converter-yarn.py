import streamlit as st
import math
import pandas as pd
from PIL import Image

favicon = Image.open('sci-lume-fav_BW.png')

st.set_page_config(page_title="SLL Yarn Conversion", page_icon=favicon)

def convert_yarn_units(value, density, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    conversion_factors = {
        ('Denier', 'Decitex'): value * (10 / 9),
        ('Denier', 'Tex'): value * (1 / 9),
        ('Denier', 'g/m'): value * (1 / 9000),
        ('Denier', 'Micrometers'): math.sqrt((((value / 9000) / (density / 1e-6)) * 1e12) / math.pi) * 2,
        ('Denier', 'English Cotton Count'): ((value / (9000 * 1.09361 * 453.59237)) ** -1) / 840,
        ('Denier', 'Worsted'): ((value / (9000 * 1.09361 * 453.59237)) ** -1) / 560,
        ('Decitex', 'Denier'): (9 / 10),
        ('Decitex', 'Tex'): (1 / 10),
        ('Decitex', 'g/m'): (1 / 10000),
        ('Decitex', 'Micrometers'): math.sqrt((((value / 10000) / (density / 1e-6)) * 1e12) / math.pi) * 2,
        ('Decitex', 'English Cotton Count'): ((value / (10000 * 1.09361 * 453.59237)) ** -1) / 840,
        ('Decitex', 'Worsted'): ((value / (10000 * 1.09361 * 453.59237)) ** -1) / 560,
        ('Tex', 'Denier'): 9,
        ('Tex', 'Decitex'): 10,
        ('Tex', 'g/m'): (1 / 1000),
        ('Tex', 'Micrometers'): math.sqrt((((value / 1000) / (density / 1e-6)) * 1e12) / math.pi) * 2,
        ('Tex', 'English Cotton Count'): ((value / (1000 * 1.09361 * 453.59237)) ** -1) / 840,
        ('Tex', 'Worsted'): ((value / (1000 * 1.09361 * 453.59237)) ** -1) / 560,
        ('g/m', 'Denier'): (value * 9000),
        ('g/m', 'Decitex'): (value * 10000),
        ('g/m', 'Tex'): (value * 1000),
        ('g/m', 'Micrometers'): math.sqrt((((value) / (density / 1e-6)) * 1e12) / math.pi) * 2,
        ('g/m', 'English Cotton Count'): ((value / (1.09361 * 453.59237)) ** -1) / 840,
        ('g/m', 'Worsted'): ((value / (1.09361 * 453.59237)) ** -1) / 560,
        ('Micrometers', 'Denier'): ((math.pi * ((value / 2.0) ** 2) * 1e-12) * (density / 1e-6) * 9000),
        ('Micrometers', 'Decitex'): ((math.pi * ((value / 2.0) ** 2) * 1e-12) * (density / 1e-6) * 10000),
        ('Micrometers', 'Tex'): ((math.pi * ((value / 2.0) ** 2) * 1e-12) * (density / 1e-6) * 1000),
        ('Micrometers', 'g/m'): ((math.pi * ((value / 2.0) ** 2) * 1e-12) * (density / 1e-6)),
        ('Micrometers', 'English Cotton Count'): math.sqrt(
            (((math.pi * ((value / 2.0) ** 2) * 1e-12) * (density / 1e-6)) * 0.9144 / 453.59237) ** -1) / 840,
        ('Micrometers', 'Worsted'): math.sqrt(
            (((math.pi * ((value / 2.0) ** 2) * 1e-12) * (density / 1e-6)) * 0.9144 / 453.59237) ** -1) / 560,
        ('English Cotton Count', 'Decitex'): (
            ((value * 840 * 0.9144 / 453.592370) ** -1) * 10000),
        ('English Cotton Count', 'Tex'): (
            ((value * 840 * 0.9144 / 453.592370) ** -1) * 1000),
        ('English Cotton Count', 'g/m'): (
            ((value * 840 * 0.9144 / 453.592370) ** -1)),
        ('English Cotton Count', 'Micrometers'): math.sqrt(
            (((((value * 840 * 0.9144 / 453.592370) ** -1)) / (density / 1e-6)) * 1e12) / math.pi) * 2,
        ('English Cotton Count', 'Denier'): (
            ((value * 840 * 0.9144 / 453.592370)) ** -1 * 9000),
        ('English Cotton Count', 'Worsted'): ((value * 840) / 560),
        ('Worsted', 'Decitex'): (
            ((value * 560 * 0.9144 / 453.592370)) ** -1 * 10000),
        ('Worsted', 'Tex'): (
            ((value * 560 * 0.9144 / 453.592370)) ** -1 * 1000),
        ('Worsted', 'g/m'): (
            ((value * 560 * 0.9144 / 453.592370)) ** -1),
        ('Worsted', 'Micrometers'): math.sqrt(
            (((((value * 560 * 0.9144 / 453.592370)) ** -1) / (density / 1e-6)) * 1e12) / math.pi) * 2,
        ('Worsted', 'English Cotton Count'): ((value * 560) / 840),
        ('Worsted', 'Denier'): (
            ((value * 560 * 0.9144 / 453.592370)) ** -1 * 9000),
    }

    return conversion_factors[(from_unit, to_unit)]

# Yarn Conversion Part
# st.title("Yarn Unit Conversion") commented out for metadata as per recommendations
st.header("Yarn Unit Conversion")
st.text("A simple app to convert between different yarn measurements")

mcol1, mcol2 = st.columns([1, 2])

# Define the units for conversion
# units_old = ['Denier', 'Decitex', 'Tex', 'g/m', 'Micrometers', 'English Cotton Count', 'Worsted']
# no g/m in the thing because it probably isn't useful and I cannot figure out how to format it good
units = ['Denier', 'Decitex', 'Tex', 'Micrometers', 'English Cotton Count', 'Worsted']
tableunits = ['Denier (g/9,000 m)', 'Decitex (g/10,000 m)', 'Tex (g/1,000 m)', 'Micrometers (0.000001 m)', 'English Cotton Count (840 yd/lbs)', 'Worsted (560 yd/lbs)']
# for later: add woolen (256 yd/lbs) and metric count (1000m/kg)

# Add number input field
with mcol1:
    value = st.number_input("Enter a Yarn Size:", value=1.00)

    # Add unit selection dropdown
    from_unit = st.selectbox("Measurement:", units)

    # Density of the material if wanting Microns
    density = st.number_input("Density (g/mL) of the material:", value=1.00)

# Calculate and display the converted measurements
with mcol2:

    converted_list = []
    for to_unit in units:
        converted_list.append(convert_yarn_units(value, density, from_unit, to_unit))

    data = {
        'Unit': tableunits,
        'Value': converted_list,
    }

    df = pd.DataFrame(data) # , index=units)

    # formatted_df = df.style.format({"Value": "{:.2f}"})  # Format other indices with 2 decimal places
    # formatted_df = formatted_df.format({"Value": "{:.6f}"}, subset=pd.IndexSlice['g/m', :])  # Format 'g/m' index with 6 decimal places

    # st.table(formatted_df)
    # st.dataframe(df, hide_index=True)
    st.data_editor(
    df,
    column_config={
        "Unit": st.column_config.TextColumn(
            "Unit (definition)",
            disabled=True,
        ),
        "Value": st.column_config.NumberColumn(
            "Value",
            format="%.2f",
            disabled=True,
        )
    },
    hide_index=True,
    )
