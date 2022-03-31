import streamlit as st
import pandas as pd 
import altair as alt
import pickle


st.set_page_config(page_title="Predicting Heat Disease with Ensemble Models")
overview = st.beta_container()
left, right = st.beta_columns(2)
prediction = st.beta_container()

