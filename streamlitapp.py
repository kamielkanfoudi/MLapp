import streamlit as st
import pandas as pd 
import altair as alt

st.title('Predicting Heat Disease with Ensemble Models')

st.set_page_config(page_title="Titanic Survival App")
overview = st.beta_container()
left, right = st.beta_columns(2)
prediction = st.beta_container()
