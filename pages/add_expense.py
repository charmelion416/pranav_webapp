import pandas as pd
import streamlit as st
import os

if not os.path.exists('data'):
    os.makedirs("data")

if not os.path.exists("data/expenses.csv"):
    expenses = pd.DataFrame(columns = ["Date", "Category", "Description", "Currency", "Amount"])
    expenses.to_csv("data/expenses.csv",index=False)

date = st.date_input("Date :date:")
category = st.selectbox("Category 📁" ,("Food 🍪", "Personal Care 💅", "Traveling ✈️", "Real Estate 🏠", "Buisness 💼"))

desc = st.text_input("Description 📄", key = "description")
curr = st.selectbox("Currency 💲/💶", ("Dollars 💲", "Euros 💶"))
amt = st.number_input("Amount", max_value = 99999999, step = 1, key = "amount")

def insert():
    insert_csv(date, category, desc, curr, amt)
    
def insert_csv(date, category, description, currency, amount):
    dataFrame = pd.read_csv("data/expenses.csv")
    dataFrame.loc[len(dataFrame)] = [date, category, description, currency, amount]
    dataFrame.to_csv("data/expenses.csv",index=False)

button = st.button("Add Expense 💸",on_click = insert)

def clear():
    st.session_state.description = ""
    st.session_state.amount = 0 

buttonn = st.button("Clear Expense ❌", on_click = clear)