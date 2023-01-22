import streamlit as st
import pandas as pd
import numpy as np


st.title('Sales Data Analysis & Report')

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

path = 'Combined_sales_data.csv'
df = pd.read_csv(path, encoding='ISO-8859-1')

st.write(df.head()) 


## ----------------------
## add month column
all_data['Month'] = df['Order Date'].str[0:2]
all_data['Month'] = df['Month'].astype('int32')

st.write(all_data.head()) 
