import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("JASAJE")
st.write(
    "Servicios Forestales Cia. Ltda."
)

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

st.subheader('Number of pickups by hour')




