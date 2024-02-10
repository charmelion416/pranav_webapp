import streamlit as st
import pandas as pd
import os

if not os.path.exists("data") and not os.path.exists("data/expenses.csv"):
    st.write("Add some expenses before viewing it.")

else:
    DataFrame = pd.read_csv("data/expenses.csv")
    st.dataframe(DataFrame)