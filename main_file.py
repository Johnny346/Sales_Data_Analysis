import streamlit as st
import pandas as pd
import numpy as np


st.title('Sales Data Analysis & Report')

all_data = pd.read_csv("Sales_Data_Analysis/Combined_sales_data.csv")

all_data.head()
