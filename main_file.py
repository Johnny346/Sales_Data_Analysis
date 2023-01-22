import streamlit as st
import pandas as pd
import numpy as np


st.title('Sales Data Analysis & Report')

all_data = pd.read_csv(r"https://github.com/Johnny346/Sales_Data_Analysis/blob/main/Combined_sales_data.csv")

all_data.head()
