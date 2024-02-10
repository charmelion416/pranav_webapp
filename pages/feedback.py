import streamlit as st
import pandas as pd
import os

if not os.path.exists("data/feedback.csv"):
    asdf = pd.DataFrame(columns = ["Name", "Feedback", "Rating"])
    asdf.to_csv("data/feedback.csv",index=False)

name = st.text_input("Name")
feedback = st.text_input("Feedback")

rating = st.slider("Rating", min_value = 1, max_value = 5)

if rating == 1:
    st.subheader("The worst it can possibly be 😭")

if rating == 2:
    st.subheader("Getting better... 😑")

if rating == 3:
    st.subheader("Above average 🙂")

if rating == 4:
    st.subheader("Really nice... 😀")

if rating == 5:
    st.subheader("The best it can possibly be 😁")

def submit():
    submit_csv(name, feedback, rating)

def submit_csv(name, feedback, rating):
    dataFrame = pd.read_csv("data/feedback.csv")
    dataFrame.loc[len(dataFrame)] = [name, feedback, rating]
    dataFrame.to_csv("data/feedback.csv",index=False)
    st.balloons()


sumitt = st.button("Submit", on_click = submit)