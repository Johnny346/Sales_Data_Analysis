import streamlit as st
import pandas as pd
import numpy as np


st.title('Sales Data Analysis & Report')

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
all_data = pd.read_csv("Sales_Data_Analysis/Combined_sales_data.csv")
st.write(all_data) 
